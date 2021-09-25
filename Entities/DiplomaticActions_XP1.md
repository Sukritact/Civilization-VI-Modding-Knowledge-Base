---
tags:
- entity
- DiplomaticActions_XP1
- XP2
- XP1
- DiplomaticActions
- Diplomatic
- Actions
- XP
- 1
---
# DiplomaticActions_XP1
## Entity
This file is a description of an Entity's properties. There is no accessible variable of this name, rather, these entities must be retrieved from GameData.DiplomaticActions_XP1. Accessing a property should be invoked with a `.`.
## Properties
|	Property	|	Type	|	Collection Of Type?	|	May Be Nil?	|	Default	|	References	|	Key	|	Notes	|
|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	-:	|
|	DiplomaticActionType	|	string	|		|		|		|	[[DiplomaticAction]].DiplomaticActionType	|	✓	|	|
|	RequiresGoldenAgeCommemorationType	|	string	|		|	✓	|		|	[[CommemorationType]].CommemorationType	|		|	|
|	AllianceType	|	string	|		|	✓	|		|	[[Alliance]].AllianceType	|		|	|
|	RequiresBrokenPromise	|	boolean	|		|		|	0	|		|		|	|
|	RequiresDifferentLateGovernment	|	boolean	|		|		|	0	|		|		|	|
|	RequiresAllianceSoonToEnd	|	boolean	|		|		|	0	|		|		|	|
|	AllianceReference	|	[[Alliance]]	|		|	✓	|		|		|		|	|
|	RequiresGoldenAgeCommemorationTypeReference	|	[[CommemorationType]]	|		|	✓	|		|		|		|	|