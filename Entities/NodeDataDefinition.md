---
tags:
- entity
- NodeDataDefinition
- Node
- Data
- Definition
---
# NodeDataDefinition
## Entity
This file is a description of an Entity's properties. There is no accessible variable of this name, rather, these entities must be retrieved from GameData.NodeDataDefinition. Accessing a property should be invoked with a `.`.
## Properties
|	Property	|	Type	|	Collection Of Type?	|	May Be Nil?	|	Default	|	References	|	Key	|	Notes	|
|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	-:	|
|	DataName	|	string	|		|		|		|		|		|	|
|	DefnId	|	number	|		|		|		|		|		|	|
|	DataType	|	string	|		|		|		|	[[DataType]].TypeName	|		|	|
|	NodeType	|	string	|		|		|		|	[[NodeDefinition]].NodeType	|		|	|
|	Required	|	boolean	|		|		|	0	|		|		|	|
|	RequiredGroup	|	boolean	|		|		|	0	|		|		|	|
|	Output	|	boolean	|		|		|	0	|		|		|	|
|	Modified	|	boolean	|		|		|	0	|		|		|	|
|	UserData	|	boolean	|		|		|	0	|		|		|	|
|	Automatic	|	boolean	|		|		|	0	|		|		|	|
|	Tagged	|	boolean	|		|		|	0	|		|		|	|
|	EnumList	|	string	|		|	✓	|		|		|		|	|
|	UniqueId	|	number	|		|		|		|		|	✓	|	|
