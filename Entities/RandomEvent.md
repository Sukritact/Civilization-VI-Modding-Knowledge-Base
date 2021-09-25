---
tags:
- entity
- RandomEvent
- XP2
- Random
- Event
---
# RandomEvent
## Entity
This file is a description of an Entity's properties. There is no accessible variable of this name, rather, these entities must be retrieved from GameData.RandomEvent. Accessing a property should be invoked with a `.`.
## Properties
|	Property	|	Type	|	Collection Of Type?	|	May Be Nil?	|	Default	|	References	|	Key	|	Notes	|
|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	-:	|
|	RandomEventType	|	string	|		|		|		|		|	✓	|	|
|	Name	|	string	|		|		|		|		|		|	|
|	Description	|	string	|		|		|		|		|		|	|
|	LongDescription	|	string	|		|	✓	|		|		|		|	|
|	EffectString	|	string	|		|	✓	|		|		|		|	|
|	Severity	|	number	|		|		|	-1	|		|		|	|
|	NaturalWonder	|	string	|		|	✓	|		|	[[Feature]].FeatureType	|		|	|
|	IceLoss	|	number	|		|		|	0	|		|		|	|
|	HaltsStormFertility	|	boolean	|		|		|	0	|		|		|	|
|	HaltsFloodFertility	|	boolean	|		|		|	0	|		|		|	|
|	FertilityRemovalChance	|	number	|		|		|	0	|		|		|	|
|	ClimateChangePoints	|	number	|		|		|	0	|		|		|	|
|	ChanceIncreasePerDegree	|	number	|		|		|	0	|		|		|	|
|	Hexes	|	number	|		|		|	0	|		|		|	|
|	Movement	|	number	|		|		|	0	|		|		|	|
|	Duration	|	number	|		|		|	0	|		|		|	|
|	Spacing	|	number	|		|		|	0	|		|		|	|
|	IconLarge	|	string	|		|	✓	|		|		|		|	|
|	IconSmall	|	string	|		|	✓	|		|		|		|	|
|	MinTurnAtRisk	|	number	|		|		|	0	|		|		|	|
|	MitigatedYieldReduction	|	number	|		|		|	0	|		|		|	|
|	EffectOperatorType	|	string	|		|	✓	|		|		|		|	|
|	UnitTriggered	|	boolean	|		|		|	0	|		|		|	|
|	Global	|	boolean	|		|		|	0	|		|		|	|
|	AvoidTerritory	|	boolean	|		|		|	0	|		|		|	|
|	TargetCities	|	boolean	|		|		|	0	|		|		|	|
|	DamageCollection	|	[[RandomEvent_Damage]]	|	✓	|	✓	|		|		|		|	|
|	FrequencyCollection	|	[[RandomEvent_Frequency]]	|	✓	|	✓	|		|		|		|	|
|	NaturalWonderReference	|	[[Feature]]	|		|	✓	|		|		|		|	|
|	PillagedImprovementCollection	|	[[RandomEvent_PillagedImprovement]]	|	✓	|	✓	|		|		|		|	|
|	TerrainCollection	|	[[RandomEvent_Terrain]]	|	✓	|	✓	|		|		|		|	|
|	YieldCollection	|	[[RandomEvent_Yield]]	|	✓	|	✓	|		|		|		|	|
