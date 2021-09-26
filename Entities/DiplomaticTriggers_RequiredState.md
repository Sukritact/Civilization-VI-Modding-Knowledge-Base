---
tags:
- entity
- DiplomaticTriggers_RequiredState
- DiplomaticTriggers
- RequiredState
- Diplomatic
- Triggers
- Required
- State
---
# DiplomaticTriggers_RequiredState
## Entity
This file is a description of an Entity's properties. There is no accessible variable of this name, rather, these entities must be retrieved from GameData.DiplomaticTriggers_RequiredState. Accessing a property should be invoked with a `.`.
## Properties
|	Property	|	Type	|	Collection Of Type?	|	May Be Nil?	|	Default	|	References	|	Key	|	Notes	|
|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	-:	|
|	TriggerType	|	string	|		|		|		|	[[DiplomaticTrigger]].TriggerType	|		|	|
|	RequiredState	|	string	|		|		|		|	[[DiplomaticState]].StateType	|		|	|
|	StateReference	|	[[DiplomaticState]]	|		|	✓	|		|		|		|	|
