---
tags:
- entity
- District_CitizenYieldChange
- District
- CitizenYieldChange
- Citizen
- Yield
- Change
---
# District_CitizenYieldChange
## Entity
This file is a description of an Entity's properties. There is no accessible variable of this name, rather, these entities must be retrieved from GameData.District_CitizenYieldChange. Accessing a property should be invoked with a `.`.
## Properties
|	Property	|	Type	|	Collection Of Type?	|	May Be Nil?	|	Default	|	References	|	Key	|	Notes	|
|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	-:	|
|	DistrictType	|	string	|		|		|		|	[[District]].DistrictType	|		|	|
|	YieldType	|	string	|		|		|		|	[[Yield]].YieldType	|		|	|
|	YieldChange	|	number	|		|		|	0	|		|		|	|
|	DistrictReference	|	[[District]]	|		|	✓	|		|		|		|	|
|	YieldReference	|	[[Yield]]	|		|	✓	|		|		|		|	|
