---
tags:
- entity
- UnitPromotion
- Unit
- Promotion
---
# UnitPromotion
## Entity
This file is a description of an Entity's properties. There is no accessible variable of this name, rather, these entities must be retrieved from GameData.UnitPromotion. Accessing a property should be invoked with a `.`.
## Properties
|	Property	|	Type	|	Collection Of Type?	|	May Be Nil?	|	Default	|	References	|	Key	|	Notes	|
|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	-:	|
|	UnitPromotionType	|	string	|		|		|		|	[[Type]].Type	|	✓	|	|
|	Name	|	[[LocalizedText]]	|		|		|		|		|		|	|
|	Description	|	[[LocalizedText]]	|		|		|		|		|		|	|
|	Level	|	number	|		|		|		|		|		|	|
|	Specialization	|	string	|		|	✓	|		|		|		|	|
|	PromotionClass	|	string	|		|	✓	|		|	[[UnitPromotionClass]].PromotionClassType	|		|	|
|	Column	|	number	|		|		|	0	|		|		|	|
|	PrereqUnitPromotionCollection	|	[[UnitPromotionPrereq]]	|	✓	|	✓	|		|		|		|	|
|	PromotionClassReference	|	[[UnitPromotionClass]]	|		|	✓	|		|		|		|	|
