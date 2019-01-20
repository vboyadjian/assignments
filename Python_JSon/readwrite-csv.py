import csv

vegetables = [
 {"name": "eggplant", "color": "purple"},
 {"name": "tomato", "color": "red"},
 {"name": "corn", "color": "yellow"},
 {"name": "okra", "color": "green"},
 {"name": "arugula", "color": "green"},
 {"name": "broccoli", "color": "green"},
]

#open a CSV file
with open('veggies.csv', "w") as f:
	writer = csv.writer(f)
	writer.writerow(['name', 'color'])

#loop through veggies
	for vegetable in vegetables:

		name=vegetable['name']
		color= vegetable['color']

		row= [name,color]

		writer.writerow(row)


