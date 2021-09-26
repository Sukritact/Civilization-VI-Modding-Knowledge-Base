---
tags:
- entity
- Resource_TradeRouteYield
- Resource
- TradeRouteYield
- Trade
- Route
- Yield
---
# Resource_TradeRouteYield
## Entity
This file is a description of an Entity's properties. There is no accessible variable of this name, rather, these entities must be retrieved from GameData.Resource_TradeRouteYield. Accessing a property should be invoked with a `.`.
## Properties
|	Property	|	Type	|	Collection Of Type?	|	May Be Nil?	|	Default	|	References	|	Key	|	Notes	|
|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	-:	|
|	ResourceType	|	string	|		|		|		|	[[Resource]].ResourceType	|		|	|
|	YieldType	|	string	|		|		|		|	[[Yield]].YieldType	|		|	|
|	YieldChange	|	number	|		|		|		|		|		|	|
|	YieldReference	|	[[Yield]]	|		|	✓	|		|		|		|	|
