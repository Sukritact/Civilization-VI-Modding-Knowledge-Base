---
tags:
- entity
- DiplomaticTriggeredTransition
- Diplomatic
- Triggered
- Transition
---
# DiplomaticTriggeredTransition
## Entity
This file is a description of an Entity's properties. There is no accessible variable of this name, rather, these entities must be retrieved from GameData.DiplomaticTriggeredTransition. Accessing a property should be invoked with a `.`.
## Properties
|	Property	|	Type	|	Collection Of Type?	|	May Be Nil?	|	Default	|	References	|	Key	|	Notes	|
|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	-:	|
|	TriggerType	|	string	|		|		|		|	[[DiplomaticTrigger]].TriggerType	|		|	|
|	CivilizationLevel	|	string	|		|		|		|	[[CivilizationLevel]].CivilizationLevelType	|		|	|
|	OpponentCivilizationLevel	|	string	|		|		|		|	[[CivilizationLevel]].CivilizationLevelType	|		|	|
|	TransitionState	|	string	|		|		|		|	[[DiplomaticState]].StateType	|		|	|
|	CivLevelReference	|	[[CivilizationLevel]]	|		|	✓	|		|		|		|	|
|	OpponentCivLevelReference	|	[[CivilizationLevel]]	|		|	✓	|		|		|		|	|
|	TransitionStateReference	|	[[DiplomaticState]]	|		|	✓	|		|		|		|	|
|	TriggerReference	|	[[DiplomaticTrigger]]	|		|	✓	|		|		|		|	|
