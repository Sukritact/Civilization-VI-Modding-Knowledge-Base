---
tags:
- entity
- Governor
- XP2
- XP1
---
# Governor
## Entity
This file is a description of an Entity's properties. There is no accessible variable of this name, rather, these entities must be retrieved from GameData.Governor. Accessing a property should be invoked with a `.`.
## Properties
|	Property	|	Type	|	Collection Of Type?	|	May Be Nil?	|	Default	|	References	|	Key	|	Notes	|
|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	-:	|
|	GovernorType	|	string	|		|		|		|	[[Type]].Type	|	✓	|	|
|	Name	|	[[LocalizedText]]	|		|		|		|		|		|	|
|	Description	|	[[LocalizedText]]	|		|		|		|		|		|	|
|	IdentityPressure	|	number	|		|		|	0	|		|		|	|
|	Title	|	[[LocalizedText]]	|		|		|		|		|		|	|
|	ShortTitle	|	[[LocalizedText]]	|		|		|		|		|		|	|
|	TransitionStrength	|	number	|		|		|	0	|		|		|	|
|	AssignCityState	|	boolean	|		|		|	0	|		|		|	|
|	Image	|	string	|		|		|	NO_IMAGE	|		|		|	|
|	PortraitImage	|	string	|		|		|		|		|		|	|
|	PortraitImageSelected	|	string	|		|		|		|		|		|	|
|	TraitType	|	string	|		|	✓	|		|	[[Trait]].TraitType	|		|	|
|	PromotionCollection	|	[[GovernorPromotion]]	|	✓	|	✓	|		|		|		|	|
|	SecretSocietyCollection	|	[[SecretSociety]]	|	✓	|	✓	|		|		|		|	|
