---
tags:
- entity
- BarbarianTribe_UnitCondition
- BarbarianTribe
- UnitCondition
- Barbarian
- Tribe
- Unit
- Condition
---
# BarbarianTribe_UnitCondition
## Entity
This file is a description of an Entity's properties. There is no accessible variable of this name, rather, these entities must be retrieved from GameData.BarbarianTribe_UnitCondition. Accessing a property should be invoked with a `.`.
## Properties
|	Property	|	Type	|	Collection Of Type?	|	May Be Nil?	|	Default	|	References	|	Key	|	Notes	|
|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	-:	|
|	TribeType	|	string	|		|		|		|	[[BarbarianTribe]].TribeType	|		|	|
|	UnitType	|	string	|		|		|		|	[[Unit]].UnitType	|		|	|
|	ReplacesUnitType	|	string	|		|	✓	|		|	[[Unit]].UnitType	|		|	|
|	MaxPerTribe	|	number	|		|		|	1	|		|		|	|
