---
tags:
- entity
- Improvement_ValidBuildUnit
- Improvement
- ValidBuildUnit
- Valid
- Build
- Unit
---
# Improvement_ValidBuildUnit
## Entity
This file is a description of an Entity's properties. There is no accessible variable of this name, rather, these entities must be retrieved from GameData.Improvement_ValidBuildUnit. Accessing a property should be invoked with a `.`.
## Properties
|	Property	|	Type	|	Collection Of Type?	|	May Be Nil?	|	Default	|	References	|	Key	|	Notes	|
|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	-:	|
|	ImprovementType	|	string	|		|		|		|	[[Improvement]].ImprovementType	|		|	|
|	UnitType	|	string	|		|		|		|	[[Unit]].UnitType	|		|	|
|	ConsumesCharge	|	boolean	|		|		|	1	|		|		|	|
|	ValidRepairOnly	|	boolean	|		|		|	0	|		|		|	|
|	UnitReference	|	[[Unit]]	|		|	✓	|		|		|		|	|
