import json

def filter_bridge(filename):
	with open(filename) as f:
		data = json.load(f)

	'''
	for i in data:
		if 'Chancellor' in i['question'] and 'When was' in i['question']:
			print((i['question'], i['answer']))	
	'''
	new_data = []
	for d in data:
		if d['type']=='bridge':
			new_data.append(d)
	
	with open('new-'+filename,'w') as f:
		json.dump(new_data, f) 

filter_bridge("hotpot-dev.json")
filter_bridge("hotpot-train.json")	