---
tags:
- entity
- District_TradeRouteYield
- District
- TradeRouteYield
- Trade
- Route
- Yield
---
# District_TradeRouteYield
## Entity
This file is a description of an Entity's properties. There is no accessible variable of this name, rather, these entities must be retrieved from GameData.District_TradeRouteYield. Accessing a property should be invoked with a `.`.
## Properties
|	Property	|	Type	|	Collection Of Type?	|	May Be Nil?	|	Default	|	References	|	Key	|	Notes	|
|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	-:	|
|	DistrictType	|	string	|		|		|		|	[[District]].DistrictType	|		|	|
|	YieldType	|	string	|		|		|		|	[[Yield]].YieldType	|		|	|
|	YieldChangeAsOrigin	|	number	|		|		|	0	|		|		|	|
|	YieldChangeAsDomesticDestination	|	number	|		|		|	0	|		|		|	|
|	YieldChangeAsInternationalDestination	|	number	|		|		|	0	|		|		|	|
|	DistrictReference	|	[[District]]	|		|	✓	|		|		|		|	|
|	YieldReference	|	[[Yield]]	|		|	✓	|		|		|		|	|
