---
tags:
- entity
- Buildings_XP2
- XP2
- Buildings
- XP
- 2
---
# Buildings_XP2
## Entity
This file is a description of an Entity's properties. There is no accessible variable of this name, rather, these entities must be retrieved from GameData.Buildings_XP2. Accessing a property should be invoked with a `.`.
## Properties
|	Property	|	Type	|	Collection Of Type?	|	May Be Nil?	|	Default	|	References	|	Key	|	Notes	|
|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	-:	|
|	BuildingType	|	string	|		|		|		|	[[Building]].BuildingType	|	✓	|	|
|	RequiredPower	|	number	|		|		|	0	|		|		|	|
|	ResourceTypeConvertedToPower	|	string	|		|	✓	|		|	[[Resource]].ResourceType	|		|	|
|	PreventsFloods	|	boolean	|		|		|	0	|		|		|	|
|	PreventsDrought	|	boolean	|		|		|	0	|		|		|	|
|	BlocksCoastalFlooding	|	boolean	|		|		|	0	|		|		|	|
|	CostMultiplierPerTile	|	number	|		|		|	0	|		|		|	|
|	CostMultiplierPerSeaLevel	|	number	|		|		|	0	|		|		|	|
|	Bridge	|	boolean	|		|		|	0	|		|		|	|
|	CanalWonder	|	boolean	|		|		|	0	|		|		|	|
|	EntertainmentBonusWithPower	|	number	|		|		|	0	|		|		|	|
|	NuclearReactor	|	boolean	|		|		|	0	|		|		|	|
|	Pillage	|	boolean	|		|		|	1	|		|		|	|
|	BuildingReference	|	[[Building]]	|		|	✓	|		|		|		|	|
|	ResourceTypeConvertedToPowerReference	|	[[Resource]]	|		|	✓	|		|		|		|	|
