---
tags:
- entity
- Building_ResourceCost
- XP2
- Building
- ResourceCost
- Resource
- Cost
---
# Building_ResourceCost
## Entity
This file is a description of an Entity's properties. There is no accessible variable of this name, rather, these entities must be retrieved from GameData.Building_ResourceCost. Accessing a property should be invoked with a `.`.
## Properties
|	Property	|	Type	|	Collection Of Type?	|	May Be Nil?	|	Default	|	References	|	Key	|	Notes	|
|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	-:	|
|	BuildingType	|	string	|		|		|		|	[[Building]].BuildingType	|		|	|
|	ResourceType	|	string	|		|		|		|	[[Resource]].ResourceType	|		|	|
|	StartProductionCost	|	number	|		|		|		|		|		|	|
|	PerTurnMaintenanceCost	|	number	|		|		|		|		|		|	|
|	BuildingReference	|	[[Building]]	|		|	✓	|		|		|		|	|
|	ResourceReference	|	[[Resource]]	|		|	✓	|		|		|		|	|
