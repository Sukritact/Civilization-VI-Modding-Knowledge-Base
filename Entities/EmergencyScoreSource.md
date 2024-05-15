---
tags:
- entity
- EmergencyScoreSource
- XP2
- Emergency
- Score
- Source
---
# EmergencyScoreSource
## Entity
This file is a description of an Entity's properties. There is no accessible variable of this name, rather, these entities must be retrieved from GameData.EmergencyScoreSource. Accessing a property should be invoked with a `.`.
## Properties
|	Property	|	Type	|	Collection Of Type?	|	May Be Nil?	|	Default	|	References	|	Key	|	Notes	|
|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	-:	|
|	ScoreSourceType	|	string	|		|	✓	|		|		|	✓	|	|
|	EmergencyType	|	string	|		|		|		|	[[Emergencies_XP2]].EmergencyType	|		|	|
|	Description	|	string	|		|	✓	|		|		|		|	|
|	ScoreAmount	|	number	|		|		|	0	|		|		|	|
|	FromProject	|	string	|		|	✓	|		|	[[Projects_XP2]].ProjectType	|		|	|
|	MilitaryInEnemyTerritory	|	boolean	|		|		|	0	|		|		|	|
|	ReligiousInEnemyTerritory	|	boolean	|		|		|	0	|		|		|	|
|	AttackedEnemyCity	|	boolean	|		|		|	0	|		|		|	|
|	FromGold	|	boolean	|		|		|	0	|		|		|	|
|	KilledEnemyUnit	|	boolean	|		|		|	0	|		|		|	|
|	SpreadReligion	|	boolean	|		|		|	0	|		|		|	|
|	ReligionAttackedEnemy	|	boolean	|		|		|	0	|		|		|	|
|	ReligiousUnitsInEnemyTerritory	|	boolean	|		|		|	0	|		|		|	|
|	FromGreatPerson	|	string	|		|	✓	|		|	[[GreatPersonClass]].GreatPersonClassType	|		|	|
|	FromFavor	|	boolean	|		|		|	0	|		|		|	|
|	FromBuilding	|	string	|		|	✓	|		|	[[Building]].BuildingType	|		|	|
|	FromDistrict	|	string	|		|	✓	|		|	[[District]].DistrictType	|		|	|
|	FromCO2Footprint	|	boolean	|		|		|	0	|		|		|	|
|	FromAtWar	|	boolean	|		|		|	0	|		|		|	|
|	FromBadCO2Footprint	|	boolean	|		|		|	0	|		|		|	|
|	FromSacrificedUnitStrength	|	boolean	|		|		|	0	|		|		|	|
