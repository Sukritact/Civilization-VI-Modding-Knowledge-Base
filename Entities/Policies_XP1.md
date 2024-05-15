---
tags:
- entity
- Policies_XP1
- XP2
- XP1
- Policies
- XP
- 1
---
# Policies_XP1
## Entity
This file is a description of an Entity's properties. There is no accessible variable of this name, rather, these entities must be retrieved from GameData.Policies_XP1. Accessing a property should be invoked with a `.`.
## Properties
|	Property	|	Type	|	Collection Of Type?	|	May Be Nil?	|	Default	|	References	|	Key	|	Notes	|
|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	-:	|
|	PolicyType	|	string	|		|		|		|		|	✓	|	|
|	MinimumGameEra	|	string	|		|	✓	|		|	[[Era]].EraType	|		|	|
|	MaximumGameEra	|	string	|		|	✓	|		|	[[Era]].EraType	|		|	|
|	RequiresDarkAge	|	boolean	|		|		|	0	|		|		|	|
|	RequiresGoldenAge	|	boolean	|		|		|	0	|		|		|	|
|	MaximumGameEraReference	|	[[Era]]	|		|	✓	|		|		|		|	|
|	MinimumGameEraReference	|	[[Era]]	|		|	✓	|		|		|		|	|
