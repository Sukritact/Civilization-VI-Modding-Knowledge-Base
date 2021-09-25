---
tags:
- entity
- HeroClass
- Hero
- Class
---
# HeroClass
## Entity
This file is a description of an Entity's properties. There is no accessible variable of this name, rather, these entities must be retrieved from GameData.HeroClass. Accessing a property should be invoked with a `.`.
## Properties
|	Property	|	Type	|	Collection Of Type?	|	May Be Nil?	|	Default	|	References	|	Key	|	Notes	|
|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	-:	|
|	HeroClassType	|	string	|		|		|		|	[[Type]].Type	|	✓	|	|
|	Name	|	[[LocalizedText]]	|		|		|		|		|		|	|
|	Description	|	[[LocalizedText]]	|		|		|		|		|		|	|
|	UnitType	|	string	|		|		|		|	[[Unit]].UnitType	|		|	|
|	CreationProjectType	|	string	|		|		|		|	[[Project]].ProjectType	|		|	|
|	ArtifactGreatWorkType	|	string	|		|	✓	|		|	[[GreatWork]].GreatWorkType	|		|	|
|	EpicGreatWorkType	|	string	|		|	✓	|		|	[[GreatWork]].GreatWorkType	|		|	|
|	DiscoveryMinEraType	|	string	|		|	✓	|		|	[[Era]].EraType	|		|	|
|	DiscoveryMinEraReference	|	[[Era]]	|		|	✓	|		|		|		|	|
|	UnitReference	|	[[Unit]]	|		|	✓	|		|		|		|	|
