---
tags:
- entity
- AiBuildSpecialization
- Ai
- Build
- Specialization
---
# AiBuildSpecialization
## Entity
This file is a description of an Entity's properties. There is no accessible variable of this name, rather, these entities must be retrieved from GameData.AiBuildSpecialization. Accessing a property should be invoked with a `.`.
## Properties
|	Property	|	Type	|	Collection Of Type?	|	May Be Nil?	|	Default	|	References	|	Key	|	Notes	|
|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	-:	|
|	SpecializationType	|	string	|		|		|		|		|		|	|
|	BuildingYield	|	string	|		|	✓	|		|	[[Yield]].YieldType	|		|	|
|	IncludePopulation	|	boolean	|		|		|	0	|		|		|	|
|	IncludeDefense	|	boolean	|		|		|	0	|		|		|	|
|	IncludeMilitaryUnits	|	boolean	|		|		|	0	|		|		|	|
|	IncludeTradeUnits	|	boolean	|		|		|	0	|		|		|	|
|	PrioritizationYield	|	string	|		|		|		|	[[Yield]].YieldType	|		|	|
|	PriorityOffset	|	number	|		|		|	0	|		|		|	|
|	PriorityReference	|	[[Yield]]	|		|	✓	|		|		|		|	|
|	YieldReference	|	[[Yield]]	|		|	✓	|		|		|		|	|
