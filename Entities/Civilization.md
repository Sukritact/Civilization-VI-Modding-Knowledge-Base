---
tags:
- entity
- Civilization
---
# Civilization
## Entity
This file is a description of an Entity's properties. There is no accessible variable of this name, rather, these entities must be retrieved from GameData.Civilization. Accessing a property should be invoked with a `.`.
## Properties
|	Property	|	Type	|	Collection Of Type?	|	May Be Nil?	|	Default	|	References	|	Key	|	Notes	|
|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	-:	|
|	CivilizationType	|	string	|		|		|		|	[[Type]].Type	|	✓	|	|
|	Name	|	[[LocalizedText]]	|		|		|		|		|		|	|
|	Description	|	string	|		|	✓	|		|		|		|	|
|	Adjective	|	string	|		|		|		|		|		|	|
|	RandomCityNameDepth	|	number	|		|		|	1	|		|		|	|
|	StartingCivilizationLevelType	|	string	|		|		|		|	[[CivilizationLevel]].CivilizationLevelType	|		|	|
|	Ethnicity	|	string	|		|	✓	|		|		|		|	|
|	CitizenNameCollection	|	[[CivilizationCitizenName]]	|	✓	|	✓	|		|		|		|	|
|	CityNameCollection	|	[[CityName]]	|	✓	|	✓	|		|		|		|	|
|	ReligionCollection	|	[[Religion]]	|	✓	|	✓	|		|		|		|	|
|	StartBiasFeatureCollection	|	[[StartBiasFeature]]	|	✓	|	✓	|		|		|		|	|
|	StartBiasResourceCollection	|	[[StartBiasResource]]	|	✓	|	✓	|		|		|		|	|
|	StartBiasRiverCollection	|	[[StartBiasRiver]]	|	✓	|	✓	|		|		|		|	|
|	StartBiasTerrainCollection	|	[[StartBiasTerrain]]	|	✓	|	✓	|		|		|		|	|
|	TraitCollection	|	[[Trait]]	|	✓	|	✓	|		|		|		|	|
