---
tags:
- entity
- Government
---
# Government
## Entity
This file is a description of an Entity's properties. There is no accessible variable of this name, rather, these entities must be retrieved from GameData.Government. Accessing a property should be invoked with a `.`.
## Properties
|	Property	|	Type	|	Collection Of Type?	|	May Be Nil?	|	Default	|	References	|	Key	|	Notes	|
|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	-:	|
|	GovernmentType	|	string	|		|		|		|	[[Type]].Type	|	✓	|	|
|	Name	|	string	|		|		|		|		|		|	|
|	PrereqCivic	|	string	|		|	✓	|		|	[[Civic]].CivicType	|		|	|
|	InherentBonusDesc	|	string	|		|		|		|		|		|	|
|	AccumulatedBonusShortDesc	|	string	|		|		|		|		|		|	|
|	AccumulatedBonusDesc	|	string	|		|		|		|		|		|	|
|	OtherGovernmentIntolerance	|	number	|		|		|	0	|		|		|	|
|	InfluencePointsPerTurn	|	number	|		|		|		|		|		|	|
|	InfluencePointsThreshold	|	number	|		|		|		|		|		|	|
|	InfluenceTokensPerThreshold	|	number	|		|		|		|		|		|	|
|	BonusType	|	string	|		|		|		|	[[GovernmentBonusName]].GovernmentBonusType	|		|	|
|	PolicyToUnlock	|	string	|		|	✓	|		|	[[Policy]].PolicyType	|		|	|
|	Tier	|	string	|		|	✓	|		|	[[GovernmentTier]].TierType	|		|	|
|	GovernmentSlotsReference	|	[[Government_SlotCount]]	|	✓	|	✓	|		|		|		|	|
|	PolicyToUnlockReference	|	[[Policy]]	|		|	✓	|		|		|		|	|
|	PrereqCivicReference	|	[[Civic]]	|		|	✓	|		|		|		|	|
|	StartingGovernmentCollection	|	[[StartingGovernment]]	|	✓	|	✓	|		|		|		|	|
