import csv
input_file = "data.csv"

with open(input_file, 'r', newline='') as infile:
    reader = csv.DictReader(infile)
    fieldnames = reader.fieldnames
    
    for row in reader:
        print(row)