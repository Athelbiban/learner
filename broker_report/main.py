import pandas as pd
import numpy as np
import requests
import json
from get_mail_mailru import main as mail_main
from parser_broker_report import main as parser_main


def fix_split(ticker_list, transactions, transactions_executed, share_split_dict):

    replacement_dict = {
        'VTBE': 'RSHE',
        'RU000A102HB1': 'SU26227RMFS7',
        'RU000A1038V6': 'SU26238RMFS4',
        'RU000A101QE0': 'SU26234RMFS3'
    }

    ticker_list_copy = ticker_list.copy()
    for ticker in ticker_list_copy:

        if ticker in replacement_dict:
            new_ticker = replacement_dict[ticker]
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


def get_stock_data_dict(tickers: list, transactions_executed):

    round_numb_3_list = ['LKOH', 'MGNT']
    round_numb_4_list = ['IRAO', 'MOEX', 'YDEX', 'SBMM']
    round_numb_5_list = ['HYDR', 'AFKS']
    round_numb_6_list = ['GAZP', 'MTSS', 'NVTK', 'ROSN', 'SBER', 'CHMF', 'SNGS', 'SBGD', 'SBMX', 'AFKS', 'AFLT', 'RTKM']

    share_amount_dict = {}
    share_price_dict = {}
    share_commission_dict = {}
    for ticker in tickers:

        if ticker in round_numb_3_list:
            round_numb = 3
        elif ticker in round_numb_4_list:
            round_numb = 4
        elif ticker in round_numb_5_list:
            round_numb = 5
        elif ticker in round_numb_6_list:
            round_numb = 6
        else:
            round_numb = 2

        share_frame = transactions_executed[transactions_executed['Код'] == ticker]
        share_list = list(zip(share_frame['Вид'], share_frame['Количество'], share_frame['Сумма'],
                              share_frame['Комиссия Брокера'], share_frame['Комиссия Биржи']))

        share_amount = share_price_avg = share_total_cost = share_commission = 0
        for i in range(len(share_list)):

            share_type = share_list[i][0]
            amount_new = share_list[i][1]
            share_total_cost_new = share_list[i][2]
            share_commission_new = share_list[i][3] + share_list[i][4]

            if share_type == 'Покупка':
                share_amount += amount_new
                share_total_cost += share_total_cost_new
                share_commission += share_commission_new
                share_price_avg = round((share_total_cost + share_commission) / share_amount, round_numb)

            elif share_type == 'Продажа':
                share_amount -= amount_new
                share_total_cost = share_amount * share_price_avg

                if share_amount > 0:
                    share_commission += share_commission_new
                else:
                    share_commission = 0

            else:
                raise Exception('Неверный вид транзакции')

        share_amount_dict[ticker] = share_amount
        share_price_dict[ticker] = share_price_avg
        share_commission_dict[ticker] = round(share_commission, 2)

    return share_amount_dict, share_price_dict, share_commission_dict


def get_last_prices_dict(tickers: list, bond_tickers: list):

    last_prices_dict = {}
    trading_list = []
    trading_mode_list = ['TQBR', 'TQTF', 'TQCB', 'TQOB', 'TQIR']
    for id_trading in trading_mode_list:

        stocks = 'shares'
        if id_trading in ['TQOB', 'TQCB', 'TQIR']:
            stocks = 'bonds'

        url = (f"https://iss.moex.com/iss/engines/stock/markets/{stocks}/boards/{id_trading}/securities.json"
               f"?iss.meta=off&iss.only=marketdata&marketdata.columns=SECID,LAST")

        try:
            response = requests.get(url)
        except requests.exceptions.ConnectionError as e:
            raise Exception('Проблема с запросом: ' + url)

        data = json.loads(response.text)['marketdata']['data']
        trading_list.append(data)

    for ticker in tickers:
        for value in trading_list:
            flag = False
            for line in value:
                if ticker == line[0]:

                    if ticker in bond_tickers:
                        last_prices_dict[ticker] = round(line[1] * 10, 2)
                    else:
                        last_prices_dict[ticker] = line[1]
                    flag = True
                    break

            if flag:
                break

    return last_prices_dict


def get_coupon_data_dict(tickers: list):

    bond_ticker_list = []
    coupon_dict = {}
    for id_trading in ['TQOB', 'TQCB', 'TQIR']:
        url = (f"https://iss.moex.com/iss/engines/stock/markets/bonds/boards/{id_trading}/securities.json"
               f"?iss.meta=off&iss.only=securities&securities.columns=SECID,ACCRUEDINT")

        try:
            response = requests.get(url)
        except requests.exceptions.ConnectionError as e:
            raise Exception('Проблема с запросом: ' + url)

        data = json.loads(response.text)['securities']['data']
        len_data = len(data)
        for ticker in tickers:
            for i in range(len_data):
                line = data[i]
                if ticker == line[0]:
                    coupon_dict[ticker] = line[1]
                    bond_ticker_list.append(ticker)

    return coupon_dict, bond_ticker_list


def main():

    # mail_main()
    parser_main()

    portfolio = pd.read_csv('portfolio.csv')
    portfolio['Дата'] = portfolio['Дата'].astype('datetime64[ns]')
    transactions = pd.read_csv('transactions.csv')\
        .drop_duplicates(['Дата заключения', 'Время заключения', 'Статус', 'Номер сделки'])
    transactions['Дата заключения'] = \
        pd.to_datetime(transactions['Дата заключения'] + ' ' + transactions['Время заключения'], dayfirst=True)
    transactions['Дата расчетов'] = pd.to_datetime(transactions['Дата расчетов'], dayfirst=True)
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

    fix_split(ticker_list, transactions, transactions_executed, share_split_dict)
    share_amount_dict, share_price_dict, share_commission_dict = get_stock_data_dict(ticker_list, transactions_executed)
    coupon_dict, bond_ticker_list = get_coupon_data_dict(ticker_list)
    last_prices_dict = get_last_prices_dict(ticker_list, bond_ticker_list)

    portfolio_dict = {
        'Котировки': last_prices_dict,
        'НКД': coupon_dict,
        'Количество': share_amount_dict,
        'Средняя цена': share_price_dict,
        'Комиссия': share_commission_dict
    }

    main_df = pd.DataFrame.from_dict(portfolio_dict)
    main_df.index.name = 'Название'
    main_df[(main_df['Количество'] == 0) | (main_df['Котировки'] == '')] = np.nan
    main_df.dropna(axis=0, subset=['Котировки', 'Количество'], inplace=True)
    main_df['НКД'] = main_df['НКД'].fillna(0)
    main_df[['Котировки', 'НКД']] = main_df[['Котировки', 'НКД']].astype('float64')
    main_df['Количество'] = main_df['Количество'].astype('int64')
    main_df['Средняя цена'] = main_df['Средняя цена']
    main_df['Текущая цена'] = round((main_df['Котировки'] + main_df['НКД']) * main_df['Количество'], 2)
    main_df['P/L, руб.'] = round(main_df['Текущая цена'] - main_df['Средняя цена'] * main_df['Количество'], 2)
    main_df['P/L, %'] = (main_df['Котировки'] * 100 / main_df['Средняя цена'] - 100).round(2)

    main_df.to_csv(path_or_buf='portfolio_main.csv', index_label=False)


if __name__ == '__main__':
    main()
