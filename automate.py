import json
import locale
import os

locale.setlocale(locale.LC_ALL, 'vi_VN')

sections = ['Animal Products', 'Vegetable Products',
		 'Metals', 'Mineral Products', 'Wood Products',
		 'Precious Metals', 'Textiles', 
		 'Plastics and Rubbers', 'Stone And Glass']

advanced_sections = ['Machines', 'Weapons', 'Footwear and Headwear',
					'Instruments', 'Transportation', 'Chemical Products'
					'Foodstuffs', 'Paper Goods', 'Miscellaneous',
					'Arts and Antiques']

old_to_new_sections = {
	"Animal Products": "Animal",
    "Vegetable Products": "Vegetable",
    "Metals": "Metal",
    "Mineral Products": "Mineral",
    "Wood Products": "Wood",
    "Precious Metals": "Precious Metals",
    "Textiles": "Textiles",
    "Plastics and Rubbers": "Plastics & Rubbers",
    "Stone And Glass": "Stone & Glass"
}

natural_resources = {}

def recalculate(value):
	return round((value/100000000)/10)*10

def get_new_section_name(section):
	return old_to_new_sections[section]

for file in os.listdir("./json"):
	filename = os.fsdecode(file)

	with open('./json/{filename}'.format(filename=filename)) as f:
		data = json.load(f)

	temp_dict = {}

	for section in sections:
		new_section = get_new_section_name(section)
		temp_dict[new_section] = 0
		for item in data:
			if (item["Section"] == section):
				temp_dict[new_section] += item["Trade Value"]
		temp_dict[new_section] = recalculate(temp_dict[new_section])
		if (temp_dict[new_section]==0):
			del temp_dict[new_section]

	natural_resources[os.path.splitext(filename)[0]] = temp_dict

filename = input("Enter name:\n")

# write to json file
with open('./{filename}'.format(filename=filename), "w") as f:
	natural_resources_json = json.dumps(natural_resources, ensure_ascii=False, indent = 2)
	f.write(natural_resources_json)