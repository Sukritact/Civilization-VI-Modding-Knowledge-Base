---
tags:
- entity
- Boost
---
# Boost
## Entity
This file is a description of an Entity's properties. There is no accessible variable of this name, rather, these entities must be retrieved from GameData.Boost. Accessing a property should be invoked with a `.`.
## Properties
|	Property	|	Type	|	Collection Of Type?	|	May Be Nil?	|	Default	|	References	|	Key	|	Notes	|
|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	-:	|
|	BoostID	|	number	|		|		|		|		|	✓	|	|
|	TechnologyType	|	string	|		|	✓	|		|	[[Technology]].TechnologyType	|		|	|
|	CivicType	|	string	|		|	✓	|		|	[[Civic]].CivicType	|		|	|
|	Boost	|	number	|		|		|		|		|		|	|
|	TriggerId	|	number	|		|		|	0	|		|		|	|
|	TriggerDescription	|	string	|		|		|		|		|		|	|
|	TriggerLongDescription	|	string	|		|		|		|		|		|	|
|	Unit1Type	|	string	|		|	✓	|		|	[[Unit]].UnitType	|		|	|
|	BoostClass	|	string	|		|		|		|	[[BoostName]].BoostType	|		|	|
|	Unit2Type	|	string	|		|	✓	|		|	[[Unit]].UnitType	|		|	|
|	BuildingType	|	string	|		|	✓	|		|	[[Building]].BuildingType	|		|	|
|	ImprovementType	|	string	|		|	✓	|		|	[[Improvement]].ImprovementType	|		|	|
|	BoostingTechType	|	string	|		|	✓	|		|	[[Technology]].TechnologyType	|		|	|
|	ResourceType	|	string	|		|	✓	|		|	[[Resource]].ResourceType	|		|	|
|	NumItems	|	number	|		|		|	0	|		|		|	|
|	DistrictType	|	string	|		|	✓	|		|	[[District]].DistrictType	|		|	|
|	RequiresResource	|	boolean	|		|		|	0	|		|		|	|
|	RequirementSetId	|	string	|		|	✓	|		|		|		|	|
|	GovernmentSlotType	|	string	|		|	✓	|		|	[[GovernmentSlot]].GovernmentSlotType	|		|	|
|	BoostingCivicType	|	string	|		|	✓	|		|	[[Civic]].CivicType	|		|	|
|	GovernmentTierType	|	string	|		|	✓	|		|	[[GovernmentTier]].TierType	|		|	|
|	BoostingCivicReference	|	[[Civic]]	|		|	✓	|		|		|		|	|
|	BoostingTechReference	|	[[Technology]]	|		|	✓	|		|		|		|	|
|	BoostReference	|	[[BoostName]]	|		|	✓	|		|		|		|	|
|	BuildingReference	|	[[Building]]	|		|	✓	|		|		|		|	|
|	CivicReference	|	[[Civic]]	|		|	✓	|		|		|		|	|
|	DistrictReference	|	[[District]]	|		|	✓	|		|		|		|	|
|	GovernmentTierReference	|	[[GovernmentTier]]	|		|	✓	|		|		|		|	|
|	ImprovementReference	|	[[Improvement]]	|		|	✓	|		|		|		|	|
|	ResourceReference	|	[[Resource]]	|		|	✓	|		|		|		|	|
|	TechnologyReference	|	[[Technology]]	|		|	✓	|		|		|		|	|
|	Unit1Reference	|	[[Unit]]	|		|	✓	|		|		|		|	|
|	Unit2Reference	|	[[Unit]]	|		|	✓	|		|		|		|	|
