import pandas as pd
import numpy as np
import requests
from get_mail_mailru import main as mail_main
from parser_broker_report import main as parser_main


def fix_split(ticker_list, transactions, transactions_executed, share_split_dict):
    ticker_list_copy = ticker_list.copy()
    for ticker in ticker_list_copy:
        if ticker == 'RU000A101FA1':
            new_ticker = 'SU25084RMFS3'
            ticker_list.remove(ticker)
            ticker_list.append(new_ticker)
            transactions_executed.loc[transactions['Код'] == ticker, 'Код'] = new_ticker
        if ticker == 'VTBE':
            new_ticker = 'RSHE'
            ticker_list.remove(ticker)
            ticker_list.append(new_ticker)
            transactions_executed.loc[transactions['Код'] == ticker, 'Код'] = new_ticker
    for ticker in ticker_list:
        if ticker in share_split_dict:
            transactions_executed.loc[(transactions_executed['Код'] == ticker) &
                                      (transactions_executed['Дата заключения'] <
                                       share_split_dict[ticker][0]), 'Количество'] =\
                (transactions_executed.loc[(transactions_executed['Код'] == ticker) &
                                           (transactions_executed['Дата заключения'] <
                                           share_split_dict[ticker][0]), 'Количество'] *
                 share_split_dict[ticker][1])


def get_share_price_dict(tickers: list, transactions_executed):
    share_price_dict = {}
    for ticker in tickers:
        if ticker in ['SBMX', 'AFKS']:
            round_numb = 3
        elif ticker in ['IRAO']:
            round_numb = 4
        else:
            round_numb = 2
        share = transactions_executed[transactions_executed['Код'] == ticker]
        share_price = ((share['Сумма'].sum() + share['Комиссия Брокера'].sum() + share['Комиссия Биржи'].sum()) /
                       (share.loc[share['Вид'] == 'Покупка', 'Количество'].sum() -
                        share.loc[share['Вид'] == 'Продажа', 'Количество'].sum())).round(round_numb)
        share_price_dict[ticker] = share_price
    return share_price_dict


def get_share_amount_dict(tickers: list, transactions_executed):
    share_amount_dict = {}
    for ticker in tickers:
        share_amount_dict[ticker] = (transactions_executed.loc[transactions_executed['Код'] == ticker, 'Количество']
                                     .sum())
    return share_amount_dict


def get_trading_dict():
    trading_dict = {}
    trading_mode_list = ['TQBR', 'TQTF', 'TQCB', 'TQOB']
    for id_trading in trading_mode_list:
        stocks = 'shares'
        if id_trading in ['TQOB', 'TQCB']:
            stocks = 'bonds'
        url = (f"https://iss.moex.com/iss/engines/stock/markets/{stocks}/boards/{id_trading}/" 
               f"securities.csv?iss.meta=off&iss.only=marketdata&marketdata.columns=SECID,LAST")
        csv_text = requests.get(url).text.split('\n')
        trading_dict[id_trading] = csv_text
    return trading_dict


def get_last_prices_dict(tickers: list):
    last_prices_dict = {}
    trading_dict = get_trading_dict()
    for ticker in tickers:
        if ticker == 'RU000A101FA1':
            ticker = 'SU25084RMFS3'
        if ticker == 'VTBE':
            ticker = 'RSHE'
        for value in trading_dict.values():
            for line in value:
                line = line.split(';')
                if ticker in line:
                    last_prices_dict[ticker] = line[1]
    return last_prices_dict


def get_commission_dict(tickers: list, transactions_executed):
    commission_dict = {}
    for ticker in tickers:
        commission_dict[ticker] = (transactions_executed.loc[transactions_executed['Код'] ==
                                                             ticker, 'Комиссия Брокера'] +
                                   transactions_executed.loc[transactions_executed['Код'] == ticker,
                                   'Комиссия Биржи']).sum().round(2)
    return commission_dict


def get_coupon_dict(tickers: list):
    coupon_dict = {}
    url = "https://iss.moex.com/iss/engines/stock/markets/bonds/boards/TQOB/securities.csv?iss.meta=off&iss.only" \
          "=securities&securities.columns=SECID,ACCRUEDINT "
    csv_text = requests.get(url).text.split('\n')

    for ticker in tickers:
        for line in csv_text:
            line = line.split(';')
            if ticker in line:
                coupon_dict[ticker] = line[1]
    return coupon_dict


def main():
    mail_main()
    parser_main()

    portfolio = pd.read_csv('portfolio.csv')
    portfolio['Дата'] = portfolio['Дата'].astype('datetime64[ns]')
    transactions = pd.read_csv('transactions.csv').drop_duplicates(['Дата заключения', 'Время заключения', 'Статус'])
    # transactions['Дата заключения'] = pd.to_datetime(transactions['Дата заключения'] +
    #                                                  ' ' + transactions['Время заключения'], dayfirst=True)
    # transactions['Дата расчетов'] = pd.to_datetime(transactions['Дата расчетов'], dayfirst=True)
    transactions = transactions.drop('Время заключения', axis=1)\
                               .dropna(axis=1).sort_values('Дата заключения').reset_index(drop=True)
    transactions_executed = transactions[transactions['Статус'] == 'И']

    ticker_list = list(transactions_executed['Код'].unique())
    share_split_dict = {
        'FXGD': ['2022-02-17', 10],
        'SBMX': ['2021-06-09', 100],
        'FXUS': ['2022-01-24', 100],
        'FXRL': ['2021-11-24', 100],
        'FXRU': ['2022-02-17', 10],
        'FXDE': ['2021-12-15', 100]
    }
    # replacement_dict = {
    #     'VTBE': 'RSHE',
    #     'RU000A101FA1': 'SU25084RMFS3'
    # }

    fix_split(ticker_list, transactions, transactions_executed, share_split_dict)
    share_price_dict = get_share_price_dict(ticker_list, transactions_executed)
    share_amount_dict = get_share_amount_dict(ticker_list, transactions_executed)
    last_prices_dict = get_last_prices_dict(ticker_list)
    commission_dict = get_commission_dict(ticker_list, transactions_executed)
    coupon_dict = get_coupon_dict(ticker_list)

    portfolio_dict = {
        'Котировки': last_prices_dict,
        'НКД': coupon_dict,
        'Количество': share_amount_dict,
        'Средняя цена': share_price_dict,
        'Комиссия': commission_dict
    }

    main_df = pd.DataFrame.from_dict(portfolio_dict)
    main_df.index.name = 'Название'
    main_df.loc[main_df['Котировки'] == '', 'Котировки'] = np.nan
    main_df.dropna(axis=0, subset='Котировки', inplace=True)
    main_df[['Котировки', 'НКД']] = main_df[['Котировки', 'НКД']].astype('float64')
    main_df['Текущая цена'] = main_df['Котировки'] * main_df['Количество']
    main_df['P/L, руб.'] = main_df['Текущая цена'] - main_df['Средняя цена'] * main_df['Количество']
    main_df['P/L, %'] = (main_df['Котировки'] * 100 / main_df['Средняя цена'] - 100).round(2)

    # bond_price, bond_NKD, bond_amount, bond_average_price, bond_commission = \
    #     main_df.loc['SU25084RMFS3', 'Котировки'], \
    #     main_df.loc['SU25084RMFS3', 'НКД'], \
    #     main_df.loc['SU25084RMFS3', 'Количество'], \
    #     main_df.loc['SU25084RMFS3', 'Средняя цена'], \
    #     main_df.loc['SU25084RMFS3', 'Комиссия']

    # main_df.loc['SU25084RMFS3', 'Котировки'] = bond_price * 10
    # main_df.loc['SU25084RMFS3', 'Текущая цена'] = (bond_price * 10 + bond_NKD) * bond_amount
    # main_df.loc['SU25084RMFS3', 'P/L, руб.'] = (main_df.loc['SU25084RMFS3', 'Текущая цена'] -
    #                                             bond_average_price * bond_amount)
    # main_df.loc['SU25084RMFS3', 'P/L, %'] = (((bond_price * 10 + bond_NKD) * 100 / bond_average_price) - 100).round(2)

    main_df.to_csv(path_or_buf='portfolio_main.csv', index_label=False)


if __name__ == '__main__':
    main()
