---
UI: true
arguments: []
invoke: ':'
memberOf: Unit
methodname: GetLocation
returns:
- UnitLocation [table]
script: true
tags:
- Unit/_function
- function/UI
- function/script
---
# Unit:GetLocation
> this function is a member of [[Unit]]
> this method expects an implicit "self" argument. invoke it with `:`
-----
## Usage
|  UI | Script | Returns | Function | Arguments |
|:---:|:------:|-------:|:--------:|:---------|
|✓|✓|`UnitLocation [table]`|Unit:GetLocation||

## Notes
The function returns a table with two indices: `x`, and `y`.