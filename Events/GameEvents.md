## Static Events
Events can be subscribed by using `GameEvents.SomeEvent.Add(SomeFunction)`.

| Name | Parameters |
|:---- |:--------- |
| [[BuildingConstructed]] | `playerID [number]`<br/>`cityID [number]`<br/>`buildingID [number]`<br/>`plotID [number]`<br/>`bOriginalConstruction [boolean]` |
| [[BuildingPillageStateChanged]] | `playerID [number]`<br/>`cityID [number]`<br/>`buildingID [number]`<br/>`bPillageState [boolean]` |
| [[CityBuilt]] | `playerID [number]`<br/>`cityID [number]`<br/>`iX [number]`<br/>`iY [number]` |
| [[CityConquered]] | `newPlayerID [number]`<br/>`oldPlayerID [number]`<br/>`newCityID [number]`<br/>`iCityX [number]`<br/>`iCityY [number]` |
| [[DiploSurpriseDeclareWar]] | `mainPlayer [number]`<br/>`opponentPlayer [number]` |
| [[EventPopupChoice]] | `playerID [number]`<br/>`tParameters [table]` |
| [[FoundNewWorld]] | `playerID [number]`<br/>`Threshold [number]` |
| [[HasFourCities]] | `playerID [number]`<br/>`Threshold [number]` |
| [[OnCityPopulationChanged]] | `cityOwner [number]`<br/>`cityID [number]`<br/>`ChangeAmount [number]` |
| [[OnCivicCulturevated]] | `iPlayer [number]`<br/>`eCivic [number]` |
| [[OnDistrictConstructed]] | `playerID [number]`<br/>`districtID [number]`<br/>`iX [number]`<br/>`iY [number]` |
| [[OnFaithEarned]] | `ePlayer [number]`<br/>`iFaithAmount [number]` |
| [[OnGameTurnStarted]] | `playerID [number]` |
| [[OnNewMajorityReligion]] |  |
| [[OnPillage]] | `playerID [number]`<br/>`unitID [number]`<br/>`bImprovement [boolean]`<br/>`buildingType [number]` |
| [[OnPlayerCommandSetObjectState]] | `playerID [number]`<br/>`tParameters [table]` |
| [[OnPlayerGaveInfluenceToken]] | `majorID [number]`<br/>`minorID [number]`<br/>`iAmount [number]` |
| [[OnRandomEventOccurred]] | `iType [number]`<br/>`iSeverity [number]`<br/>`iX [number]`<br/>`iY [number]`<br/>`iMitigationLevel [number]` |
| [[OnUnitRetreated]] | `unitOwner [number]`<br/>`unitID [number]` |
| [[PlayerTurnStartComplete]] | `playerID [number]` |
| [[PlayerTurnStarted]] | `playerID [number]` |
| [[PlotOwnershipChanged]] |  |
| [[PlotPropertyChanged]] | `iX [number]`<br/>`iY [number]` |
| [[PolicyChanged]] | `playerID [number]`<br/>`policyID [number]`<br/>`bEnacted [boolean]` |
| [[UnitAddedToMap]] | `playerID [number]`<br/>`unitID [number]` |
