```
//----- Open 1NT -----//
//1NT = 15-17 Balance
//Balance : 4333, 4432, 5332

//deklarasi variable yang bisa dihapus
conditionEW = 1
northDist = 1
totalHCP = 1
balancedOpps = 1
balancedHCP = 1
//---done---//

//Rentang HCP South
southHCP = 15 <= hcp(south) && hcp(south) <= 17

//Distribusi South
southDist = shape(south, any 4432 + any 4333 + any 5332)

//Jika ingin kartunya mengarah game terus, 
//atur ini ke ">= 24 atau 25"
totalHCP = (hcp(south) + hcp(north)) >= 21

//Distribusi North, sementara set true saja
northDist = 1

//Supaya kemungkinan musuh melakukan bid sangat kecil
balancedOpps = shape(east, any 4432 + any 4333) && shape(west, any 4432 + 4333)
balancedHCP = -1 <= (hcp(east) - hcp(west)) && (hcp(east) - hcp(west)) <= 1

//Kondisi East - West
conditionEW = balancedOpps && balancedHCP

//Kondisi South - North
conditionSN = southHCP && southDist && totalHCP && northDist

condition conditionEW && conditionSN

//----- ..... -----//
```