import json
# ----------------------------------------------------------------------
# Process Object Hierarchy
# ----------------------------------------------------------------------
with open('Objects.json', "r", encoding='utf-8') as js_file:
	data = json.load(js_file)

objects = {}
objectTree = {}

for object_entry in data["Objects"]:

	objectName 				= object_entry["Name"]
	objects[objectName]	= {'children': {}, 'parent': False, "static": (object_entry["Type"] == "Static")}

for object_entry in data["Objects"]:

	objectName = object_entry["Name"]
	for method in object_entry["Methods"]:

		try:
			childName = method["Returns"][0]
		except IndexError:
			pass
		else:
			if childName:
				# if childName.startswith(objectName) and childName in objects:
				if childName in objects:
					if objects[childName]['parent'] != False:
						objects[childName]['parent'] = 0
					else:
						objects[childName]['parent'] = objectName
					objects[objectName]['children'][childName] = objects[childName]

sortedobjects = sorted(objects.keys(), key=lambda x:x.lower())

def DumpChildren(objectName, indent):

	object_entry = objects[objectName]
	if indent != "" and not object_entry['parent']:
		return

	print(indent + "- [[" + objectName + "]]")

	indent = indent + "\t"

	children = sorted(object_entry['children'].keys(), key=lambda x:x.lower())
	for child in children:
		DumpChildren(child, indent)

for objectName in sortedobjects:
	object_entry = objects[objectName]

	if not object_entry["static"]:
		if not object_entry["parent"]:
			DumpChildren(objectName, "")

print("   ")

for objectName in sortedobjects:
	object_entry = objects[objectName]

	if object_entry["static"]:
		if not object_entry["parent"]:
			DumpChildren(objectName, "")