import os

dir_path = r'c:\Users\VostrovSO\Documents\Востров С.О\РУ2.179.065 _ Изделие ЗСПУ-У\pdf'
output_file = 'file_names.txt'

with open(output_file, 'w') as f:
    for file_name in os.listdir(dir_path):
        file_name = file_name[:-4]
        f.write(file_name + '\n')
