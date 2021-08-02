import glob
import re
import yaml
import json
import os
# ===========================================================================
# Defines
# ===========================================================================
yamlRegex		= re.compile(r'^\s*(---\s.*?\s*---)\s*', re.S)
usageRegex		= re.compile(r'(## Usage.*?)(\s*($|###*))', re.S)
methodsRegex	= re.compile(r'(## Methods.*?)(\s*($|###*))', re.S)

NamesRegex		= re.compile(r'(\w+)(.(\w+))?.md')

# ----------------------------------------------------------------------
# Process Object Hierarchy
# ----------------------------------------------------------------------
with open('Objects.json', encoding='utf-8') as js_file:
	data = json.load(js_file)

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
# Get Data
# ----------------------------------------------------------------------
def GetObjectData(objectEntry):
	objectName = objectEntry["Name"]
	# ------------------------------
	# Generate the object tag
	objectTag = objectName
	currentName = objectName
	while objects[currentName]['parent']:
		objectTag = objects[currentName]['parent'] + "/" + objectTag
		currentName = objects[currentName]['parent']
	# ------------------------------
	objectPath = "../Objects/" + objectName + "/" + objectName + ".md"
	isStatic = objectEntry["Type"] == "Static"

	objectYaml = {}
	objectYaml["tags"] = []
	objectYaml["tags"].append(objectTag)
	if isStatic: objectYaml["tags"].append("object/static")
	else: objectYaml["tags"].append("object/instance")

	objectData = {
		"name":			objectName,
		"static":		isStatic,
		"yaml":			objectYaml,
		"path":			objectPath,
		"hierarchy":	objectTag
	}

	return objectData

def GetMethodData(method, objectData):
	uiString		= "✓" if method["UI"] == 1 else " "
	isUI			= method["UI"] == 1
	scriptString	= "✓" if method["Script"] == 1 else " "
	isScript		= method["Script"] == 1

	returns, arguments = [], []
	for pair in [(returns, method["Returns"]), (arguments, method["Arguments"])]:
		listNew 	= pair[0]
		_list		= pair[1]

		for val in _list:

			processed = ""

			if val in objects:
				processed = "<code>[[" + val + "]]<code/>"
			else:
				processed = "`" + val + "`"
			listNew.append(processed)

	returnsString = "<br>".join(returns)
	argumentsString = "<br>".join(arguments)

	invoke		= ":" if method["Name"].find(':') != -1 else "."
	method_name	= method["Name"].replace(objectData["name"] + invoke, "")
	filename	= method["Name"].replace(":", ".")
	link		= filename + "\\|" + method_name

	isSetProperty = method_name in ['GetProperty', 'SetProperty']
	# ========================================================
	method_yaml = {}
	method_yaml["tags"] = []
	method_yaml["tags"].append(objectData["hierarchy"] + "/_function")
	if isUI: method_yaml["tags"].append("function/UI")
	if isScript: method_yaml["tags"].append("function/script")

	method_yaml["invoke"]		= invoke
	method_yaml["returns"]		= method["Returns"]
	method_yaml["arguments"]	= method["Arguments"]
	method_yaml["memberOf"]		= objectData["hierarchy"]
	method_yaml["methodname"]	= method_name
	method_yaml["UI"]			= isUI
	method_yaml["script"]		= isScript
	# ========================================================
	methodData = {}
	methodData["uiString"]		= uiString
	methodData["isUI"]			= isUI
	methodData["scriptString"]	= scriptString
	methodData["isScript"]		= isScript

	methodData["returnsString"]	= returnsString
	methodData["argsString"]	= argumentsString

	methodData["invoke"]		= invoke
	methodData["name"]			= method["Name"]
	methodData["methodName"]	= method_name
	methodData["link"]			= link
	methodData["isSetProperty"]	= isSetProperty

	methodData["yaml"]			= method_yaml

	return methodData
# ----------------------------------------------------------------------
# Generate File
# ----------------------------------------------------------------------
def UpdateFile(path, objectData, methodData):

	with open(path, 'r', encoding='utf-8') as file:
		content		= file.read()
		print(path)
		yamlMatch	= yamlRegex.match(content)
		yamlEnd		= yamlMatch.span(1)[1]
		if methodData:
			usageMatch	= usageRegex.search(content)
			dataStart, dataEnd = usageMatch.span(1)
		else:
			methodsMatch = methodsRegex.search(content)
			dataStart, dataEnd = methodsMatch.span(1)

		if not (yamlEnd and dataStart): return

		postYaml	= content[yamlEnd:dataStart]
		postData	= content[dataEnd:]

	with open(path, 'w', encoding='utf-8') as file:

		if methodData:
			file.write('---\n')
			yaml.dump(methodData["yaml"], file)
			file.write('---')
			file.write(postYaml)

			file.write('## Usage\n')
			if methodData["isSetProperty"]:
				file.write('See [[About Get-SetProperty]]\n')
			else:
				file.write('|  UI | Script | Returns | Function | Arguments |\n')
				file.write('|:---:|:------:|-------:|:--------:|:---------|\n')
				file.write('|' + methodData["uiString"])
				file.write('|' + methodData["scriptString"])
				file.write('|' + methodData["returnsString"])
				file.write('|'); file.write(methodData["name"])
				file.write('|' + methodData["argsString"])
				file.write('|')
				file.write(postData)
		else:
			file.write('---\n')
			yaml.dump(objectData["yaml"], file)
			file.write('---')
			file.write(postYaml)
			file.write('## Methods\n')
			file.write('| Script | UI  | Returns | . or : | Name | Arguments |\n')
			file.write('|:------:|:---:| -------:|:---- |:---- |:--------- |')

			for method in objectData["methods"]:
				file.write('\n')
				file.write('|' + method["scriptString"])
				file.write('|' + method["uiString"])
				file.write('|' + method["returnsString"])
				file.write('|' + method["invoke"])
				file.write('|[[' + method["link"] + "]]")
				file.write('|' + method["argsString"])
				file.write('|')
			file.write(postData)

# ===========================================================================
# Utility Functions
# ===========================================================================
filePaths = [f for f in glob.glob("../Objects/**/*.md", recursive=True)]

for objectEntry in data["Objects"]:
	# ----------------------------------------------------------------------
	# Object
	# ----------------------------------------------------------------------
	objectData = GetObjectData(objectEntry)
	objectName = objectData["name"]
	objectPath = "../Objects/" + objectName + "/" + objectName + ".md"

	if os.path.isfile(objectPath):
		pass
	else:
		pass
	# ----------------------------------------------------------------------
	# Methods
	# ----------------------------------------------------------------------
	objectData["methods"] = []

	for method in objectEntry["Methods"]:
		methodData = GetMethodData(method, objectData)
		methodPath = "../Objects/" + objectName + "/" + method["Name"].replace(":", ".") + ".md"

		if not os.path.isfile(methodPath):
			os.makedirs(os.path.dirname(methodPath), exist_ok=True)
			f = open(methodPath, "w", encoding='utf-8')
			f.write('---\n')
			f.write('\n')
			f.write('---\n')
			f.write('# ' + method["Name"] + "\n")
			f.write('> this function is a member of [[' + objectName + "]]\n")
			if methodData["invoke"] == ":":
				f.write('> this method expects an implicit "self" argument. invoke it with `:`\n')
			else:
				f.write('> this method can be invoked with `.`\n')
			f.write('-----\n')
			f.write('## Usage\n')
			f.close()

		UpdateFile(methodPath, objectData, methodData)

		objectData["methods"].append(methodData)
	# ----------------------------------------------------------------------
	# ----------------------------------------------------------------------

	if not os.path.isfile(objectPath):
		os.makedirs(os.path.dirname(objectPath), exist_ok=True)
		f = open(objectPath, "w", encoding='utf-8')
		f.write('---\n')
		f.write('\n')
		f.write('---\n')

		f.write('# ' + objectName + "\n")

		if objectData["static"]:
			f.write('## Object\n')
			f.write('This file is a description of an object. This object is accessible as a global variable. Most of its methods do not expect an implicit "self" argument and should be invoked with a `.`\n')
		else:
			f.write('## Instance\n')
			f.write('This file is a description of an Instance’s Metatable. There is no accessible variable of this name. Most of its methods will expect an implicit "self" argument and should be invoked with a `:`.\n')
		f.write('\n')
		f.write('## Methods\n')
		f.close()

	UpdateFile(objectPath, objectData, False)
