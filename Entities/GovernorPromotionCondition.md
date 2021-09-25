---
tags:
- entity
- GovernorPromotionCondition
- XP2
- XP1
- Governor
- Promotion
- Condition
---
# GovernorPromotionCondition
## Entity
This file is a description of an Entity's properties. There is no accessible variable of this name, rather, these entities must be retrieved from GameData.GovernorPromotionCondition. Accessing a property should be invoked with a `.`.
## Properties
|	Property	|	Type	|	Collection Of Type?	|	May Be Nil?	|	Default	|	References	|	Key	|	Notes	|
|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	-:	|
|	GovernorPromotionType	|	string	|		|		|		|	[[GovernorPromotion]].GovernorPromotionType	|	✓	|	|
|	HiddenWithoutPrereqs	|	boolean	|		|		|		|		|		|	|
|	EarliestGameEra	|	string	|		|	✓	|		|	[[Era]].EraType	|		|	|
|	EarliestGameEraReference	|	[[Era]]	|		|	✓	|		|		|		|	|
