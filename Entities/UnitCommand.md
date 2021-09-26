---
tags:
- entity
- UnitCommand
- Unit
- Command
---
# UnitCommand
## Entity
This file is a description of an Entity's properties. There is no accessible variable of this name, rather, these entities must be retrieved from GameData.UnitCommand. Accessing a property should be invoked with a `.`.
## Properties
|	Property	|	Type	|	Collection Of Type?	|	May Be Nil?	|	Default	|	References	|	Key	|	Notes	|
|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	-:	|
|	CommandType	|	string	|		|		|		|		|	✓	|	|
|	Description	|	string	|		|		|		|		|		|	|
|	Help	|	string	|		|	✓	|		|		|		|	|
|	DisabledHelp	|	string	|		|	✓	|		|		|		|	|
|	Icon	|	string	|		|		|		|		|		|	|
|	Sound	|	string	|		|	✓	|		|		|		|	|
|	VisibleInUI	|	boolean	|		|		|		|		|		|	|
|	HoldCycling	|	boolean	|		|		|	0	|		|		|	|
|	CategoryInUI	|	string	|		|	✓	|		|		|		|	|
|	InterfaceMode	|	string	|		|	✓	|		|		|		|	|
|	PrereqTech	|	string	|		|	✓	|		|	[[Technology]].TechnologyType	|		|	|
|	PrereqCivic	|	string	|		|	✓	|		|	[[Civic]].CivicType	|		|	|
|	MaxEra	|	number	|		|		|	-1	|		|		|	|
|	HotkeyId	|	string	|		|	✓	|		|		|		|	|
|	PrereqCivicReference	|	[[Civic]]	|		|	✓	|		|		|		|	|
|	PrereqTechReference	|	[[Technology]]	|		|	✓	|		|		|		|	|
