import json
import locale
import os

locale.setlocale(locale.LC_ALL, 'vi_VN')

resources = ["Corn", "Soybeans", "Wheat", "Barley", "Ground Nuts", "Apples and Pears", "Citrus"
			"Gold", "Crude Petroleum", "Raw Aluminium", "Silver", "Precious Metal Ore"
			"Crustaceans", "Poultry Meat", "Cheese", "Non-fillet Frozen Fish"
			"Raw Tobacco" ]

directory = os.fsencode("json")

sections = ['Animal Products', 'Vegetable Products',
		 'Metals', 'Mineral Products', 'Wood Products',
		 'Precious Metals', 'Textiles', 
		 'Plastics and Rubbers', 'Stone And Glass']

advanced_sections = ['Machines', 'Weapons', 'Footwear and Headwear',
					'Instruments', 'Transportation', 'Chemical Products'
					'Foodstuffs', 'Paper Goods', 'Miscellaneous',
					'Arts and Antiques']

natural_resources = {}

def recalculate(value):
	return round((value/100000000)/10)*10
    
for file in os.listdir(directory):
	filename = os.fsdecode(file)

	with open('./json/{filename}'.format(filename=filename)) as f:
		data = json.load(f)

	temp_dict = {}

	for section in sections:
		temp_dict[section] = 0
		for item in data:
			if (item["Section"] == section):
				temp_dict[section] += item["Trade Value"]
		temp_dict[section] = recalculate(temp_dict[section])
		if (temp_dict[section]==0):
			del temp_dict[section]

	natural_resources[os.path.splitext(filename)[0]] = temp_dict

filename = input("Enter name:\n")

# write to json file
with open('./{filename}'.format(filename=filename), "w") as f:
	natural_resources_json = json.dumps(natural_resources, ensure_ascii=False, indent = 2)
	f.write(natural_resources_json)