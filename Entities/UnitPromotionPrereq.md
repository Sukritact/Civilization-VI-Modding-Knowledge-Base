---
tags:
- entity
- UnitPromotionPrereq
- Unit
- Promotion
- Prereq
---
# UnitPromotionPrereq
## Entity
This file is a description of an Entity's properties. There is no accessible variable of this name, rather, these entities must be retrieved from GameData.UnitPromotionPrereq. Accessing a property should be invoked with a `.`.
## Properties
|	Property	|	Type	|	Collection Of Type?	|	May Be Nil?	|	Default	|	References	|	Key	|	Notes	|
|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	-:	|
|	UnitPromotion	|	string	|		|		|		|	[[UnitPromotion]].UnitPromotionType	|		|	|
|	PrereqUnitPromotion	|	string	|		|		|		|	[[UnitPromotion]].UnitPromotionType	|		|	|
|	PrereqUnitPromotionReference	|	[[UnitPromotion]]	|		|	✓	|		|		|		|	|
|	UnitPromotionReference	|	[[UnitPromotion]]	|		|	✓	|		|		|		|	|
