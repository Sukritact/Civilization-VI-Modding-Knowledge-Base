# A Note on Value Types
While working in Lua for Civ VI, you will regularly encounter six types of values: `nil`, `number`, `string`, `boolean`, `function` and `table`. You will also encounter `object` variables; though they are often technically `tables`, are utilised significantly differently.

Civ VI occasionally uses Hungarian Notation, prefixing variables with lowercase character indication their purpose. While this does not always clearly indicate the type of the variable, it often can be extrapolated. Additionally, usage is not always consistent, so you might find cases where the variables don't follow this pattern.

Here are some often encountered prefixes:

 | Prefix |  Meaning   | Value Type | Notes                              |
 |:------:|:----------:|:----------:| ---------------------------------- |
 |   i    |  integer   |   `number`   |                                    |
 |   f    |   float    |   `number`   |                                    |
 |   e    | enumerator |   `number`   |                                    |
 |   h    |    hash    |   `number`   |                                    |
 |   b    |  boolean   |  `boolean`   |                                    |
 |   s    |   string   |   `string`   |                                    |
 |   t    |   table    |   `table`    |                                    |
 |   k    |  constant  |    N/A     | this prefix does not indicate type |
 |   p    |  pointer   |   `object`   |                                    |

The notation is sometimes extended to include the scope of a variable, optionally separated by an underscore. This extension is often also used without the Hungarian type-specification: 

-   `g_Wheels` : member of a global namespace
-   `m_wheels`, `_wheels` : member of a structure/class
-   `s_wheels` : static member of a class
-   `c_wheels` : static member of a function