---
tags:
- entity
- Improvement_ValidTerrain
- Improvement
- ValidTerrain
- Valid
- Terrain
---
# Improvement_ValidTerrain
## Entity
This file is a description of an Entity's properties. There is no accessible variable of this name, rather, these entities must be retrieved from GameData.Improvement_ValidTerrain. Accessing a property should be invoked with a `.`.
## Properties
|	Property	|	Type	|	Collection Of Type?	|	May Be Nil?	|	Default	|	References	|	Key	|	Notes	|
|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	-:	|
|	ImprovementType	|	string	|		|		|		|	[[Improvement]].ImprovementType	|		|	|
|	TerrainType	|	string	|		|		|		|	[[Terrain]].TerrainType	|		|	|
|	PrereqTech	|	string	|		|	✓	|		|	[[Technology]].TechnologyType	|		|	|
|	PrereqCivic	|	string	|		|	✓	|		|	[[Civic]].CivicType	|		|	|
|	ImprovementReference	|	[[Improvement]]	|		|	✓	|		|		|		|	|
|	PrereqCivicReference	|	[[Civic]]	|		|	✓	|		|		|		|	|
|	PrereqTechReference	|	[[Technology]]	|		|	✓	|		|		|		|	|
|	TerrainReference	|	[[Terrain]]	|		|	✓	|		|		|		|	|
