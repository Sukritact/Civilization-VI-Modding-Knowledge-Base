from jsmin import jsmin
import json
import os
import yaml

with open('Objects.json') as js_file:
	data = json.load(js_file)
# ----------------------------------------------------------------------
# Process Object Hierarchy
# ----------------------------------------------------------------------
objects = {}
objectTree = {}

for object_entry in data["Objects"]:

	objectName 				= object_entry["Name"]
	objects[objectName]	= {'children': {}, 'parent': False}

for object_entry in data["Objects"]:

	objectName = object_entry["Name"]
	for method in object_entry["Methods"]:

		try:
			childName = method["Returns"][0]
		except IndexError:
			pass
		else:
			if childName:
				if childName.startswith(objectName) and childName in objects:
					objects[childName]['parent'] = objectName
					objects[objectName]['children'][childName] = objects[childName]
# ----------------------------------------------------------------------
# Generate File
# ----------------------------------------------------------------------
for object_entry in data["Objects"]:

	objectName = object_entry["Name"]
	objectTag = objectName

	currentName = objectName
	while objects[currentName]['parent']:
		objectTag = objects[currentName]['parent'] + "/" + objectTag
		currentName = objects[currentName]['parent']

	path = "../Objects/" + objectName + "/" + objectName + ".md"

	isStatic = object_entry["Type"] == "Static"

	# with open(object_path, 'r') as original: original_object_data = original.read()
	with open(path, 'w', encoding='utf-8') as object_file:
		# ----------------------------------------------------------------------
		# Object
		# ----------------------------------------------------------------------
		object_yaml = {}
		object_yaml["tags"] = []
		object_yaml["tags"].append(objectTag)
		if isStatic: object_yaml["tags"].append("object/static")
		else: object_yaml["tags"].append("object/instance")

		object_file.write('---\n')
		yaml.dump(object_yaml, object_file)
		object_file.write('---\n')

		object_file.write('# ' + objectName + "\n")

		if isStatic:
			object_file.write('## Object\n')
			object_file.write('This file is a description of an object. This object is accessible as a global variable. Most of its methods do not expect an implicit "self" argument and should be invoked with a `.`\n')
		else:
			object_file.write('## Instance\n')
			object_file.write('This file is a description of an Instance’s Metatable. There is no accessible variable of this name. Most of its methods will expect an implicit "self" argument and should be invoked with a `:`.\n')

		object_file.write('\n')
		object_file.write('## Methods\n')
		object_file.write('| Script | UI  | Returns | . or : | Name | Arguments |\n')
		object_file.write('|:------:|:---:| -------:|:---- |:---- |:--------- |\n')

		for method in object_entry["Methods"]:
			# ========================================================
			ui			= "✓" if method["UI"] == 1 else " "
			isUI		= method["UI"] == 1
			script		= "✓" if method["Script"] == 1 else " "
			isScript	= method["Script"] == 1

			returns, arguments = [], []
			for pair in [(returns, method["Returns"]), (arguments, method["Arguments"])]:
				listNew 	= pair[0]
				_list		= pair[1]

				for val in _list:

					processed = ""

					if val in objects:
						processed = "<code>[["+val+"]]<code/>"
					else:
						processed = "`"+val+"`"
					listNew.append(processed)

			returnsString = "<br>".join(returns)
			argumentsString = "<br>".join(arguments)

			invoke		= ":" if method["Name"].find(':') != -1 else "."
			method_name	= method["Name"].replace(objectName + invoke, "")
			filename	= method["Name"].replace(":",".")
			link		= filename + "\\|" + method_name

			isSetProperty = method_name in ['GetProperty', 'SetProperty']
			# ========================================================
			method_yaml = {}
			method_yaml["tags"] = []
			method_yaml["tags"].append(objectTag + "/_function")
			if isUI: method_yaml["tags"].append("function/UI")
			if isScript: method_yaml["tags"].append("function/script")

			method_yaml["invoke"]		= invoke
			method_yaml["returns"]		= method["Returns"]
			method_yaml["arguments"]	= method["Arguments"]
			method_yaml["memberOf"]		= currentName
			method_yaml["methodname"]	= method_name
			method_yaml["UI"]			= isUI
			method_yaml["script"]		= isScript
			# ========================================================

			object_file.write('|' + script + '|' + ui + '|' + returnsString + '|' + invoke + '|[[' + link + ']]|' + argumentsString + '|\n')

			with open("../Objects/" + objectName + "/" + filename + ".md", "w", encoding='utf-8') as method_file:

				method_file.write('---\n')
				yaml.dump(method_yaml, method_file)
				method_file.write('---\n')

				method_file.write('# ' + method["Name"] + "\n")
				method_file.write('> this function is a member of [[' + objectName + "]]\n")
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
					method_file.write('|:---:|:------:|-------:|:--------:|:---------|\n')
					method_file.write('|' + ui)
					method_file.write('|' + script)
					method_file.write('|' + returnsString)
					method_file.write('|'); method_file.write(method["Name"])
					method_file.write('|' + argumentsString)
					method_file.write('|\n')