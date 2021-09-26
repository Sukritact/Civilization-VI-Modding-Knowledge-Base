---
tags:
- entity
- Resource_Consumption
- XP2
- Resource
- Consumption
---
# Resource_Consumption
## Entity
This file is a description of an Entity's properties. There is no accessible variable of this name, rather, these entities must be retrieved from GameData.Resource_Consumption. Accessing a property should be invoked with a `.`.
## Properties
|	Property	|	Type	|	Collection Of Type?	|	May Be Nil?	|	Default	|	References	|	Key	|	Notes	|
|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	-:	|
|	ResourceType	|	string	|		|		|		|	[[Resource]].ResourceType	|	✓	|	|
|	Accumulate	|	boolean	|		|		|	0	|		|		|	|
|	PowerProvided	|	number	|		|		|	0	|		|		|	|
|	CO2perkWh	|	number	|		|		|	0	|		|		|	|
|	BaseExtractionRate	|	number	|		|		|	0	|		|		|	|
|	ImprovedExtractionRate	|	number	|		|		|	0	|		|		|	|
|	ObsoleteTech	|	string	|		|	✓	|		|	[[Technology]].TechnologyType	|		|	|
|	StockpileCap	|	number	|		|		|	0	|		|		|	|
|	ResourceReference	|	[[Resource]]	|		|	✓	|		|		|		|	|
|	TechnologyReference	|	[[Technology]]	|		|	✓	|		|		|		|	|
