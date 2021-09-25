---
tags:
- entity
- Moment
- XP2
- XP1
---
# Moment
## Entity
This file is a description of an Entity's properties. There is no accessible variable of this name, rather, these entities must be retrieved from GameData.Moment. Accessing a property should be invoked with a `.`.
## Properties
|	Property	|	Type	|	Collection Of Type?	|	May Be Nil?	|	Default	|	References	|	Key	|	Notes	|
|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	-:	|
|	MomentType	|	string	|		|		|		|	[[Type]].Type	|	✓	|	|
|	Name	|	[[LocalizedText]]	|		|		|		|		|		|	|
|	Description	|	[[LocalizedText]]	|		|		|		|		|		|	|
|	InstanceDescription	|	[[LocalizedText]]	|		|	✓	|		|		|		|	|
|	InterestLevel	|	number	|		|		|	0	|		|		|	|
|	EraScore	|	number	|		|	✓	|		|		|		|	|
|	RepeatTurnCooldown	|	number	|		|	✓	|		|		|		|	|
|	CommemorationType	|	string	|		|	✓	|		|	[[CommemorationType]].CommemorationType	|		|	|
|	MinimumGameEra	|	string	|		|	✓	|		|	[[Era]].EraType	|		|	|
|	MaximumGameEra	|	string	|		|	✓	|		|	[[Era]].EraType	|		|	|
|	BackgroundTexture	|	string	|		|	✓	|		|		|		|	|
|	IconTexture	|	string	|		|	✓	|		|		|		|	|
|	MomentIllustrationType	|	string	|		|	✓	|		|	[[MomentIllustrationType]].MomentIllustrationType	|		|	|
|	ObsoleteEra	|	string	|		|	✓	|		|	[[Era]].EraType	|		|	|
|	CommemorationReference	|	[[CommemorationType]]	|		|	✓	|		|		|		|	|
|	MaximumGameEraReference	|	[[Era]]	|		|	✓	|		|		|		|	|
|	MinimumGameEraReference	|	[[Era]]	|		|	✓	|		|		|		|	|
|	ObsoleteEraReference	|	[[Era]]	|		|	✓	|		|		|		|	|
