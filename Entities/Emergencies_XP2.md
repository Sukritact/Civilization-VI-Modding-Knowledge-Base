---
tags:
- entity
- Emergencies_XP2
- XP2
- Emergencies
- XP
- 2
---
# Emergencies_XP2
## Entity
This file is a description of an Entity's properties. There is no accessible variable of this name, rather, these entities must be retrieved from GameData.Emergencies_XP2. Accessing a property should be invoked with a `.`.
## Properties
|	Property	|	Type	|	Collection Of Type?	|	May Be Nil?	|	Default	|	References	|	Key	|	Notes	|
|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	-:	|
|	EmergencyType	|	string	|		|	✓	|		|	[[EmergencyAlliance]].EmergencyType	|	✓	|	|
|	Hostile	|	boolean	|		|		|	1	|		|		|	|
|	NoTarget	|	boolean	|		|		|	0	|		|		|	|
|	UIType	|	string	|		|	✓	|		|		|		|	|
|	UIBackgroundPrefix	|	string	|		|	✓	|		|		|		|	|
|	NoCongress	|	boolean	|		|		|	0	|		|		|	|
|	DiscussionCollectionReference	|	[[Discussion]]	|	✓	|	✓	|		|		|		|	|
|	EmergencyReference	|	[[EmergencyAlliance]]	|		|	✓	|		|		|		|	|
|	ScoreSources	|	[[EmergencyScoreSource]]	|	✓	|	✓	|		|		|		|	|
