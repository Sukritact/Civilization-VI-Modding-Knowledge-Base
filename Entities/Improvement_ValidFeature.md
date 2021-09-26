---
tags:
- entity
- Improvement_ValidFeature
- Improvement
- ValidFeature
- Valid
- Feature
---
# Improvement_ValidFeature
## Entity
This file is a description of an Entity's properties. There is no accessible variable of this name, rather, these entities must be retrieved from GameData.Improvement_ValidFeature. Accessing a property should be invoked with a `.`.
## Properties
|	Property	|	Type	|	Collection Of Type?	|	May Be Nil?	|	Default	|	References	|	Key	|	Notes	|
|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	-:	|
|	ImprovementType	|	string	|		|		|		|	[[Improvement]].ImprovementType	|		|	|
|	FeatureType	|	string	|		|		|		|	[[Feature]].FeatureType	|		|	|
|	PrereqTech	|	string	|		|	✓	|		|	[[Technology]].TechnologyType	|		|	|
|	PrereqCivic	|	string	|		|	✓	|		|	[[Civic]].CivicType	|		|	|
|	FeatureReference	|	[[Feature]]	|		|	✓	|		|		|		|	|
|	PrereqCivicReference	|	[[Civic]]	|		|	✓	|		|		|		|	|
|	PrereqTechReference	|	[[Technology]]	|		|	✓	|		|		|		|	|
