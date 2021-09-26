---
tags:
- entity
- Project_YieldConversion
- Project
- YieldConversion
- Yield
- Conversion
---
# Project_YieldConversion
## Entity
This file is a description of an Entity's properties. There is no accessible variable of this name, rather, these entities must be retrieved from GameData.Project_YieldConversion. Accessing a property should be invoked with a `.`.
## Properties
|	Property	|	Type	|	Collection Of Type?	|	May Be Nil?	|	Default	|	References	|	Key	|	Notes	|
|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	-:	|
|	ProjectType	|	string	|		|		|		|	[[Project]].ProjectType	|		|	|
|	YieldType	|	string	|		|		|		|	[[Yield]].YieldType	|		|	|
|	PercentOfProductionRate	|	number	|		|		|	0	|		|		|	|
|	ProjectReference	|	[[Project]]	|		|	✓	|		|		|		|	|
|	YieldReference	|	[[Yield]]	|		|	✓	|		|		|		|	|
