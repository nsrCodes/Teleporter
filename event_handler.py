# the script that handles the events, sanitizes the input raises exception and alll
import json_data_handler as records
import os
import pyfiglet 
def list_all():
	print(pyfiglet.figlet_format("Teleport"))
	data = records.load()
	timestamp = records.last_edited()
	if data['records']:
		for record in data['records']:
			print(f'[ENTRY]:	{record}	->	{data["records"][record]}')
		
	else:
		print('There are no records to be displayed')
	print("-------------------------------------------")
	print(f'The records were last edited on : {data["last_modified"]}')


def navigate(args):
	if records.look_up(args.alias):
		address = records.look_up(args.alias)

		if not os.path.isdir(address):
			records.delete(args.alias,forced=True)
			print(" The address that this alias was associated to no longer exists. \n This will now be deleted from your list of aliases")
			return

		if args.terminal:
			try:
				os.system(f'gnome-terminal --working-directory={address} > /dev/null 2>&1')
			except: 
				raise "Could not Open location. Please report this issue on our github"
				
		else:
			os.system(f'xdg-open {address}')
	else:
		print("Invalid alias")


def delete(args):
	if records.look_up(args.alias):
		records.delete(args.alias)
	else:
		print("Location Not Found")


def append(args):
	address = args.location
	if address[0] == '.':
		try:
			address = os.getcwd()+ address[1:]
		except IndexError:
			address = os.getcwd()

	if not os.path.isdir(address):
		print("No such directory")
		return

	if records.look_up(args.alias):
		records.append(name=args.alias,address=address)
		# check if location updates 
	else:
		records.add(name=args.alias,address=address)


# to interpret args
def understand_args(args):

	if args.list:
		# list
		list_all()
	else:
		try:
			if args.which =='navigator':
				navigate(args)

			elif args.which == 'delete':
				delete(args)

			elif args.which == 'add_or_edit':
				append(args)
			else:
				print("something unexpected")
		except AttributeError:
			print(os.system('cat user_guide.md'))