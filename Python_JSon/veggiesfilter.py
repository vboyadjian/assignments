from pprint import pprint
import csv

with open('testwrite.csv', 'r') as f:
	reader = csv.DictReader(f)
	vegetables = list(reader)



# filter whitelist by colors
green_veggies = []
whitelist = ["green"]
for vegetable in vegetables:
	if vegetable['color'] in whitelist:
		green_veggies.append(vegetable)



		pprint(green_veggies)

