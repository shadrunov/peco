import csv
with open("test.csv", encoding="utf-8") as f:
    first_search_dict = list(csv.DictReader(f))
    for i in first_search_dict:
        if i["id"] == name:
            name = i["name"]