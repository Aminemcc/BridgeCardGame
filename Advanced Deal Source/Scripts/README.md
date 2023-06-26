# Documentation
This documentation is for settings available in each script

## List Available Scripts
- [1C Precision](#1c-precision)
- [1D Precision]
- [1NT]
- [2C Precision]
- [2M (2H/S)]

### 1C Precision
[Link to File](./1C.txt)
Here is the script
```
//----- Open 1C -----//
//1C = 16-17 HCP Unbalance / 18+ any dist

//---Setting---//

//Player who can receive opening card
northOpen = 1
eastOpen = 1
southOpen = 1
westOpen = 1

//Opener settings {0 : off, 1 : on}
minOpenHCP = 16
maxOpenHCP = 40
//5332 5M considered unbalance
balOpener = 1
unbalOpener = 1


//Minimum HCP 1C Opener & Partner
min_hcp = 21
max_hcp = 40

//--responder--//
respMinHCP = 0
respMaxHCP = 20

//0 : Off, 1 : On
resp4441 = 1
//any 5 only cards
respAny5 = 1
//any 6+ suiter
respAny6Up = 1
//Balanced card 4432 / 4333
respBal = 1
//any two suiter card (5+5+)
resp2Suiter = 1

//--responder--//




//quality one of opponents card (0 : off, 1 : on)
quality_set = 1
//interval is : [0-3000] quality of normal opening around 1200
minQuality = 0
maxQuality = 1100
//balanced card and HCP between opps (0 : off, 1 : on)
balancedOpps = 1

//---Setting Done---//


//HCP
northHCP = minOpenHCP <= hcp(north) && hcp(north) <= maxOpenHCP
northHCP_16_17 = 16 <= hcp(north) && hcp(north) <= 17
northHCP_18 = hcp(north) >= 18

eastHCP = minOpenHCP <= hcp(east) && hcp(east) <= maxOpenHCP
eastHCP_16_17 = 16 <= hcp(east) && hcp(east) <= 17
eastHCP_18 = hcp(east) >= 18

southHCP = minOpenHCP <= hcp(south) && hcp(south) <= maxOpenHCP
southHCP_16_17 = 16 <= hcp(south) && hcp(south) <= 17
southHCP_18 = hcp(south) >= 18

westHCP = minOpenHCP <= hcp(west) && hcp(west) <= maxOpenHCP
westHCP_16_17 = 16 <= hcp(west) && hcp(west) <= 17
westHCP_18 = hcp(west) >= 18


//Total HCP NS & EW
hcpNS = min_hcp <= ( hcp(north) + hcp(south) ) && ( hcp(north) + hcp(south) ) <= max_hcp
hcpEW = min_hcp <= ( hcp(east) + hcp(west) ) && ( hcp(east) + hcp(west) ) <= max_hcp

//Distribusi
northBal = shape(north, any 4432 + any 4333 + any 5332 - 5xxx - x5xx)
northDist = ( (northHCP_16_17 && !northBal && unbalOpener) || 
    ( northHCP_18 && ( (northBal && balOpener)  || (!northBal && unbalOpener) ) ) ) && northHCP && northOpen

eastBal = shape(east, any 4432 + any 4333 + any 5332 - 5xxx - x5xx)
eastDist = ( (eastHCP_16_17 && !eastBal && unbalOpener) || 
    ( eastHCP_18 && ( (eastBal && balOpener)  || (!eastBal && unbalOpener) ) ) ) && eastHCP && eastOpen

southBal = shape(south, any 4432 + any 4333 + any 5332 - 5xxx - x5xx)
southDist = ( (southHCP_16_17 && !southBal && unbalOpener) || 
    ( southHCP_18 && ( (southBal && balOpener)  || (!southBal && unbalOpener) ) ) ) && southHCP && southOpen

westBal = shape(west, any 4432 + any 4333 + any 5332 - 5xxx - x5xx)
westDist = ( (westHCP_16_17 && !westBal && unbalOpener) || 
    ( westHCP_18 && ( (westBal && balOpener) || (!westBal && unbalOpener) ) ) ) && westHCP && westOpen


//responder
northResHCP = respMinHCP <= hcp(north) && hcp(north) <= respMaxHCP
eastResHCP = respMinHCP <= hcp(east) && hcp(east) <= respMaxHCP
southResHCP = respMinHCP <= hcp(south) && hcp(south) <= respMaxHCP
westResHCP = respMinHCP <= hcp(west) && hcp(west) <= respMaxHCP

responderHCP = (northDist && southResHCP) || (eastDist && westResHCP) ||
    (southDist && northResHCP) || (westDist && eastResHCP)

northRes4441 = shape(north, any 4441)
northRes6AnyUp = ( spades(north) >= 6 || hearts(north) >= 6 || diamonds(north) >= 6 || clubs(north) >= 6 ) && 
    shape(north, xxxx - any 65xx - any 75xx - any 7600)
northRes2Suiter = shape(north, any 55xx + any 65xx + any 6610 + any 7600)
northResBal = shape(north, any 4432 + any 4333)
northRes5Any = shape(north, any 5xxx) && !northRes2Suiter && !northRes6AnyUp
northResponses = ( ( northRes4441 && resp4441 ) || ( northRes6AnyUp && respAny6Up ) || ( northRes2Suiter && resp2Suiter ) ||
    ( northResBal && respBal ) || ( northRes5Any && respAny5 ) )

eastRes4441 = shape(east, any 4441)
eastRes6AnyUp = ( spades(east) >= 6 || hearts(east) >= 6 || diamonds(east) >= 6 || clubs(east) >= 6 ) && 
    shape(east, xxxx - any 65xx - any 75xx - any 7600)
eastRes2Suiter = shape(east, any 55xx + any 65xx + any 6610 + any 7600)
eastResBal = shape(east, any 4432 + any 4333)
eastRes5Any = shape(east, any 5xxx) && !eastRes2Suiter && !eastRes6AnyUp
eastResponses = ( ( eastRes4441 && resp4441 ) || ( eastRes6AnyUp && respAny6Up ) || ( eastRes2Suiter && resp2Suiter ) ||
    ( eastResBal && respBal ) || ( eastRes5Any && respAny5 ) )

southRes4441 = shape(south, any 4441)
southRes6AnyUp = ( spades(south) >= 6 || hearts(south) >= 6 || diamonds(south) >= 6 || clubs(south) >= 6 ) && 
    shape(south, xxxx - any 65xx - any 75xx - any 7600)
southRes2Suiter = shape(south, any 55xx + any 65xx + any 6610 + any 7600)
southResBal = shape(south, any 4432 + any 4333)
southRes5Any = shape(south, any 5xxx) && !southRes2Suiter && !southRes6AnyUp
southResponses = ( ( southRes4441 && resp4441 ) || ( southRes6AnyUp && respAny6Up ) || ( southRes2Suiter && resp2Suiter ) ||
    ( southResBal && respBal ) || ( southRes5Any && respAny5 ) )

westRes4441 = shape(west, any 4441)
westRes6AnyUp = ( spades(west) >= 6 || hearts(west) >= 6 || diamonds(west) >= 6 || clubs(west) >= 6 ) && 
    shape(west, xxxx - any 65xx - any 75xx - any 7600)
westRes2Suiter = shape(west, any 55xx + any 65xx + any 6610 + any 7600)
westResBal = shape(west, any 4432 + any 4333)
westRes5Any = shape(west, any 5xxx) && !westRes2Suiter && !westRes6AnyUp
westResponses = ( ( westRes4441 && resp4441 ) || ( westRes6AnyUp && respAny6Up ) || ( westRes2Suiter && resp2Suiter ) ||
    ( westResBal && respBal ) || ( westRes5Any && respAny5 ) )


responderDist = (northDist && southResponses) || (eastDist && westResponses) || (southDist && northResponses) || (westDist && eastResponses)

//Balanced opponents
balancedOpps_on = ( shape(east, any 4432 + any 4333) && shape(west, any 4432 + 4333) ) || 
	( shape(north, any 4432 + any 4333) && shape(south, any 4432 + 4333) )
balancedHCP = -1 <= (hcp(east) - hcp(west)) && (hcp(east) - hcp(west)) <= 1

//Quality opponents
cNorth = minQuality <= cccc(north) && cccc(north) <= maxQuality && !northDist && !southDist
cEast = minQuality <= cccc(east) && cccc(east) <= maxQuality && !eastDist && !westDist
cSouth = minQuality <= cccc(south) && cccc(south) <= maxQuality && !northDist && !southDist
cWest = minQuality <= cccc(west) && cccc(west) <= maxQuality && !eastDist && !westDist

//Wrap everything up
conditionOpps = ( !balancedOpps || (balancedOpps_on && balancedHCP) ) && ( !quality_set || (cNorth || cSouth) || (cEast || cWest) )

conditionOpener = ( (northDist || southDist) && hcpNS ) || ( (eastDist || westDist) && hcpEW )

conditionResponder = responderHCP && responderDist

condition conditionOpener && conditionOpps && conditionResponder

//----- ..... -----//
```
