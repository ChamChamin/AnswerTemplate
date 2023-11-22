import csv
import json

file_c = "1forTask2.csv"
file_j = "2forTask2.json"

with open(file_c) as fl:
    lines = [line for line in csv.DictReader(fl)]
    with open(file_j, "w") as fj1:
        fj1.write(json.dumps(lines, indent=4))

with open(file_j, "r") as fj2:
    new_fj2 = json.loads(fj2.read())
    for i in new_fj2:
        print(i)