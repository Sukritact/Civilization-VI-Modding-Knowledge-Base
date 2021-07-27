# GameGreatPeople:CreatePerson
> this function is a member of [[GameGreatPeople]]
> this method expects an implicit "self" argument. invoke it with `:`
-----
## Usage
> GameGreatPeople:CreatePerson(`PlayerID [number]`,  `IndividualID [number]` , `X [number]` , `Y [number]`)

Creates the specified Great Person Individual. Units created this way will stack on the specified tile with no limit.

Great Person Recruitment history is not updated, and it does not seem to prevent the same Great Person Individual from being earned normally through gameplay. This contrasts with [[GameGreatPeople.GrantPerson]] which does.

### Parameters
- `playerID [number]`
- `IndividualID [number]` 
	- Corresponds to a an `Index` or `Hash` column in the `GreatPersonIndividuals` table
- `X [number]`
- `Y [number]`