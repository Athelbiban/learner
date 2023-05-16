import os
import xlwt


def list_files_to_excel(directory):
    # Создаем новый файл .xls
    workbook = xlwt.Workbook()
    sheet = workbook.add_sheet('Files')

    # Записываем заголовок
    # sheet.write(0, 0, 'File Name')

    # Получаем список файлов в указанной директории
    files = os.listdir(directory)

    # Записываем названия файлов в таблицу
    for i, file_name in enumerate(files):
        first_part, second_part = file_name.split(' _ ')
        sheet.write(i, 0, first_part)
        sheet.write(i, 1, second_part)

    # Сохраняем файл .xls
    workbook.save('file_list.xls')
    print("Файл успешно создан.")


# Указываем директорию, для которой нужно вывести список файлов
directory = 'c:\\Users\\VostrovSO\\Documents\\Востров С.О\\М 203Ю _ Волан1\\М203Ю _ Волан 1 версия 4\\РУ2.179.060 _ Прибор 1ВЛ\\pdf\\'
list_files_to_excel(directory)
