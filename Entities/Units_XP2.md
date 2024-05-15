---
tags:
- entity
- Units_XP2
- XP2
- Units
- XP
- 2
---
# Units_XP2
## Entity
This file is a description of an Entity's properties. There is no accessible variable of this name, rather, these entities must be retrieved from GameData.Units_XP2. Accessing a property should be invoked with a `.`.
## Properties
|	Property	|	Type	|	Collection Of Type?	|	May Be Nil?	|	Default	|	References	|	Key	|	Notes	|
|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	-:	|
|	UnitType	|	string	|		|		|		|	[[Unit]].UnitType	|	✓	|	|
|	ResourceMaintenanceAmount	|	number	|		|		|	0	|		|		|	|
|	ResourceCost	|	number	|		|		|	0	|		|		|	|
|	ResourceMaintenanceType	|	string	|		|	✓	|		|	[[Resource]].ResourceType	|		|	|
|	TourismBomb	|	number	|		|		|	0	|		|		|	|
|	CanEarnExperience	|	boolean	|		|		|	1	|		|		|	|
|	TourismBombPossible	|	boolean	|		|		|	0	|		|		|	|
|	CanFormMilitaryFormation	|	boolean	|		|		|	1	|		|		|	|
|	MajorCivOnly	|	boolean	|		|		|	0	|		|		|	|
|	CanCauseDisasters	|	boolean	|		|		|	0	|		|		|	|
|	CanSacrificeUnits	|	boolean	|		|		|	0	|		|		|	|
|	ResourceReference	|	[[Resource]]	|		|	✓	|		|		|		|	|
