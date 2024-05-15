---
tags:
- entity
- Strategy_YieldPriority
- Strategy
- YieldPriority
- Yield
- Priority
---
# Strategy_YieldPriority
## Entity
This file is a description of an Entity's properties. There is no accessible variable of this name, rather, these entities must be retrieved from GameData.Strategy_YieldPriority. Accessing a property should be invoked with a `.`.
## Properties
|	Property	|	Type	|	Collection Of Type?	|	May Be Nil?	|	Default	|	References	|	Key	|	Notes	|
|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	-:	|
|	StrategyType	|	string	|		|	✓	|		|	[[Strategy]].StrategyType	|		|	|
|	YieldType	|	string	|		|	✓	|		|	[[Yield]].YieldType	|		|	|
|	PseudoYieldType	|	string	|		|	✓	|		|	[[PseudoYield]].PseudoYieldType	|		|	|
|	PercentageDelta	|	number	|		|		|	0	|		|		|	|
|	PseudoYieldReference	|	[[PseudoYield]]	|		|	✓	|		|		|		|	|
|	YieldReference	|	[[Yield]]	|		|	✓	|		|		|		|	|
