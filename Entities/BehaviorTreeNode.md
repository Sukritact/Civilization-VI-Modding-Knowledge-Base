---
tags:
- entity
- BehaviorTreeNode
- Behavior
- Tree
- Node
---
# BehaviorTreeNode
## Entity
This file is a description of an Entity's properties. There is no accessible variable of this name, rather, these entities must be retrieved from GameData.BehaviorTreeNode. Accessing a property should be invoked with a `.`.
## Properties
|	Property	|	Type	|	Collection Of Type?	|	May Be Nil?	|	Default	|	References	|	Key	|	Notes	|
|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	-:	|
|	TreeName	|	string	|		|		|		|	[[BehaviorTree]].TreeName	|		|	|
|	NodeId	|	number	|		|		|		|		|		|	|
|	JumpTo	|	number	|		|		|	0	|		|		|	|
|	NodeType	|	string	|		|		|		|	[[NodeDefinition]].NodeType	|		|	|
|	PrimaryKey	|	number	|		|		|		|		|	✓	|	|
