---
UI: true
arguments:
- QueuePosition [number]
invoke: ':'
memberOf: City/CityBuildQueue
methodname: GetAt
returns:
- QueueEntry [table]
script: false
tags:
- City/CityBuildQueue/_function
- function/UI
---
# CityBuildQueue:GetAt
> this function is a member of [[CityBuildQueue]]
> this method expects an implicit "self" argument. invoke it with `:`
-----
## Usage
|  UI | Script | Returns | Function | Arguments |
|:---:|:------:|-------:|:--------:|:---------|
|✓| |`QueueEntry [table]`|CityBuildQueue:GetAt|`QueuePosition [number]`|

## Notes
Unlike standard Lua arrays `QueuePosition [number]` starts at 0. It returns a `table` representing whatever order is in the Build Queue at that position, or `null` if there is nothing queued at that position.

The table it returns is as follows:

| Key                   | Value | Sub-Value | Notes                                                        |
| --------------------- | :-----: | :---------: | ------------------------------------------------------------ |
| Directive             | integer   |           | Corresponds to an entry in the CityProductionDirectives global table |
| Modifiers             | integer   |           |                                                              |
| DistrictType          | integer   |           | Empty if not applicable.                                     |
| ProjectType           | integer   |           | Empty if not applicable.                                     |
| UnitType              | integer   |           | Empty if not applicable.                                     |
| MilitaryFormationType | integer   |           | Empty if not applicable. Corresponds to an entry in the MilitaryFormationTypes global table. Allows you to tell if the city is building a single unit, a Corps, etc. |
| BuildingType          | integer   |           | Empty if not applicable.                                     |
| Location              | table |           |                                                              |
|                       | x     | integer       |                                                              |
|                       | y     | integer       |                                                              |