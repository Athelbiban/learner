import xlwt

def extract_strings(file_name):
    with open(file_name, 'r') as input_file:
        book = xlwt.Workbook(encoding="utf-8")
        sheet = book.add_sheet("Sheet 1")
        row_index = 0
        for line in input_file:
            line = line.strip()
            first_part, second_part = line.split(" *")
            second_part, third_part = second_part.split(" _ ")
            third_part = third_part.strip().rsplit('.pdf', 1)[0]
            sheet.write(row_index, 0, first_part)
            sheet.write(row_index, 1, second_part)
            sheet.write(row_index, 2, third_part)
            row_index += 1
        book.save("output.xls")

extract_strings("input.txt")
