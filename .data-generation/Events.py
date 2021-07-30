import csv
import os

events = {}
eventTypes = set()
eventIndices = {}

i = 0

with open('Civ VI Modding Companion - Events.csv', newline='') as csvfile:
	reader = csv.reader(csvfile, delimiter=',', quotechar='|')
	for row in reader:

		if i < 4:
			i += 1
			continue

		eventName = row[3]
		eventType = "GameEvents" if len(row[10]) > 0 else "Events"

		argumentName = row[4]
		argumentType = row[5][1:]

		try:
			events[eventName]
		except Exception:
			events[eventName] = {'eventType': eventType, 'arguments': []}

		eventTypes.add(eventType)

		if argumentName:
			argumentText = '`' + argumentName
			if argumentType:
				argumentText += ' [' + argumentType + ']'
			argumentText += '`'

			# argument = {'argumentName': argumentName, 'argumentType': argumentType, 'argumentText': argumentText}
			events[eventName]['arguments'].append(argumentText)

for eventType in eventTypes:

	filename = '../EventObjects/' + eventType + '.md'

	os.makedirs(os.path.dirname(filename), exist_ok=True)
	f = open(filename, "w")
	eventIndices[eventType] = f

	f.write('## Static Events\n')
	f.write('Events can be subscribed by using `' + eventType + '.SomeEvent.Add(SomeFunction)`.\n')
	f.write('\n')
	f.write('| Name | Parameters |\n')
	f.write('|:---- |:--------- |\n')

for eventName in events:

	event		= events[eventName]
	eventType	= event['eventType']
	eventIndex	= eventIndices[eventType]

	arguments	= event['arguments']

	# -----------------------
	#  Create Index Entry
	# -----------------------
	indexEntry = '| [[' + eventType + "." + eventName + ']] | '

	if len(arguments) > 0:
		indexEntry += "<br/>".join(arguments)

	indexEntry += ' |\n'
	eventIndex.write(indexEntry)
	# -----------------------
	#  Create Event File
	# -----------------------
	fullName = eventType + '.' + eventName

	filename = '../EventObjects/' + eventType + '/' + eventType + "." + eventName + '.md'
	os.makedirs(os.path.dirname(filename), exist_ok=True)
	f = open(filename, "w")

	f.write('# ' + fullName + "\n")
	f.write('## Description\n')
	f.write('TBD\n')
	f.write('\n')
	f.write('## Usage\n')

	argumentsText = (", ".join(arguments))
	argumentsText = argumentsText.replace('`', '')

	f.write('> `' + fullName + '(' + argumentsText + ')`\n\n')
	f.write('Regular event: you can subscribe to it through `' + fullName + '.Add(<function handler>)`\n')
	f.write('\n')
	f.write('### Parameters\n')

	argumentsList = "\n- ".join(arguments)
	if len(argumentsList) > 0:
		argumentsList = '- ' + argumentsList

	f.write(argumentsList)
