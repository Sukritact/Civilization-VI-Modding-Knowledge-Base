---
tags:
- entity
- GreatPersonClass
- Great
- Person
- Class
---
# GreatPersonClass
## Entity
This file is a description of an Entity's properties. There is no accessible variable of this name, rather, these entities must be retrieved from GameData.GreatPersonClass. Accessing a property should be invoked with a `.`.
## Properties
|	Property	|	Type	|	Collection Of Type?	|	May Be Nil?	|	Default	|	References	|	Key	|	Notes	|
|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	-:	|
|	GreatPersonClassType	|	string	|		|		|		|	[[Type]].Type	|	✓	|	|
|	Name	|	string	|		|		|		|		|		|	|
|	UnitType	|	string	|		|		|		|	[[Unit]].UnitType	|		|	|
|	DistrictType	|	string	|		|		|		|	[[District]].DistrictType	|		|	|
|	MaxPlayerInstances	|	number	|		|	✓	|		|		|		|	|
|	PseudoYieldType	|	string	|		|	✓	|		|	[[PseudoYield]].PseudoYieldType	|		|	|
|	IconString	|	string	|		|		|		|		|		|	|
|	ActionIcon	|	string	|		|		|		|		|		|	|
|	AvailableInTimeline	|	boolean	|		|		|	1	|		|		|	|
|	GenerateDuplicateIndividuals	|	boolean	|		|		|	0	|		|		|	|
|	DistrictReference	|	[[District]]	|		|	✓	|		|		|		|	|
|	ExclusionReference	|	[[ExcludedGreatPersonClass]]	|	✓	|	✓	|		|		|		|	|
|	PseudoYieldReference	|	[[PseudoYield]]	|		|	✓	|		|		|		|	|
|	UnitReference	|	[[Unit]]	|		|	✓	|		|		|		|	|
