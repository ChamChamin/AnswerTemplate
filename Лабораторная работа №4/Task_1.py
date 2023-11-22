import json

summ = 0
file_lif = "forTask1.json"

with open(file_lif) as fl:
    new_fl = json.loads(fl.read())
    for i in new_fl:
        summ += i['score'] * i['weight']

print(round(summ, 3))