---
tags:
- entity
- Strategy
---
# Strategy
## Entity
This file is a description of an Entity's properties. There is no accessible variable of this name, rather, these entities must be retrieved from GameData.Strategy. Accessing a property should be invoked with a `.`.
## Properties
|	Property	|	Type	|	Collection Of Type?	|	May Be Nil?	|	Default	|	References	|	Key	|	Notes	|
|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	-:	|
|	StrategyType	|	string	|		|		|		|		|	✓	|	|
|	VictoryType	|	string	|		|	✓	|		|	[[Victory]].VictoryType	|		|	|
|	NumConditionsNeeded	|	number	|		|		|	1	|		|		|	|
|	ConditionCollection	|	[[StrategyCondition]]	|	✓	|	✓	|		|		|		|	|
|	PriorityCollection	|	[[Strategy_Priority]]	|	✓	|	✓	|		|		|		|	|
|	VictoryReference	|	[[Victory]]	|		|	✓	|		|		|		|	|
|	YieldCollection	|	[[Strategy_YieldPriority]]	|	✓	|	✓	|		|		|		|	|
