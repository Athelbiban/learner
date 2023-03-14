import os

dir_path = r'c:\Users\VostrovSO\Documents\Востров С.О\УИШЯ.466539.001_Прибор 1Е\PDF\printed'
output_file = 'file_names.txt'

with open(output_file, 'w') as f:
    for file_name in os.listdir(dir_path):
        file_name = file_name[:-4]
        f.write(file_name + '\n')
