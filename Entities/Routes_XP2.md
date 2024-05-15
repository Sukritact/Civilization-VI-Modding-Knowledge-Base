---
tags:
- entity
- Routes_XP2
- XP2
- Routes
- XP
- 2
---
# Routes_XP2
## Entity
This file is a description of an Entity's properties. There is no accessible variable of this name, rather, these entities must be retrieved from GameData.Routes_XP2. Accessing a property should be invoked with a `.`.
## Properties
|	Property	|	Type	|	Collection Of Type?	|	May Be Nil?	|	Default	|	References	|	Key	|	Notes	|
|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	-:	|
|	RouteType	|	string	|		|		|		|	[[Route]].RouteType	|	✓	|	|
|	BuildOnlyWithUnit	|	boolean	|		|		|	0	|		|		|	|
|	BuildWithUnitChargeCost	|	number	|		|		|		|		|		|	|
|	PrereqTech	|	string	|		|	✓	|		|	[[Technology]].TechnologyType	|		|	|
|	PrereqTechReference	|	[[Technology]]	|		|	✓	|		|		|		|	|
|	RouteReference	|	[[Route]]	|		|	✓	|		|		|		|	|
