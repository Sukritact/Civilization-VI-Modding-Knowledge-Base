---
tags:
- entity
- Unit
---
# Unit
## Entity
This file is a description of an Entity's properties. There is no accessible variable of this name, rather, these entities must be retrieved from GameData.Unit. Accessing a property should be invoked with a `.`.
## Properties
|	Property	|	Type	|	Collection Of Type?	|	May Be Nil?	|	Default	|	References	|	Key	|	Notes	|
|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	-:	|
|	UnitType	|	string	|		|		|		|	[[Type]].Type	|	✓	|	|
|	Name	|	string	|		|		|		|		|		|	|
|	BaseSightRange	|	number	|		|		|		|		|		|	|
|	BaseMoves	|	number	|		|		|		|		|		|	|
|	Combat	|	number	|		|		|	0	|		|		|	|
|	RangedCombat	|	number	|		|		|	0	|		|		|	|
|	Range	|	number	|		|		|	0	|		|		|	|
|	Bombard	|	number	|		|		|	0	|		|		|	|
|	Domain	|	string	|		|		|		|		|		|	|
|	FormationClass	|	string	|		|		|		|		|		|	|
|	Cost	|	number	|		|		|		|		|		|	|
|	PopulationCost	|	number	|		|	✓	|		|		|		|	|
|	FoundCity	|	boolean	|		|		|	0	|		|		|	|
|	FoundReligion	|	boolean	|		|		|	0	|		|		|	|
|	MakeTradeRoute	|	boolean	|		|		|	0	|		|		|	|
|	EvangelizeBelief	|	boolean	|		|		|	0	|		|		|	|
|	LaunchInquisition	|	boolean	|		|		|	0	|		|		|	|
|	RequiresInquisition	|	boolean	|		|		|	0	|		|		|	|
|	BuildCharges	|	number	|		|		|	0	|		|		|	|
|	ReligiousStrength	|	number	|		|		|	0	|		|		|	|
|	ReligionEvictPercent	|	number	|		|		|	0	|		|		|	|
|	SpreadCharges	|	number	|		|		|	0	|		|		|	|
|	ReligiousHealCharges	|	number	|		|		|	0	|		|		|	|
|	ExtractsArtifacts	|	boolean	|		|		|	0	|		|		|	|
|	Description	|	string	|		|	✓	|		|		|		|	|
|	Flavor	|	string	|		|	✓	|		|	[[Flavor]].FlavorType	|		|	|
|	CanCapture	|	boolean	|		|		|	1	|		|		|	|
|	CanRetreatWhenCaptured	|	boolean	|		|		|	0	|		|		|	|
|	TraitType	|	string	|		|	✓	|		|	[[Trait]].TraitType	|		|	|
|	AllowBarbarians	|	boolean	|		|		|	0	|		|		|	|
|	CostProgressionModel	|	string	|		|		|	NO_COST_PROGRESSION	|		|		|	|
|	CostProgressionParam1	|	number	|		|		|	0	|		|		|	|
|	PromotionClass	|	string	|		|	✓	|		|	[[UnitPromotionClass]].PromotionClassType	|		|	|
|	InitialLevel	|	number	|		|		|	1	|		|		|	|
|	NumRandomChoices	|	number	|		|		|	0	|		|		|	|
|	PrereqTech	|	string	|		|	✓	|		|	[[Technology]].TechnologyType	|		|	|
|	PrereqCivic	|	string	|		|	✓	|		|	[[Civic]].CivicType	|		|	|
|	PrereqDistrict	|	string	|		|	✓	|		|	[[District]].DistrictType	|		|	|
|	PrereqPopulation	|	number	|		|	✓	|		|		|		|	|
|	LeaderType	|	string	|		|	✓	|		|		|		|	|
|	CanTrain	|	boolean	|		|		|	1	|		|		|	|
|	StrategicResource	|	string	|		|	✓	|		|	[[Resource]].ResourceType	|		|	|
|	PurchaseYield	|	string	|		|	✓	|		|	[[Yield]].YieldType	|		|	|
|	MustPurchase	|	boolean	|		|		|	0	|		|		|	|
|	Maintenance	|	number	|		|		|	0	|		|		|	|
|	Stackable	|	boolean	|		|		|	0	|		|		|	|
|	AirSlots	|	number	|		|		|	0	|		|		|	|
|	CanTargetAir	|	boolean	|		|		|	0	|		|		|	|
|	PseudoYieldType	|	string	|		|	✓	|		|	[[PseudoYield]].PseudoYieldType	|		|	|
|	ZoneOfControl	|	boolean	|		|		|	0	|		|		|	|
|	AntiAirCombat	|	number	|		|		|	0	|		|		|	|
|	Spy	|	boolean	|		|		|	0	|		|		|	|
|	WMDCapable	|	boolean	|		|		|	0	|		|		|	|
|	ParkCharges	|	number	|		|		|	0	|		|		|	|
|	IgnoreMoves	|	boolean	|		|		|	0	|		|		|	|
|	TeamVisibility	|	boolean	|		|		|	0	|		|		|	|
|	ObsoleteTech	|	string	|		|	✓	|		|	[[Technology]].TechnologyType	|		|	|
|	ObsoleteCivic	|	string	|		|	✓	|		|	[[Civic]].CivicType	|		|	|
|	MandatoryObsoleteTech	|	string	|		|	✓	|		|	[[Technology]].TechnologyType	|		|	|
|	MandatoryObsoleteCivic	|	string	|		|	✓	|		|	[[Civic]].CivicType	|		|	|
|	AdvisorType	|	string	|		|	✓	|		|		|		|	|
|	EnabledByReligion	|	boolean	|		|		|	0	|		|		|	|
|	TrackReligion	|	boolean	|		|		|	0	|		|		|	|
|	DisasterCharges	|	number	|		|		|	0	|		|		|	|
|	UseMaxMeleeTrainedStrength	|	boolean	|		|		|	0	|		|		|	|
|	ImmediatelyName	|	boolean	|		|		|	0	|		|		|	|
|	CanEarnExperience	|	boolean	|		|		|	1	|		|		|	|
|	AiInfoCollection	|	[[UnitAiInfo]]	|	✓	|	✓	|		|		|		|	|
|	BaseUnitCollection	|	[[UnitUpgrade]]	|	✓	|	✓	|		|		|		|	|
|	BonusMinorStartingUnitCollection	|	[[BonusMinorStartingUnit]]	|	✓	|	✓	|		|		|		|	|
|	CaptureCollection	|	[[UnitCapture]]	|	✓	|	✓	|		|		|		|	|
|	MajorStartingUnitCollection	|	[[MajorStartingUnit]]	|	✓	|	✓	|		|		|		|	|
|	MandatoryObsoleteCivicReference	|	[[Civic]]	|		|	✓	|		|		|		|	|
|	MandatoryObsoleteTechReference	|	[[Technology]]	|		|	✓	|		|		|		|	|
|	ObsoleteCivicReference	|	[[Civic]]	|		|	✓	|		|		|		|	|
|	ObsoleteTechReference	|	[[Technology]]	|		|	✓	|		|		|		|	|
|	PrereqBuildingCollection	|	[[Building]]	|	✓	|	✓	|		|		|		|	|
|	PrereqCivicReference	|	[[Civic]]	|		|	✓	|		|		|		|	|
|	PrereqDistrictReference	|	[[District]]	|		|	✓	|		|		|		|	|
|	PrereqTechReference	|	[[Technology]]	|		|	✓	|		|		|		|	|
|	PromotionClassReference	|	[[UnitPromotionClass]]	|		|	✓	|		|		|		|	|
|	PseudoYieldReference	|	[[PseudoYield]]	|		|	✓	|		|		|		|	|
|	ReplacedByCollection	|	[[UnitReplace]]	|	✓	|	✓	|		|		|		|	|
|	ReplacesCollection	|	[[UnitReplace]]	|	✓	|	✓	|		|		|		|	|
|	StrategicResourceReference	|	[[Resource]]	|		|	✓	|		|		|		|	|
|	TraitReference	|	[[Trait]]	|		|	✓	|		|		|		|	|
|	UpgradeUnitCollection	|	[[UnitUpgrade]]	|	✓	|	✓	|		|		|		|	|
|	YieldReference	|	[[Yield]]	|		|	✓	|		|		|		|	|
