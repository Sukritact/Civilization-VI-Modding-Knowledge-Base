---
tags:
- entity
- DiplomaticState
- Diplomatic
- State
---
# DiplomaticState
## Entity
This file is a description of an Entity's properties. There is no accessible variable of this name, rather, these entities must be retrieved from GameData.DiplomaticState. Accessing a property should be invoked with a `.`.
## Properties
|	Property	|	Type	|	Collection Of Type?	|	May Be Nil?	|	Default	|	References	|	Key	|	Notes	|
|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	-:	|
|	StateType	|	string	|		|		|		|		|		|	|
|	Name	|	string	|		|		|		|		|		|	|
|	DiplomaticYieldBonus	|	number	|		|		|	0	|		|		|	|
|	RelationshipLevel	|	number	|		|		|	0	|		|		|	|
|	TransitionActionCollection	|	[[DiplomaticStateAction]]	|	✓	|	✓	|		|		|		|	|
|	TransitionsOut	|	[[DiplomaticStateTransition]]	|	✓	|	✓	|		|		|		|	|
|	ValidActions	|	[[DiplomaticStateAction]]	|	✓	|	✓	|		|		|		|	|
