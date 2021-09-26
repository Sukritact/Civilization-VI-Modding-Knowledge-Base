---
tags:
- entity
- BoostHandler
- Boost
- Handler
---
# BoostHandler
## Entity
This file is a description of an Entity's properties. There is no accessible variable of this name, rather, these entities must be retrieved from GameData.BoostHandler. Accessing a property should be invoked with a `.`.
## Properties
|	Property	|	Type	|	Collection Of Type?	|	May Be Nil?	|	Default	|	References	|	Key	|	Notes	|
|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	-:	|
|	HandlerId	|	string	|		|	✓	|		|		|	✓	|	|
|	TechBoostType	|	string	|		|		|		|	[[BoostName]].BoostType	|		|	|
|	BehaviorTree	|	string	|		|	✓	|		|	[[BehaviorTree]].TreeName	|		|	|
|	OperationName	|	string	|		|	✓	|		|	[[AiOperationDef]].OperationName	|		|	|
|	LuaScript	|	string	|		|	✓	|		|		|		|	|
|	UniquenessTag	|	string	|		|	✓	|		|		|		|	|
|	WinnowFunction	|	string	|		|	✓	|		|		|		|	|
|	BoostTypeReference	|	[[BoostName]]	|		|	✓	|		|		|		|	|
