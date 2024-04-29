---
UI: false
arguments:
  - ModifierID [string]
invoke: ":"
memberOf: City
methodname: AttachModifierByID
returns: 
script: true
tags:
  - City/_function
  - function/script
---
# City:AttachModifierByID
> this function is a member of [[City]]
> this method expects an implicit "self" argument. invoke it with `:`
-----
## Usage
|  UI | Script | Returns | Function | Arguments |
|:---:|:------:|-------:|:--------:|:---------|
| |✓||City:AttachModifierByID|`ModifierID [string]`|

## Notes
`ModifierType [string]`, refers to the actual ModifierID used in the database, like `MONUMENT_LOYALTY` for example.
Modifiers attached this way are lost when ownership is transferred to another Player.
