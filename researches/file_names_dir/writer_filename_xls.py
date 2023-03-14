import os
import xlwt

dir_path = r'c:\Users\VostrovSO\Documents\Востров С.О\УИШЯ.466539.001_Прибор 1Е\PDF\printed'  # путь к текущей директории
book = xlwt.Workbook(encoding='utf-8')  # создаем новую книгу Excel
sheet = book.add_sheet('Files')  # добавляем лист с названием "Files"
row = 0  # начинаем с первой строки

for filename in os.listdir(dir_path):  # перебираем все файлы в директории
    filename = filename[:-4]
    sheet.write(row, 0, filename)  # записываем имя файла в первый столбец
    row += 1  # переходим на следующую строку

book.save('file_names.xls')  # сохраняем книгу в файл "files.xls"
