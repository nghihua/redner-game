import json
import os

for file in os.listdir(directory):
	filename = os.fsdecode(file)
	print(filename)

	with open('./raw_json/{filename}'.format(filename=filename)) as f:
		data = json.load(f)["data"]

	data.sort(reverse = True, key = lambda item: item["Trade Value"])

# write to json file
with open('./{filename}'.format(filename=filename), "w") as f:
	data_json = json.dumps(data, ensure_ascii=False, indent = 2)
	f.write(data_json)