import csv

def extract_strings(file_name):
    with open(file_name, 'r') as input_file, open("output.csv", 'w', newline='') as output_file:
        writer = csv.writer(output_file, delimiter='\t')
        for line in input_file:
            line = line.strip()
            first_part, second_part = line.split(" *")
            second_part, third_part = second_part.split(" _ ")
            third_part = third_part.strip().rsplit('.pdf', 1)[0]
            writer.writerow([first_part, second_part, third_part])

extract_strings("input.txt")
