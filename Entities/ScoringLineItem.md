---
tags:
- entity
- ScoringLineItem
- Scoring
- Line
- Item
---
# ScoringLineItem
## Entity
This file is a description of an Entity's properties. There is no accessible variable of this name, rather, these entities must be retrieved from GameData.ScoringLineItem. Accessing a property should be invoked with a `.`.
## Properties
|	Property	|	Type	|	Collection Of Type?	|	May Be Nil?	|	Default	|	References	|	Key	|	Notes	|
|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	-:	|
|	LineItemType	|	string	|		|		|		|		|	✓	|	|
|	Name	|	string	|		|		|		|		|		|	|
|	Category	|	string	|		|		|		|	[[ScoringCategory]].CategoryType	|		|	|
|	Multiplier	|	number	|		|		|	1	|		|		|	|
|	ScaleByCost	|	boolean	|		|		|	0	|		|		|	|
|	Civics	|	boolean	|		|		|	0	|		|		|	|
|	Cities	|	boolean	|		|		|	0	|		|		|	|
|	Districts	|	boolean	|		|		|	0	|		|		|	|
|	Population	|	boolean	|		|		|	0	|		|		|	|
|	GreatPeople	|	boolean	|		|		|	0	|		|		|	|
|	Techs	|	boolean	|		|		|	0	|		|		|	|
|	Wonders	|	boolean	|		|		|	0	|		|		|	|
|	Religion	|	boolean	|		|		|	0	|		|		|	|
|	Pillage	|	boolean	|		|		|	0	|		|		|	|
|	Trade	|	boolean	|		|		|	0	|		|		|	|
|	GoldPerTurn	|	boolean	|		|		|	0	|		|		|	|
|	TieBreakerPriority	|	number	|		|		|		|		|		|	|
|	ScoringScenario1	|	boolean	|		|		|	0	|		|		|	|
|	ScoringScenario2	|	boolean	|		|		|	0	|		|		|	|
|	ScoringScenario3	|	boolean	|		|		|	0	|		|		|	|
|	EraScore	|	boolean	|		|		|	0	|		|		|	|
|	Converted	|	boolean	|		|		|	0	|		|		|	|
|	Buildings	|	boolean	|		|		|	0	|		|		|	|
|	CategoryReference	|	[[ScoringCategory]]	|		|	✓	|		|		|		|	|
