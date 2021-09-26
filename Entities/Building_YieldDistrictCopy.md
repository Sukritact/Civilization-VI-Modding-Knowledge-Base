---
tags:
- entity
- Building_YieldDistrictCopy
- Building
- YieldDistrictCopy
- Yield
- District
- Copy
---
# Building_YieldDistrictCopy
## Entity
This file is a description of an Entity's properties. There is no accessible variable of this name, rather, these entities must be retrieved from GameData.Building_YieldDistrictCopy. Accessing a property should be invoked with a `.`.
## Properties
|	Property	|	Type	|	Collection Of Type?	|	May Be Nil?	|	Default	|	References	|	Key	|	Notes	|
|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	-:	|
|	BuildingType	|	string	|		|		|		|	[[Building]].BuildingType	|		|	|
|	OldYieldType	|	string	|		|		|	NO_YIELD	|	[[Yield]].YieldType	|		|	|
|	NewYieldType	|	string	|		|		|	NO_YIELD	|	[[Yield]].YieldType	|		|	|
|	BuildingReference	|	[[Building]]	|		|	✓	|		|		|		|	|
|	NewYieldTypeReference	|	[[Yield]]	|		|	✓	|		|		|		|	|
|	OldYieldTypeReference	|	[[Yield]]	|		|	✓	|		|		|		|	|
