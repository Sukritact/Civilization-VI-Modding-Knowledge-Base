---
tags:
- entity
- GovernorReplace
- XP2
- XP1
- Governor
- Replace
---
# GovernorReplace
## Entity
This file is a description of an Entity's properties. There is no accessible variable of this name, rather, these entities must be retrieved from GameData.GovernorReplace. Accessing a property should be invoked with a `.`.
## Properties
|	Property	|	Type	|	Collection Of Type?	|	May Be Nil?	|	Default	|	References	|	Key	|	Notes	|
|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	-:	|
|	UniqueGovernorType	|	string	|		|		|		|	[[Governor]].GovernorType	|		|	|
|	ReplacesGovernorType	|	string	|		|		|		|	[[Governor]].GovernorType	|		|	|
|	BaseGovernorReference	|	[[Governor]]	|		|	✓	|		|		|		|	|
|	ReplacementGovernorReference	|	[[Governor]]	|		|	✓	|		|		|		|	|
