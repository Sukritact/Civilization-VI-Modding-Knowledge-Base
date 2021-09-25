---
tags:
- entity
- Discussion
- XP2
---
# Discussion
## Entity
This file is a description of an Entity's properties. There is no accessible variable of this name, rather, these entities must be retrieved from GameData.Discussion. Accessing a property should be invoked with a `.`.
## Properties
|	Property	|	Type	|	Collection Of Type?	|	May Be Nil?	|	Default	|	References	|	Key	|	Notes	|
|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	-:	|
|	DiscussionType	|	string	|		|		|		|	[[Type]].Type	|	✓	|	|
|	ProposalType	|	string	|		|		|		|	[[ProposalType]].ProposalType	|		|	|
|	Name	|	string	|		|		|		|		|		|	|
|	Description	|	string	|		|		|		|		|		|	|
|	EmergencyType	|	string	|		|	✓	|		|	[[Emergencies_XP2]].EmergencyType	|		|	|
|	AiChangeCollectionReference	|	[[CongressAiChange]]	|	✓	|	✓	|		|		|		|	|
|	EmergencyReference	|	[[EmergencyAlliance]]	|		|	✓	|		|		|		|	|
