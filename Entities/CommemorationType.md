---
tags:
- entity
- CommemorationType
- XP2
- XP1
- Commemoration
- Type
---
# CommemorationType
## Entity
This file is a description of an Entity's properties. There is no accessible variable of this name, rather, these entities must be retrieved from GameData.CommemorationType. Accessing a property should be invoked with a `.`.
## Properties
|	Property	|	Type	|	Collection Of Type?	|	May Be Nil?	|	Default	|	References	|	Key	|	Notes	|
|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	-:	|
|	CommemorationType	|	string	|		|		|		|		|	✓	|	|
|	CategoryDescription	|	[[LocalizedText]]	|		|	✓	|		|		|		|	|
|	GoldenAgeBonusDescription	|	[[LocalizedText]]	|		|	✓	|		|		|		|	|
|	NormalAgeBonusDescription	|	[[LocalizedText]]	|		|	✓	|		|		|		|	|
|	DarkAgeBonusDescription	|	[[LocalizedText]]	|		|	✓	|		|		|		|	|
|	MinimumGameEra	|	string	|		|	✓	|		|	[[Era]].EraType	|		|	|
|	MaximumGameEra	|	string	|		|	✓	|		|	[[Era]].EraType	|		|	|
|	CommemorationCollection	|	[[CommemorationModifier]]	|	✓	|	✓	|		|		|		|	|
|	ComplimentCollection	|	[[ComplimentModifier]]	|	✓	|	✓	|		|		|		|	|
|	MaximumGameEraReference	|	[[Era]]	|		|	✓	|		|		|		|	|
|	MinimumGameEraReference	|	[[Era]]	|		|	✓	|		|		|		|	|
