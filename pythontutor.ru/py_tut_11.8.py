"""
Задача «Англо-латинский словарь»
Условие
Однажды, разбирая старые книги на чердаке, школьник Вася нашёл англо-латинский словарь. Английский он к тому
времени знал в совершенстве, и его мечтой было изучить латынь. Поэтому попавшийся словарь был как раз кстати.

К сожалению, для полноценного изучения языка недостаточно только одного словаря: кроме англо-латинского
необходим латинско-английский. За неимением лучшего он решил сделать второй словарь из первого.

Как известно, словарь состоит из переводимых слов, к каждому из которых приводится несколько слов-переводов. Для
каждого латинского слова, встречающегося где-либо в словаре, Вася предлагает найти все его переводы (то есть все
английские слова, для которых наше латинское встречалось в его списке переводов), и считать их и только их
переводами этого латинского слова.

Помогите Васе выполнить работу по созданию латинско-английского словаря из англо-латинского.

В первой строке содержится единственное целое число N — количество английских слов в словаре. Далее следует N
описаний. Каждое описание содержится в отдельной строке, в которой записано сначала английское слово, затем
отделённый пробелами дефис, затем разделённые запятыми с пробелами переводы этого английского слова на
латинский. Все слова состоят только из маленьких латинских букв. Переводы отсортированы в лексикографическом
порядке. Порядок следования английских слов в словаре также лексикографический.

Выведите соответствующий данному латинско-английский словарь, в точности соблюдая формат входных данных.
В частности, первым должен идти перевод лексикографически минимального латинского слова, далее — второго в этом
порядке и т.д. Внутри перевода английские слова должны быть также отсортированы лексикографически.
"""


dict_list = []

for i in range(int(input())):
    eng, lat_str = input().split(' - ')
    lat_list = lat_str.split(', ')
    for lat in lat_list:
        dict_list.append([lat, eng])

dict_list_sort = sorted(dict_list)

for i in range(len(dict_list_sort)):
    list_temp = []
    for e in range(i + 1, len(dict_list_sort)):
        if dict_list_sort[i][0] == dict_list_sort[e][0]:
            dict_list_sort[i].append(dict_list_sort[e][1])
            list_temp += [e]
        else:
            break
    if len(list_temp) > 0:
        del dict_list_sort[list_temp[0]:list_temp[-1] + 1]

print(len(dict_list_sort))
for i in dict_list_sort:
    print("{} - {}".format(i[0], ', '.join(i[1:])))
