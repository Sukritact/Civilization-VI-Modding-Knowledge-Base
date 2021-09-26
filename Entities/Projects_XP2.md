---
tags:
- entity
- Projects_XP2
- XP2
- Projects
- XP
- 2
---
# Projects_XP2
## Entity
This file is a description of an Entity's properties. There is no accessible variable of this name, rather, these entities must be retrieved from GameData.Projects_XP2. Accessing a property should be invoked with a `.`.
## Properties
|	Property	|	Type	|	Collection Of Type?	|	May Be Nil?	|	Default	|	References	|	Key	|	Notes	|
|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	-:	|
|	ProjectType	|	string	|		|		|		|	[[Project]].ProjectType	|	✓	|	|
|	RequiredPowerWhileActive	|	number	|		|		|	0	|		|		|	|
|	ReligiousPressureModifier	|	number	|		|		|	0	|		|		|	|
|	UnlocksFromEffect	|	boolean	|		|		|	0	|		|		|	|
|	RequiredBuilding	|	string	|		|	✓	|		|	[[Building]].BuildingType	|		|	|
|	CreateBuilding	|	string	|		|	✓	|		|	[[Building]].BuildingType	|		|	|
|	FullyPoweredWhileActive	|	boolean	|		|	✓	|		|		|		|	|
|	MaxSimultaneousInstances	|	number	|		|	✓	|		|		|		|	|
|	BuildingCostCollectionReference	|	[[Project_BuildingCost]]	|	✓	|	✓	|		|		|		|	|
|	CreateBuildingReference	|	[[Building]]	|		|	✓	|		|		|		|	|
|	EmergencyScoreCollectionReference	|	[[EmergencyScoreSource]]	|	✓	|	✓	|		|		|		|	|
|	RequiredBuildingReference	|	[[Building]]	|		|	✓	|		|		|		|	|
