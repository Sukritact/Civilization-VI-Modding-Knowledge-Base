---
tags:
- entity
- DiplomaticStateAction
- Diplomatic
- State
- Action
---
# DiplomaticStateAction
## Entity
This file is a description of an Entity's properties. There is no accessible variable of this name, rather, these entities must be retrieved from GameData.DiplomaticStateAction. Accessing a property should be invoked with a `.`.
## Properties
|	Property	|	Type	|	Collection Of Type?	|	May Be Nil?	|	Default	|	References	|	Key	|	Notes	|
|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	-:	|
|	StateType	|	number	|		|		|		|	[[DiplomaticState]].StateType	|		|	|
|	DiplomaticActionType	|	number	|		|		|		|	[[DiplomaticAction]].DiplomaticActionType	|		|	|
|	AiAllowed	|	boolean	|		|		|	1	|		|		|	|
|	Worth	|	number	|		|		|	0	|		|		|	|
|	Cost	|	number	|		|		|	0	|		|		|	|
|	TransitionToState	|	string	|		|	✓	|		|	[[DiplomaticState]].StateType	|		|	|
|	TeamOnly	|	boolean	|		|		|	0	|		|		|	|
|	DiplomaticActionReference	|	[[DiplomaticAction]]	|		|	✓	|		|		|		|	|
|	TransitionStateReference	|	[[DiplomaticState]]	|		|	✓	|		|		|		|	|
