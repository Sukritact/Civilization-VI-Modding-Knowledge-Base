---
tags:
- entity
- GovernorPromotion
- XP2
- XP1
- Governor
- Promotion
---
# GovernorPromotion
## Entity
This file is a description of an Entity's properties. There is no accessible variable of this name, rather, these entities must be retrieved from GameData.GovernorPromotion. Accessing a property should be invoked with a `.`.
## Properties
|	Property	|	Type	|	Collection Of Type?	|	May Be Nil?	|	Default	|	References	|	Key	|	Notes	|
|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	-:	|
|	GovernorPromotionType	|	string	|		|		|		|		|		|	|
|	Name	|	string	|		|		|		|		|		|	|
|	Description	|	string	|		|		|		|		|		|	|
|	Level	|	number	|		|		|	0	|		|		|	|
|	Column	|	number	|		|		|	0	|		|		|	|
|	BaseAbility	|	boolean	|		|		|	0	|		|		|	|
|	GovernorCollection	|	[[Governor]]	|	✓	|	✓	|		|		|		|	|
|	PrereqGovernorPromotions	|	[[GovernorPromotion]]	|	✓	|	✓	|		|		|		|	|
