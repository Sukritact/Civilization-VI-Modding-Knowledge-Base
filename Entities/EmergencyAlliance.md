---
tags:
- entity
- EmergencyAlliance
- XP2
- XP1
- Emergency
- Alliance
---
# EmergencyAlliance
## Entity
This file is a description of an Entity's properties. There is no accessible variable of this name, rather, these entities must be retrieved from GameData.EmergencyAlliance. Accessing a property should be invoked with a `.`.
## Properties
|	Property	|	Type	|	Collection Of Type?	|	May Be Nil?	|	Default	|	References	|	Key	|	Notes	|
|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	-:	|
|	EmergencyType	|	string	|		|		|		|	[[Type]].Type	|	✓	|	|
|	Trigger	|	string	|		|		|		|		|		|	|
|	TargetRequirementSet	|	string	|		|	✓	|		|		|		|	|
|	GoalTrigger	|	string	|		|		|		|		|		|	|
|	MemberRequirementSet	|	string	|		|	✓	|		|	[[RequirementSet]].RequirementSetId	|		|	|
|	Duration	|	number	|		|		|	0	|		|		|	|
|	RemovesWarState	|	boolean	|		|		|	1	|		|		|	|
|	ShareVis	|	boolean	|		|		|	0	|		|		|	|
|	OpenBorders	|	boolean	|		|		|	0	|		|		|	|
|	KillFriendship	|	boolean	|		|		|	1	|		|		|	|
|	WarOnTarget	|	boolean	|		|		|	1	|		|		|	|
|	InformTarget	|	boolean	|		|		|	1	|		|		|	|
|	LockoutTime	|	number	|		|		|	0	|		|		|	|
|	EmergencyText	|	string	|		|		|		|	[[EmergencyText]].Type	|		|	|
|	GoalText	|	string	|		|		|		|	[[EmergencyGoalText]].GoalType	|		|	|
|	Name	|	string	|		|		|		|		|		|	|
|	Effects	|	[[EmergencyBuff]]	|	✓	|	✓	|		|		|		|	|
|	EmergencyTextBlock	|	[[EmergencyText]]	|		|	✓	|		|		|		|	|
|	GoalTextBlock	|	[[EmergencyGoalText]]	|		|	✓	|		|		|		|	|
|	Rewards	|	[[EmergencyReward]]	|	✓	|	✓	|		|		|		|	|
