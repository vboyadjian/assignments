from pprint import pprint
import csv
import json
#read CSV
with open('testwrite.csv', 'r') as f:
    reader = csv.DictReader(f)
    vegetables = list(reader)

pprint(vegetables)
#group by color

vegetables_by_color = {}
for veg in vegetables:
    color = veg['color']
    if color in vegetables_by_color:
        vegetables_by_color[color].append(veg)
    else:
        vegetables_by_color[color] = [veg]

pprint(vegetables_by_color)

#output to JSON file
with open('vegetables_by_color.json', 'w') as f:
    json.dump(vegetables_by_color, f, indent = 2)