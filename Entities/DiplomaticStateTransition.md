---
tags:
- entity
- DiplomaticStateTransition
- Diplomatic
- State
- Transition
---
# DiplomaticStateTransition
## Entity
This file is a description of an Entity's properties. There is no accessible variable of this name, rather, these entities must be retrieved from GameData.DiplomaticStateTransition. Accessing a property should be invoked with a `.`.
## Properties
|	Property	|	Type	|	Collection Of Type?	|	May Be Nil?	|	Default	|	References	|	Key	|	Notes	|
|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	-:	|
|	BaseState	|	string	|		|		|		|	[[DiplomaticState]].StateType	|		|	|
|	TransitionState	|	string	|		|		|		|	[[DiplomaticState]].StateType	|		|	|
|	RequireTransitionMax	|	number	|		|	✓	|		|		|		|	|
|	ThrottleTurns	|	number	|		|		|	0	|		|		|	|
|	AllowTransitionMin	|	number	|		|	✓	|		|		|		|	|
|	RequireTransitionMin	|	number	|		|	✓	|		|		|		|	|
|	AllowTransitionMax	|	number	|		|	✓	|		|		|		|	|
|	AllowTransitionCheck	|	string	|		|	✓	|		|		|		|	|
|	OnTransitionAction	|	string	|		|	✓	|		|		|		|	|
|	BaseStateReference	|	[[DiplomaticState]]	|		|	✓	|		|		|		|	|
|	TransitionStateReference	|	[[DiplomaticState]]	|		|	✓	|		|		|		|	|
