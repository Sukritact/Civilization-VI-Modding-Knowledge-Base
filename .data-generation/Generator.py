from jsmin import jsmin
import json
import os
import yaml

with open('Objects.json') as js_file:
	data = json.load(js_file)

for object_entry in data["Objects"]:

	object_name = object_entry["Name"]
	file_path = "../Objects/" + object_name + ".md"
	path = "../Objects/" + object_name + "/"

	isStatic = object_entry["Type"] == "Static"

	if os.path.isfile(file_path):
		os.rename(file_path, path + object_name + ".md")

	object_path = "../Objects/" + object_name + "/" + object_name + ".md"
	# with open(object_path, 'r') as original: original_object_data = original.read()
	with open(object_path, 'a') as object_file:

		# object_file.write('# ' + object_name + "\n")

		# if isStatic:
		# 	object_file.write('## Object\n')
		# 	object_file.write('This file is a description of an object. This object is accessible as a global variable. Most of its methods do not expect an implicit "self" argument and should be invoked with a `.`\n')
		# else:
		# 	object_file.write('## Instance\n')
		# 	object_file.write('This file is a description of an Instance’s Metatable. There is no accessible variable of this name. Most of its methods will expect an implicit "self" argument and should be invoked with a `:`.\n')

		# object_file.write('\n')
		# object_file.write('## Methods\n')
		# object_file.write('| Script | UI  | Returns | . or : | Name | Arguments |\n')
		# object_file.write('|:------:|:---:| -------:|:---- |:---- |:--------- |\n')

		for method in object_entry["Methods"]:
			# ========================================================
			#  yeah, mixed up script and method
			ui			= "✓" if method["Script"] == 1 else " "
			isUI		= method["Script"] == 1
			script		= "✓" if method["UI"] == 1 else " "
			isScript	= method["UI"] == 1

			returns		= "<code>[[" + method["Returns"] + "]]</code>" if method["Returns"] != "" else " "
			invoke		= ":" if method["Name"].find(':') != -1 else "."
			method_name	= method["Name"].replace(object_name + invoke, "")
			filename	= method["Name"].replace(":",".")
			link		= filename + "\\|" + method_name

			isSetProperty = method_name in ['GetProperty', 'SetProperty']
			# ========================================================
			method_yaml = {}
			method_yaml["tags"]			= ["function", object_name]
			method_yaml["invoke"]		= invoke
			method_yaml["returns"]		= [returns]
			method_yaml["arguments"]	= [""]
			method_yaml["memberOf"]		= object_name
			method_yaml["methodname"]	= method_name
			method_yaml["UI"]			= isUI
			method_yaml["script"]		= isScript

			# object_file.write('|' + ui + '|' + script + '|' + returns + '|' + invoke + '|[[' + link + ']]| |\n')

			with open("../Objects/" + object_name + "/" + filename + ".md", "w", encoding='utf-8') as method_file:

				method_file.write('---\n')
				yaml.dump(method_yaml, method_file)
				method_file.write('---\n')

				method_file.write('# ' + method["Name"] + "\n")
				method_file.write('> this function is a member of [[' + object_name + "]]\n")
				if invoke == ":":
					method_file.write('> this method expects an implicit "self" argument. invoke it with `:`\n')
				else:
					method_file.write('> this method can be invoked with `.`\n')
				method_file.write('-----\n')

				method_file.write('## Usage\n')
				if isSetProperty:
					method_file.write('See [[About Get-SetProperty]]\n')
				else:
					method_file.write('|  UI | Script | Returns | Function | Arguments |\n')
					method_file.write('|:---:|:------:|:-------:|:--------:|:---------:|\n')
					method_file.write('|`=this.UI`')
					method_file.write('|`=this.script`')
					method_file.write('|`=this.returns`')
					method_file.write('|'); method_file.write(method["Name"])
					method_file.write('|`=this.arguments`')
					method_file.write('|\n')