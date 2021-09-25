---
tags:
- entity
- StartBiasFeature
- Start
- Bias
- Feature
---
# StartBiasFeature
## Entity
This file is a description of an Entity's properties. There is no accessible variable of this name, rather, these entities must be retrieved from GameData.StartBiasFeature. Accessing a property should be invoked with a `.`.
## Properties
|	Property	|	Type	|	Collection Of Type?	|	May Be Nil?	|	Default	|	References	|	Key	|	Notes	|
|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	-:	|
|	CivilizationType	|	string	|		|		|		|	[[Civilization]].CivilizationType	|		|	|
|	FeatureType	|	string	|		|		|		|	[[Feature]].FeatureType	|		|	|
|	Tier	|	number	|		|		|	-1	|		|		|	|
|	CivilizationReference	|	[[Civilization]]	|		|	✓	|		|		|		|	|
|	FeatureReference	|	[[Feature]]	|		|	✓	|		|		|		|	|
