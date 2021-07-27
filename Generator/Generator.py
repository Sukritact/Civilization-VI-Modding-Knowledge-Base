from jsmin import jsmin
import json
import os

with open('Objects.json') as js_file:
	data = json.load(js_file)

directory = '../Methods/'
for entry in os.scandir(directory):

	name = entry.name
	root = name[:name.find(".")]
	path = entry.path
	newpath = path.replace("../Methods", "../Objects/" + root)

	if os.path.isfile(path):
		os.rename(path, newpath)
# for object_entry in data["Objects"]:

# 	object_name = object_entry["Name"]
# 	file_path = "../Objects/" + object_name + ".md"
# 	path = "../Objects/" + object_name + "/"

# 	if os.path.isfile(file_path):
# 		os.rename(file_path, path + object_name + ".md")

	# with open("../Objects/" + object_name + ".md", "w", encoding='utf-8') as object_file:
	# 	object_file.write('# ' + object_name + "\n")
	# 	if object_entry["Type"] == "Static":
	# 		object_file.write('## Object\n')
	# 		object_file.write('This file is a description of an object. This object is accessible as a global variable. Most of its methods do not expect an implicit "self" argument and should be invoked with a `.`\n')
	# 	else:
	# 		object_file.write('## Instance\n')
	# 		object_file.write('This file is a description of an Instance’s Metatable. There is no accessible variable of this name. Most of its methods will expect an implicit "self" argument and should be invoked with a `:`.\n')

	# 	object_file.write('\n')
	# 	object_file.write('## Methods\n')
	# 	object_file.write('| Script | UI  | Returns | . or : | Name | Arguments |\n')
	# 	object_file.write('|:------:|:---:| -------:|:---- |:---- |:--------- |\n')

	# 	for method in object_entry["Methods"]:
	# 		ui			= "✓" if method["Script"] == 1 else " "
	# 		script		= "✓" if method["UI"] == 1 else " "
	# 		returns		= "[[" + method["Returns"] + "]]" if method["Returns"] != "" else " "
	# 		invoke		= ":" if method["Name"].find(':') != -1 else "."
	# 		method_name	= method["Name"].replace(object_name + invoke, "")
	# 		filename	= method["Name"].replace(":",".")
	# 		link		= filename + "\\|" + method_name
	# 		object_file.write('|' + ui + '|' + script + '|' + returns + '|' + invoke + '|[[' + link + ']]| |\n')

	# 		# with open("../Methods/" + filename + ".md", "w", encoding='utf-8') as method_file:
	# 		# 	method_file.write('# ' + method["Name"] + "\n")
	# 		# 	method_file.write('> this function is a member of [[' + object_name + "]]\n")
	# 		# 	if invoke == ":":
	# 		# 		method_file.write('> this method expects an implicit "self" argument. invoke it with `:`\n')
	# 		# 	else:
	# 		# 		method_file.write('> this method can be invoked with `.`\n')
	# 		# 	method_file.write('-----\n')

	# 		# 	method_file.write('## Usage\n')
	# 		# 	method_file.write('> ')
	# 		# 	if method["Returns"] != "":
	# 		# 		method_file.write('**[[' + method["Returns"] + ']]** ')
	# 		# 	method_file.write(method["Name"] + '(')
	# 		# 	method_file.write(')\n')
