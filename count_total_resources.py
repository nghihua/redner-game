import json

total_resources = {'Animal': 0, 
		'Vegetable': 0,
		 'Metal': 0, 
		 'Mineral': 0, 
		 'Wood': 0,
		 'Precious Metal': 0, 
		 'Textile': 0, 
		 'Plastic & Rubber': 0, 
		 'Stone & Glass': 0}

with open('./final_data/recalculated_value.json') as f:
	data = json.load(f)
	for item in data:
		for country in data:
			for section in data[country]:
				total_resources[section] += data[country][section]
				# print(section)
				# print(data[country][section])

print(total_resources)
for x in total_resources:
	total_resources[x] = (100-total_resources[x]//10000)/20
print(total_resources)
total_resources = dict(sorted(total_resources.items(), key=lambda item: item[1], reverse = True))
print(total_resources)