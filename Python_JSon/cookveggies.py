#read veggies.csv
import csv
import json

with open('veggies.csv', 'r') as f:
    reader = csv.DictReader(f)
    rows = list(reader)


#save "vegetables" as vegetables.json
with open('cookedveggies.json', 'w') as f:
    json.dump(vegetables, f, indent=2)