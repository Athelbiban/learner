import os
import platform


def get_directory():

    system = platform.system()

    if system == 'Linux':
        directory = '/home/stas/Загрузки/broker_report/'
    elif system == 'Windows':
        dir1 = 'c:\\Users\\VostrovSO\\Downloads\\broker_report\\'
        dir2 = 'c:\\Users\\stas\\Downloads\\broker_report\\'

        if os.path.isdir(dir1):
            directory = dir1
        elif os.path.isdir(dir2):
            directory = dir2
        else:
            raise Exception('Директория отсутствует')

    else:
        raise Exception('Пока не умею работать с данной ОС: ' + system)

    return directory


if __name__ == '__main__':
    get_directory()