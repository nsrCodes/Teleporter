# the script that handles the data 
import json
from datetime import datetime

folder_location = "/home/razor/Downloads/nsr/projects/open_source/my_tool"
def load():
	with open(folder_location+"/data.json") as f:
		data = json.load(f)
	return data

def look_up(name):
	data = load()
	try:
		return data['records'][name]
	except KeyError:
		return False

def add_timestamp():
	data = load()
	data['last_modified'] = str(datetime.now())
	json.dump(data, open(folder_location+"/data.json", "w"), indent = 4)

def add(name,address):
	data = load()
	data['records'][name]=address
	json.dump(data, open(folder_location+"/data.json", "w"), indent = 4)
	add_timestamp()

def approval(cmd):
	while(True):
		ans = input(f'Do you want to proceed to {cmd} this entry (y/n)')
		if ans=='y' or ans=='y':
			return True
		elif ans=='n' or ans=='N':
			return False
		else:
			print("Invalid Argument")

def delete(name,forced=False):
	if (forced if forced==True else approval('delete')):
		data = load()
		removed = data['records'].pop(name,None)
		json.dump(data, open(folder_location+"/data.json", "w"), indent = 4)
		if not forced:
			print("Deleted alias corresponding to location "+removed)
		add_timestamp()

def append(name,address):
	if approval('append'):
		add(name,address)

def last_edited():
	data = load()
	return data['last_modified']