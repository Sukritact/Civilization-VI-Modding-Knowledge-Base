---
tags:
- entity
- Improvement_BonusYieldChange
- Improvement
- BonusYieldChange
- Bonus
- Yield
- Change
---
# Improvement_BonusYieldChange
## Entity
This file is a description of an Entity's properties. There is no accessible variable of this name, rather, these entities must be retrieved from GameData.Improvement_BonusYieldChange. Accessing a property should be invoked with a `.`.
## Properties
|	Property	|	Type	|	Collection Of Type?	|	May Be Nil?	|	Default	|	References	|	Key	|	Notes	|
|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	-:	|
|	Id	|	number	|		|		|	0	|		|		|	|
|	ImprovementType	|	string	|		|		|		|	[[Improvement]].ImprovementType	|		|	|
|	YieldType	|	string	|		|		|		|	[[Yield]].YieldType	|		|	|
|	BonusYieldChange	|	number	|		|		|		|		|		|	|
|	PrereqTech	|	string	|		|	✓	|		|	[[Technology]].TechnologyType	|		|	|
|	PrereqCivic	|	string	|		|	✓	|		|	[[Civic]].CivicType	|		|	|
|	ImprovementReference	|	[[Improvement]]	|		|	✓	|		|		|		|	|
|	PrereqCivicReference	|	[[Civic]]	|		|	✓	|		|		|		|	|
|	PrereqTechReference	|	[[Technology]]	|		|	✓	|		|		|		|	|
|	YieldReference	|	[[Yield]]	|		|	✓	|		|		|		|	|
