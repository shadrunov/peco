import csv
with open("test_text.csv", encoding="utf-8") as f_text:
    read = csv.reader(f_text)
    for i in read:
        print(i)
        if i[0] ==