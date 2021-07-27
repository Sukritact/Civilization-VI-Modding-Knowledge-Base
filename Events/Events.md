# Events
## Usage
This object exposes events designed to make the UI react to data changes. You may try to use them to implement gameplay changes.

## Static Events
Events can be subscribed by using `Events.SomeEvent.Add(SomeFunction)`.

| Name | Parameters |
|:---- |:--------- |
| [[AllianceAvailable]] | `playerID [number]`<br/>`otherplayerID [number]`<br/>`AllianceType [number]` |
| [[AllianceEnded]] | `playerID [number]`<br/>`otherplayerID [number]`<br/>`AllianceType [number]` |
| [[AnarchyBegins]] |  |
| [[AnarchyEnds]] |  |
| [[BarbarianRaidStarted]] |  |
| [[BarbarianSpottedCity]] | `playerID [number]`<br/>`unitID [number]`<br/>`cityOwner [number]`<br/>`cityID [number]` |
| [[BeginWonderReveal]] |  |
| [[BeliefAdded]] | `playerID [number]`<br/>`beliefID [number]` |
| [[BuildingAddedToMap]] | `iX [number]`<br/>`iY [number]`<br/>`buildingID [number]`<br/>`playerID [number]`<br/>`misc2`<br/>`misc3` |
| [[BuildingBuildProgressChanged]] |  |
| [[BuildingChanged]] | `iX [number]`<br/>`iY [number]`<br/>`buildingID [number]`<br/>`playerID [number]`<br/>`iPercentComplete [number]`<br/>`iUnknown` |
| [[BuildingPillaged]] |  |
| [[BuildingRemovedFromMap]] | `iX [number]`<br/>`iY [number]` |
| [[BuildingVisibilityChanged]] |  |
| [[CacheUpdate]] |  |
| [[CameraUpdated]] | `vFocusX [number]`<br/>`vFocusY [number]`<br/>`fZoomLevel [number]` |
| [[CapitalCityChanged]] | `playerID [number]`<br/>`cityID [number]` |
| [[CityAddedToMap]] | `playerID [number]`<br/>`cityID [number]`<br/>`iX [number]`<br/>`iY [number]` |
| [[CityChanged]] |  |
| [[CityCommandStarted]] | `cityOwnerID [number]`<br/>`cityID [number]`<br/>`districtOwnerID [number]`<br/>`commandType [number]`<br/>`iData1 [number]` |
| [[CityDefenseStatusChanged]] | `playerID [number]`<br/>`iValue [number]` |
| [[CityFocusChanged]] | `playerID [number]`<br/>`cityID [number]` |
| [[CityInitialized]] | `playerID [number]`<br/>`cityID [number]`<br/>`iX [number]`<br/>`iY [number]` |
| [[CityLiberated]] | `playerID [number]`<br/>`cityID [number]` |
| [[CityLoyaltyChanged]] | `playerID [number]`<br/>`cityID [number]` |
| [[CityMadePurchase]] | `playerID [number]`<br/>`cityID [number]`<br/>`iX [number]`<br/>`iY [number]`<br/>`purchaseType [number]`<br/>`objectType [number]` |
| [[CityNameChanged]] | `playerID [number]`<br/>`cityID [number]` |
| [[CityOccupationChanged]] | `playerID [number]`<br/>`cityID [number]` |
| [[CityPopulationChanged]] | `playerID [number]`<br/>`cityID [number]`<br/>`cityPopulation [number]` |
| [[CityProductionChanged]] | `playerID [number]`<br/>`cityID [number]`<br/>`productionID [number]`<br/>`objectID [number]`<br/>`bCancelled [boolean]` |
| [[CityProductionCompleted]] | `playerID [number]`<br/>`cityID [number]`<br/>`iConstructionType [number]`<br/>`unitID [number]`<br/>`bCancelled [boolean]` |
| [[CityProductionUpdated]] | `playerID [number]`<br/>`cityID [number]`<br/>`objectID [number]`<br/>`productionID [number]` |
| [[CityProjectCompleted]] | `playerID [number]`<br/>`cityID [number]`<br/>`projectID [number]`<br/>`buildingIndex [number]`<br/>`iX [number]`<br/>`iY [number]`<br/>`bCancelled [boolean]` |
| [[CityReligionChanged]] | `playerID [number]`<br/>`cityID [number]`<br/>`eVisibility [number]`<br/>`city` |
| [[CityReligionFollowersChanged]] | `playerID [number]`<br/>`cityID [number]`<br/>`eVisibility [number]`<br/>`city` |
| [[CityRemovedFromMap]] | `playerID [number]`<br/>`cityID [number]` |
| [[CitySiegeStatusChanged]] | `playerID [number]`<br/>`cityID [number]`<br/>`bIsBesieged [boolean]` |
| [[CityTileOwnershipChanged]] | `owner [number]`<br/>`cityID [number]` |
| [[CityTransfered]] | `playerID [number]`<br/>`cityID [number]` |
| [[CityUnitsChanged]] | `playerID [number]`<br/>`cityID [number]` |
| [[CityVisibilityChanged]] | `playerID [number]`<br/>`cityID [number]`<br/>`eVisibility [number]` |
| [[CityWorkerChanged]] | `ownerPlayerID [number]`<br/>`cityID [number]`<br/>`iX [number]`<br/>`iY [number]` |
| [[CivicBoostTriggered]] | `playerID [number]`<br/>`iBoostedCivic [number]`<br/>`iUnknownA [number]`<br/>`iUnknownB [number]` |
| [[CivicChanged]] | `ePlayer [number]`<br/>`eCivic [number]` |
| [[CivicCompleted]] | `playerID [number]`<br/>`iCivic [number]`<br/>`bCancelled [boolean]` |
| [[CivicQueueChanged]] |  |
| [[CivicsUnlocked]] |  |
| [[CliffAddedToMap]] |  |
| [[CliffRemovedFromMap]] |  |
| [[Combat]] | `combatResult [table]` |
| [[CulturalIdentityCitizenConverted]] |  |
| [[CulturalIdentityCityConverted]] | `player [number]`<br/>`cityID [number]`<br/>`fromPlayer [number]` |
| [[CulturalIdentityConversionOutcomeChanged]] | `player [number]`<br/>`cityID [number]`<br/>`eOutcome [number]` |
| [[CultureChanged]] |  |
| [[CultureYieldChanged]] | `ePlayer [number]` |
| [[DiplomacyDealEnacted]] |  |
| [[DiplomacyDealExpired]] |  |
| [[DiplomacyDeclareWar]] | `firstPlayerID [number]`<br/>`secondPlayerID [number]` |
| [[DiplomacyIncomingDeal]] | `eFromPlayer [number]`<br/>`eToPlayer [number]`<br/>`eAction [number]` |
| [[DiplomacyMakePeace]] | `firstPlayerID [number]`<br/>`secondPlayerID [number]` |
| [[DiplomacyMeet]] | `player1ID [number]`<br/>`player2ID [number]` |
| [[DiplomacyMeetMajorMinor]] |  |
| [[DiplomacyMeetMajors]] |  |
| [[DiplomacyRefusePeace]] | `eActingPlayer [number]`<br/>`eReactingPlayer [number]` |
| [[DiplomacyRelationshipChanged]] | `player1ID [number]`<br/>`player2ID [number]` |
| [[DiplomacySessionClosed]] | `sessionID [number]` |
| [[DiplomacyStatement]] | `eActingPlayer [number]`<br/>`eReactingPlayer [number]`<br/>`values [table]` |
| [[DistrictAddedToMap]] | `playerID [number]`<br/>`districtID [number]`<br/>`cityID [number]`<br/>`iX [number]`<br/>`iY [number]`<br/>`districtType [number]`<br/>`percentComplete [number]` |
| [[DistrictBuildingRestore]] |  |
| [[DistrictBuildProgressChanged]] | `playerID [number]`<br/>`districtID [number]`<br/>`cityID [number]`<br/>`iX [number]`<br/>`iY [number]`<br/>`districtType [number]`<br/>`era [number]`<br/>`civilization [number]`<br/>`percentComplete [number]`<br/>`iAppeal [number]`<br/>`isPillaged [number]` |
| [[DistrictCombatChanged]] | `eventSubType [number]`<br/>`playerID [number]`<br/>`districtID [number]` |
| [[DistrictDamageChanged]] | `playerID [number]`<br/>`districtID [number]`<br/>`damageType [number]`<br/>`newDamage [number]`<br/>`oldDamage [number]` |
| [[DistrictPillaged]] | `owner [number]`<br/>`districtID [number]`<br/>`cityID [number]`<br/>`iX [number]`<br/>`iY [number]`<br/>`districtType [number]`<br/>`percentComplete [number]`<br/>`isPillaged [number]` |
| [[DistrictRemovedFromMap]] | `playerID [number]`<br/>`districtID [number]` |
| [[DistrictUnitsChanged]] | `playerID [number]`<br/>`districtID [number]` |
| [[DistrictVisibilityChanged]] | `playerID [number]`<br/>`districtID [number]`<br/>`eVisibility [number]` |
| [[EmergenciesUpdated]] |  |
| [[EmergencyAvailable]] | `playerTarget [number]`<br/>`emergencyType [number]` |
| [[EmergencyAvailableParticipant]] |  |
| [[EmergencyCompleted]] | `playerID [number]`<br/>`eTargetPlayer [number]`<br/>`iTurn [number]` |
| [[EmergencyCompleteParticipants]] |  |
| [[EmergencyRejected]] |  |
| [[EmergencyStarted]] | `playerID [number]`<br/>`eTargetPlayer [number]`<br/>`iTurn [number]` |
| [[EndTurnBlockingChanged]] | `ePrevEndTurnBlockingType [number]`<br/>`eNewEndTurnBlockingType [number]` |
| [[EndTurnDirty]] |  |
| [[EndWonderReveal]] |  |
| [[EventPopupRequest]] |  |
| [[EventSoundRequest]] |  |
| [[FaithChanged]] | `playerID [number]`<br/>`yield [number]`<br/>`balance [number]` |
| [[FeatureAddedToMap]] |  |
| [[FeatureChanged]] |  |
| [[FeatureRemovedFromMap]] |  |
| [[FeatureVisibilityChanged]] |  |
| [[GameEraChanged]] | `previousEra [number]`<br/>`newEra [number]` |
| [[GameHistoryMomentRecorded]] | `momentIndex [number]`<br/>`iUnknown [number]` |
| [[GoodyHutReward]] | `playerID [number]`<br/>`unitID [number]`<br/>`iUnknown1 [number]`<br/>`iUnknown2 [number]` |
| [[GovDistrictPolicyLocked]] |  |
| [[GovDistrictPolicyUnlocked]] | `player [number]`<br/>`policyType [number]` |
| [[GovernmentChanged]] | `playerID [number]`<br/>`governmentID [number]` |
| [[GovernmentPolicyChanged]] | `playerID [number]`<br/>`policyID [number]` |
| [[GovernmentPolicyObsoleted]] | `ePlayer [number]` |
| [[GovernorAppointed]] | `playerID [number]`<br/>`governorID [number]` |
| [[GovernorAssigned]] | `cityOwner [number]`<br/>`cityID [number]`<br/>`governorOwner [number]`<br/>`governorType [number]` |
| [[GovernorChanged]] | `playerID [number]`<br/>`governorID [number]` |
| [[GovernorEstablished]] |  |
| [[GovernorPointsChanged]] | `player [number]`<br/>`iDelta [number]` |
| [[GovernorPromoted]] | `ePlayer [number]`<br/>`eGovernor [number]`<br/>`ePromotion [number]` |
| [[GreatPeoplePointsChanged]] | `playerID [number]` |
| [[GreatPeopleTimelineChanged]] |  |
| [[GreatWorkCreated]] | `playerID [number]`<br/>`unitID [number]`<br/>`iCityPlotX [number]`<br/>`iCityPlotY [number]`<br/>`buildingID [number]`<br/>`greatWorkID [number]` |
| [[GreatWorkMoved]] | `fromCityOwner [number]`<br/>`fromCityID [number]`<br/>`toCityOwner [number]`<br/>`toCityID [number]`<br/>`buildingID [number]`<br/>`greatWorkType [number]` |
| [[ImprovementActivated]] | `iX [number]`<br/>`iY [number]`<br/>`unitOwner [number]`<br/>`unitID [number]`<br/>`improvementType [number]`<br/>`improvementOwner [number]`<br/>`activationType [number]` |
| [[ImprovementAddedToMap]] | `iX [number]`<br/>`iY [number]`<br/>`eImprovement [number]`<br/>`playerID [number]` |
| [[ImprovementChanged]] | `iX [number]`<br/>`iY [number]`<br/>`improvementType [number]`<br/>`improvementOwner [number]`<br/>`resource [number]`<br/>`isPillaged [boolean]`<br/>`isWorked [boolean]` |
| [[ImprovementOwnershipChanged]] |  |
| [[ImprovementRemovedFromMap]] | `iX [number]`<br/>`iY [number]`<br/>`eOwner [number]` |
| [[ImprovementVisibilityChanged]] | `iX [number]`<br/>`iY [number]`<br/>`eImprovementType [number]`<br/>`eVisibility [number]` |
| [[InfluenceChanged]] |  |
| [[InfluenceGiven]] | `citystateID [number]`<br/>`playerID [number]` |
| [[LevyCounterChanged]] | `originalOwnerID [number]` |
| [[LocalPlayerChanged]] | `localPlayerID [number]`<br/>`prevLocalPlayerID [number]` |
| [[LocalPlayerTurnBegin]] |  |
| [[LocalPlayerTurnEnd]] |  |
| [[LocalPlayerTurnUnready]] |  |
| [[MapYieldsChanged]] |  |
| [[NationalParkAdded]] |  |
| [[NationalParkRemoved]] |  |
| [[NationalParkVisibilityChanged]] |  |
| [[NaturalWonderRevealed]] | `iX [number]`<br/>`iY [number]`<br/>`eFeature [number]`<br/>`bIsFirstToFind [boolean]` |
| [[NotificationActivated]] | `playerID [number]`<br/>`notificationID [number]`<br/>`bActivatedByUser [boolean]` |
| [[NotificationAdded]] | `playerID [number]`<br/>`notificationID [number]` |
| [[NotificationDismissed]] | `playerID [number]`<br/>`notificationID [number]` |
| [[NotificationRefreshRequested]] |  |
| [[ObjectPairing]] | `eSubType [number]`<br/>`parentOwner [number]`<br/>`parentType [number]`<br/>`parentID [number]`<br/>`childOwner [number]`<br/>`childType [number]`<br/>`childID [number]` |
| [[OnAiAdvisorUpdated]] |  |
| [[UnitGreatPersonActivated]] | `unitOwner [number]`<br/>`unitID [number]`<br/>`greatPersonClassID [number]`<br/>`greatPersonIndividualID [number]`<br/>`unitOwner [number]`<br/>`unitID [number]`<br/>`greatPersonClassID [number]`<br/>`greatPersonIndividualID [number]` |
| [[PantheonFounded]] | `ePlayer [number]` |
| [[PhaseBegin]] |  |
| [[PhaseEnd]] |  |
| [[PlayerAgeChanged]] | `playerID [number]` |
| [[PlayerBordersChanged]] |  |
| [[PlayerDarkAgeChanged]] | `playerID [number]` |
| [[PlayerDefeat]] | `playerID [number]`<br/>`defeatType [number]`<br/>`eventID [number]` |
| [[PlayerDestroyed]] |  |
| [[PlayerEraChanged]] | `playerID [number]`<br/>`eraID [number]` |
| [[PlayerEraScoreChanged]] | `playerID [number]`<br/>`amountAwarded [number]` |
| [[PlayerEraTransitionBegins]] | `playerID [number]` |
| [[PlayerOperationComplete]] |  |
| [[PlayerResourceChanged]] | `ownerPlayerID [number]`<br/>`resourceTypeID [number]` |
| [[PlayerRestored]] |  |
| [[PlayerRevived]] |  |
| [[PlayerTurnActivated]] | `playerID [number]`<br/>`bIsFirstTime [boolean]` |
| [[PlayerTurnDeactivated]] | `playerID [number]` |
| [[PlayerVictory]] |  |
| [[PlotAppealChanged]] |  |
| [[PlotMarkerChanged]] | `iX [number]`<br/>`iY [number]` |
| [[PlotVisibilityChanged]] | `iX [number]`<br/>`iY [number]`<br/>`visibilityType [number]` |
| [[PlotYieldChanged]] | `iX [number]`<br/>`iY [number]` |
| [[QuestChanged]] | `CityStateID [number]`<br/>`CompletedQuestPlayerID [number]` |
| [[QueueFlushed]] |  |
| [[ReligionFounded]] | `playerID [number]`<br/>`religionID [number]` |
| [[RemotePlayerTurnBegin]] |  |
| [[RemotePlayerTurnEnd]] |  |
| [[RemotePlayerTurnUnready]] |  |
| [[ResearchChanged]] | `ePlayer [number]`<br/>`eTech [number]` |
| [[ResearchCompleted]] | `ePlayer [number]`<br/>`eTech [number]` |
| [[ResearchQueueChanged]] | `ePlayer [number]`<br/>`eTech [number]` |
| [[ResearchYieldChanged]] | `ePlayer [number]` |
| [[ResourceAddedToMap]] | `iX [number]`<br/>`iY [number]`<br/>`resourceType [number]` |
| [[ResourceChanged]] |  |
| [[ResourceRemovedFromMap]] | `iX [number]`<br/>`iY [number]`<br/>`resourceType [number]` |
| [[ResourceVisibilityChanged]] | `iX [number]`<br/>`iY [number]`<br/>`resourceType [number]`<br/>`visibilityType [number]` |
| [[RiverAddedToMap]] |  |
| [[RiverRemovedFromMap]] |  |
| [[RouteAddedToMap]] |  |
| [[RouteChanged]] | `iX [number]`<br/>`iY [number]` |
| [[RouteRemovedFromMap]] |  |
| [[RouteVisibilityChanged]] |  |
| [[SpyAdded]] | `spyOwner [number]`<br/>`spyUnitID [number]` |
| [[SpyMissionCompleted]] | `playerID [number]`<br/>`missionID [number]` |
| [[SpyMissionUpdated]] |  |
| [[SpyRemoved]] | `spyOwner [number]`<br/>`counterSpyPlayer [number]` |
| [[SpyUpdated]] |  |
| [[StatusMessage]] |  |
| [[SystemUpdateUI]] | `type [number]`<br/>`tag [string]`<br/>`iData1 [number]`<br/>`iData2 [number]`<br/>`strData1 [string]` |
| [[TeamVictory]] |  |
| [[TechBoostTriggered]] | `playerID [number]`<br/>`iTechBoosted [number]`<br/>`iUnknownA [number]`<br/>`iUnknownB [number]` |
| [[TerrainTypeChanged]] |  |
| [[TradeRouteActivityChanged]] | `playerID [number]`<br/>`OriginPlayerID [number]`<br/>`OriginCityID [number]`<br/>`TargetPlayerID [number]`<br/>`TargetCityID [number]` |
| [[TradeRouteAddedToMap]] | `playerID [number]`<br/>`iX [number]`<br/>`iY [number]` |
| [[TradeRouteCapacityChanged]] | `playerID [number]` |
| [[TradeRouteRangeChanged]] |  |
| [[TradeRouteRemovedFromMap]] | `playerID [number]`<br/>`iX [number]`<br/>`iY [number]` |
| [[TreasuryChanged]] | `playerID [number]`<br/>`yield [number]`<br/>`balance [number]` |
| [[TurnBegin]] |  |
| [[TurnEnd]] |  |
| [[UnitAbilityGained]] | `playerID [number]`<br/>`unitID [number]`<br/>`eAbilityType [number]` |
| [[UnitActivate]] |  |
| [[UnitActivityChanged]] | `playerID [number]`<br/>`unitID [number]`<br/>`eActivityType [number]` |
| [[UnitAirlifted]] |  |
| [[UnitArtifactChanged]] | `playerID [number]`<br/>`unitID [number]` |
| [[UnitCaptured]] | `currentUnitOwner [number]`<br/>`unitID [number]`<br/>`owningPlayer [number]`<br/>`capturingPlayer [number]` |
| [[UnitChargesChanged]] | `playerID [number]`<br/>`unitID [number]`<br/>`newCharges [number]`<br/>`oldCharges [number]` |
| [[UnitCommandStarted]] | `playerID [number]`<br/>`unitID [number]`<br/>`hCommand [number]`<br/>`iData1 [number]` |
| [[UnitDamageChanged]] | `PlayerID [number]`<br/>`UnitID [number]`<br/>`newDamage [number]`<br/>`prevDamage [number]` |
| [[UnitEmbarkedStateChanged]] | `playerID [number]`<br/>`unitID [number]`<br/>`bEmbarkedState [boolean]` |
| [[UnitEnterFormation]] | `firstUnitOwner [number]`<br/>`firstUnitID [number]`<br/>`secondUnitOwner [number]`<br/>`secondUnitID [number]` |
| [[UnitExitFormation]] | `firstUnitOwner [number]`<br/>`firstUnitID [number]`<br/>`secondUnitOwner [number]`<br/>`secondUnitID [number]` |
| [[UnitExperienceChanged]] |  |
| [[UnitFormArmy]] | `playerID [number]`<br/>`unitID [number]` |
| [[UnitFormationChanged]] |  |
| [[UnitFormCorps]] | `playerID [number]`<br/>`unitID [number]` |
| [[UnitFortificationChanged]] | `playerID [number]`<br/>`unitID [number]` |
| [[UnitGreatPersonChanged]] |  |
| [[UnitGreatPersonCreated]] | `playerID [number]`<br/>`unitID [number]`<br/>`greatPersonClassID [number]`<br/>`greatPersonIndividualID [number]` |
| [[UnitKilledInCombat]] | `killedPlayerID [number]`<br/>`killedUnitID [number]`<br/>`playerID [number]`<br/>`unitID [number]` |
| [[UnitMoveComplete]] | `playerID [number]`<br/>`unitID [number]`<br/>`iX [number]`<br/>`iY [number]` |
| [[UnitMoved]] | `playerID [number]`<br/>`unitID [number]`<br/>`iX [number]`<br/>`iY [number]`<br/>`locallyVisible`<br/>`stateChange` |
| [[UnitMovementPointsChanged]] | `playerID [number]`<br/>`unitID [number]`<br/>`MovementPoints [number]` |
| [[UnitMovementPointsCleared]] | `playerID [number]`<br/>`unitID [number]` |
| [[UnitMovementPointsRestored]] | `playerID [number]`<br/>`unitID [number]`<br/>`MovementPoints [number]` |
| [[UnitOperationAdded]] | `playerID [number]`<br/>`unitID [number]`<br/>`iUnknown [number]`<br/>`hOperation [number]` |
| [[UnitOperationDeactivated]] | `playerID [number]`<br/>`unitID [number]`<br/>`hOperation [number]`<br/>`iData1 [number]` |
| [[UnitOperationSegmentComplete]] | `playerID [number]`<br/>`unitID [number]`<br/>`hCommand [number]`<br/>`iData1 [number]` |
| [[UnitOperationStarted]] | `ownerID [number]`<br/>`unitID [number]`<br/>`operationID [number]` |
| [[UnitOperationsCleared]] | `playerID [number]`<br/>`unitID [number]`<br/>`hCommand [number]`<br/>`iData1 [number]` |
| [[UnitParadropped]] |  |
| [[UnitPromoted]] | `playerID [number]`<br/>`unitID [number]` |
| [[UnitPromotionAvailable]] | `playerID [number]`<br/>`unitID [number]`<br/>`promotionID [number]` |
| [[UnitRemovedFromMap]] | `playerID [number]`<br/>`unitID [number]` |
| [[UnitTeleported]] | `playerID [number]`<br/>`unitID [number]`<br/>`iX [number]`<br/>`iY [number]` |
| [[UnitTradeChanged]] | `playerID [number]`<br/>`unitID [number]` |
| [[UnitUpgraded]] | `playerID [number]`<br/>`unitID [number]` |
| [[UnitVisibilityChanged]] | `playerID [number]`<br/>`unitID [number]` |
| [[WMDCountChanged]] | `playerID [number]`<br/>`eWMD [number]` |
| [[WMDDetonated]] |  |
| [[WMDFalloutChanged]] |  |
| [[WMDFalloutVisibilityChanged]] |  |
| [[WonderCompleted]] | `iX [number]`<br/>`iY [number]`<br/>`buildingIndex [number]`<br/>`playerIndex [number]`<br/>`cityID [number]`<br/>`iPercentComplete [number]`<br/>`iUnknown [number]` |
| [[WorldTextMessage]] | `messageType [number]`<br/>`delay [number]`<br/>`iX [number]`<br/>`iY [number]`<br/>`text [number]` |

## Static Methods
Methods are functions that belong to an object. Static methods are invoked through a **dot**, as in `Events.SomeMethod(<args>)`. When a dot is used the caller object is not implicitly provided as the first argument.