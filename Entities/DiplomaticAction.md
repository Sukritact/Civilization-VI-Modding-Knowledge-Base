---
tags:
- entity
- DiplomaticAction
- Diplomatic
- Action
---
# DiplomaticAction
## Entity
This file is a description of an Entity's properties. There is no accessible variable of this name, rather, these entities must be retrieved from GameData.DiplomaticAction. Accessing a property should be invoked with a `.`.
## Properties
|	Property	|	Type	|	Collection Of Type?	|	May Be Nil?	|	Default	|	References	|	Key	|	Notes	|
|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	-:	|
|	DiplomaticActionType	|	string	|		|		|		|	[[Type]].Type	|	✓	|	|
|	Name	|	string	|		|	✓	|		|		|		|	|
|	Description	|	string	|		|	✓	|		|		|		|	|
|	CivilopediaKey	|	string	|		|	✓	|		|		|		|	|
|	InitiatorPrereqCivic	|	string	|		|	✓	|		|	[[Civic]].CivicType	|		|	|
|	InitiatorPrereqTech	|	string	|		|	✓	|		|	[[Technology]].TechnologyType	|		|	|
|	TargetPrereqCivic	|	string	|		|	✓	|		|	[[Civic]].CivicType	|		|	|
|	TargetPrereqTech	|	string	|		|	✓	|		|	[[Technology]].TechnologyType	|		|	|
|	InitiatorObsoleteCivic	|	string	|		|	✓	|		|	[[Civic]].CivicType	|		|	|
|	Cost	|	number	|		|		|	0	|		|		|	|
|	RequiresCapitalPath	|	boolean	|		|		|	0	|		|		|	|
|	RequiresConvertedCity	|	boolean	|		|		|	0	|		|		|	|
|	RequiresOccupiedCity	|	boolean	|		|		|	0	|		|		|	|
|	RequiresOccupiedFriendlyCity	|	boolean	|		|		|	0	|		|		|	|
|	RequiresWarOnAlliedCityState	|	boolean	|		|		|	0	|		|		|	|
|	RequiresLeadXEras	|	number	|		|		|	0	|		|		|	|
|	RequiresArchaeologyIntrusion	|	boolean	|		|		|	0	|		|		|	|
|	RequiresAdjacentEmpires	|	boolean	|		|		|	0	|		|		|	|
|	RequiresEspionageIntrusion	|	boolean	|		|		|	0	|		|		|	|
|	NoCurrentDelegation	|	boolean	|		|		|	0	|		|		|	|
|	NoCurrentEmbassy	|	boolean	|		|		|	0	|		|		|	|
|	NoCurrentOpenBorders	|	boolean	|		|		|	0	|		|		|	|
|	NoCurrentDenunciation	|	boolean	|		|		|	0	|		|		|	|
|	NoCurrentDOF	|	boolean	|		|		|	0	|		|		|	|
|	NoCurrentResearchAgreement	|	boolean	|		|		|	0	|		|		|	|
|	NoCurrentDefensivePact	|	boolean	|		|		|	0	|		|		|	|
|	Agreement	|	boolean	|		|		|	0	|		|		|	|
|	WarmongerPercent	|	number	|		|		|	0	|		|		|	|
|	CaptureWarmongerPercent	|	number	|		|		|	0	|		|		|	|
|	RazeWarmongerPercent	|	number	|		|		|	0	|		|		|	|
|	UIGroup	|	string	|		|	✓	|		|		|		|	|
|	DenouncementTurnsRequired	|	number	|		|		|	-1	|		|		|	|
|	RequiresAlliance	|	boolean	|		|		|	0	|		|		|	|
|	RequiresTeamMembership	|	boolean	|		|		|	0	|		|		|	|
|	Duration	|	number	|		|		|	30	|		|		|	|
|	InitiatorObsoleteCivicReference	|	[[Civic]]	|		|	✓	|		|		|		|	|
|	InitiatorPrereqCivicReference	|	[[Civic]]	|		|	✓	|		|		|		|	|
|	InitiatorPrereqTechReference	|	[[Technology]]	|		|	✓	|		|		|		|	|
|	TargetPrereqCivicReference	|	[[Civic]]	|		|	✓	|		|		|		|	|
|	TargetPrereqTechReference	|	[[Technology]]	|		|	✓	|		|		|		|	|
|	ValidStates	|	[[DiplomaticState]]	|	✓	|	✓	|		|		|		|	|
