---
tags:
- entity
- UnitUpgrade
- Unit
- Upgrade
---
# UnitUpgrade
## Entity
This file is a description of an Entity's properties. There is no accessible variable of this name, rather, these entities must be retrieved from GameData.UnitUpgrade. Accessing a property should be invoked with a `.`.
## Properties
|	Property	|	Type	|	Collection Of Type?	|	May Be Nil?	|	Default	|	References	|	Key	|	Notes	|
|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	-:	|
|	Unit	|	string	|		|		|		|	[[Unit]].UnitType	|	✓	|	|
|	UpgradeUnit	|	string	|		|		|		|	[[Unit]].UnitType	|		|	|
|	UnitReference	|	[[Unit]]	|		|	✓	|		|		|		|	|
|	UpgradeUnitReference	|	[[Unit]]	|		|	✓	|		|		|		|	|
