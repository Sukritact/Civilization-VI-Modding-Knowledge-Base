---
tags:
- entity
- Policy
---
# Policy
## Entity
This file is a description of an Entity's properties. There is no accessible variable of this name, rather, these entities must be retrieved from GameData.Policy. Accessing a property should be invoked with a `.`.
## Properties
|	Property	|	Type	|	Collection Of Type?	|	May Be Nil?	|	Default	|	References	|	Key	|	Notes	|
|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	-:	|
|	PolicyType	|	string	|		|		|		|	[[Type]].Type	|	✓	|	|
|	Description	|	string	|		|	✓	|		|		|		|	|
|	PrereqCivic	|	string	|		|	✓	|		|	[[Civic]].CivicType	|		|	|
|	PrereqTech	|	string	|		|	✓	|		|	[[Technology]].TechnologyType	|		|	|
|	Name	|	string	|		|		|		|		|		|	|
|	GovernmentSlotType	|	string	|		|		|		|	[[GovernmentSlot]].GovernmentSlotType	|		|	|
|	RequiresGovernmentUnlock	|	boolean	|		|	✓	|		|		|		|	|
|	ExplicitUnlock	|	boolean	|		|		|	0	|		|		|	|
|	PolicyModifiers	|	[[PolicyModifier]]	|	✓	|	✓	|		|		|		|	|
|	PrereqCivicReference	|	[[Civic]]	|		|	✓	|		|		|		|	|
|	PrereqTechReference	|	[[Technology]]	|		|	✓	|		|		|		|	|
|	SlotReference	|	[[GovernmentSlot]]	|		|	✓	|		|		|		|	|
