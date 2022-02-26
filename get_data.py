import csv

with open("phones.csv",'r', encoding='utf-8',) as file:
    list_dict =[]

    reader_dict = csv.DictReader(file, delimiter=";")
    for row in reader_dict:
        list_dict.append(row)

print(list_dict)