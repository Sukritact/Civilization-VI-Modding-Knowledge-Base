---
tags:
- entity
- StrategyCondition
- Strategy
- Condition
---
# StrategyCondition
## Entity
This file is a description of an Entity's properties. There is no accessible variable of this name, rather, these entities must be retrieved from GameData.StrategyCondition. Accessing a property should be invoked with a `.`.
## Properties
|	Property	|	Type	|	Collection Of Type?	|	May Be Nil?	|	Default	|	References	|	Key	|	Notes	|
|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	-:	|
|	StrategyType	|	string	|		|	✓	|		|	[[Strategy]].StrategyType	|		|	|
|	ConditionFunction	|	string	|		|	✓	|		|		|		|	|
|	StringValue	|	string	|		|	✓	|		|		|		|	|
|	ThresholdValue	|	number	|		|		|	0	|		|		|	|
|	Forbidden	|	boolean	|		|		|	0	|		|		|	|
|	Disqualifier	|	boolean	|		|		|	0	|		|		|	|
|	Exclusive	|	boolean	|		|		|	0	|		|		|	|
|	StrategyReference	|	[[Strategy]]	|		|	✓	|		|		|		|	|
