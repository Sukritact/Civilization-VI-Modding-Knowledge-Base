# CityBuildQueue:GetAt
> this function is a member of [[CityBuildQueue]]
> this method expects an implicit "self" argument. invoke it with `:`
-----
## Usage
> `Queue Entry [table]` CityBuildQueue:GetAt( `Queue Position [int]` )

Unlike standard Lua arrays `Queue Position [int]` starts at 0. It returns a `table` representing whatever order is in the Build Queue at that position, or `null` if there is nothing queued at that position.

The table it returns is as follows:

| Key                   | Value | Sub-Value | Notes                                                        |
| --------------------- | ----- | --------- | ------------------------------------------------------------ |
| Directive             | Int   |           | Corresponds to an entry in the CityProductionDirectives global table |
| Modifiers             | Int   |           |                                                              |
| DistrictType          | Int   |           | Empty if not applicable.                                     |
| ProjectType           | Int   |           | Empty if not applicable.                                     |
| UnitType              | Int   |           | Empty if not applicable.                                     |
| MilitaryFormationType | Int   |           | Empty if not applicable. Corresponds to an entry in the MilitaryFormationTypes global table. Allows you to tell if the city is building a single unit, a Corps, etc. |
| BuildingType          | Int   |           | Empty if not applicable.                                     |
| Location              | Table |           |                                                              |
|                       | x     | Int       |                                                              |
|                       | y     | Int       |                                                              |

