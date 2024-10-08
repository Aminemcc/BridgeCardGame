# North Based Scripts

Scripts in this folder is focusing on intense bidding NS.<br>
in hope to explore and master a specific sequence or situation.<br>

Script akan terdapat beberapa jenis setting yang bisa diubah seperti:<br>
- Minimum & Maximum HCP
- Distribusi tertentu dengan *0 : off* dan *1 : on*
    - 0 berarti distribusi tidak akan pernah dihasilkan
    - 1 berarti distribusi bisa dihasilkan
    - Jika ingin selalu distribusi spesifik, 0-kan semua kecuali distribusi yang diinginkan
    - Jika terjadi error setelah setting diubah, karena kartu tidak mungkin dibuat
        - Balance dengan mempunyai singleton/void
        - HCP yang tidak bisa dihasilkan
        - Kartu dengan quality yang tidak bisa dihasilkan
- Minimum & Maximum Quality
    - Quality merupakan nilai kualitas dari suatu kartu berdasarkan HCP dan distribusi
    - untuk opening 1C/D/H/S Standard, biasanya kualitas kartu 1200-1500, bisa diluar rentang yang disebutkan
    - Maximum Quality : 3000

## Script List
- [1NT](#1NT)



## 1NT
[Back](#script-list)<br>
Script 1NT mempunyai beberapa setting yang bisa diubah.<br>

```
//--Opener Setting Start--//
minHcpOpen = 15
maxHcpOpen = 17

openNo5 = 1
open5M = 1
open5m = 1
semiBal = 0
//--Opener Setting End--//
```
| Setting   | Description                         | Value |
|-----------|-------------------------------------|-------|
| minHcpOpen| Minimum HCP Opener 1NT              | HCP |
| maxHcpOpen| Maximum HCP Opener 1NT             | HCP |
| openNo5   | any 4432, any 4333                 | 0/1 |
| open5M    | any 5332 with 5M                   | 0/1 |
| open5m    | any 5332 with 5m                   | 0/1 |
| semiBal   | any 5422                           | 0/1 |

```
//--North South Setting Start--//
minTotalHcp = 15
maxTotalHcp = 40
minFitM = 0
minFitm = 0
//--North South Setting End--//
```
| Setting | Description | Value |
|---------|-------------|-------|
| minTotalHcp | Minimum Total HCP North-South | HCP |
| MaxTotalHcp | Maximum Total HCP North-South | HCP |
| minFitM | Minimum fit Major north-South | 0-13 |
| minFitm | Minimum fit minor north-South | 0-13 |

```
//--Responder Setting Start--//
minHcpRes = 0
maxHcpRes = 40

alwaysVoid = 0
resBalNo5 = 1
res3suiter = 1
res5M = 1
res54M = 1
res6M = 1
res7Mup = 1
res5m = 1
res54m = 1
res6m = 1
res7mup = 1
resMM = 1
resmm = 1
resMm = 1
//--Responder Setting End--//
```
| Setting     | Description                            | Value |
|-------------|----------------------------------------|-------|
| minHcpRes | Minimum HCP Responder (South) | HCP |
| maxHcpRes | Maximum HCP Responder (South) | HCP |
| alwaysVoid | **Must** have a void | 0/1 |
| resBalNo5   | any 4432, any 4333                    | 0/1 |
| res3suiter  | any 4441                              | 0/1 |
| res5M       | any 5M with no 4OM and no 5+ other Suit | 0/1 |
| res54M | any 54MM | 0/1 |
| res6M | any 6M with no 5+ other suit | 0/1 |
| res7Mup | any 7+M with no 5+ other suit| 0/1 |
| res5m | any 5m with no 4Om and no 5+ other Suit | 0/1 |
| res54m | any 54m | 0/1 |
| res6m | any 6m with no 5+ other suit | 0/1 |
| res7mup | any 7+m with no 5+ other suit | 0/1 |
| resMM | any 5+5+MM | 0/1 |
| resmm | any 5+5+mm | 0/1 |
| resMm | any 5+M + 5+m | 0/1 |

```
//--Overcall Setting Start--//
ovcSet = 1
minHcpOvc = 8
maxHcpOvc = 11
minFitOvc = 9

ovcElse = 0
ovc6M = 1
ovcMM = 1
ovcmm = 1
ovcMm = 1
ovc7x = 1
ovc8xup = 1
//--Overcall Setting End--//
```
| Setting | Description | Value |
|---------|-------------|-------|
| ovcSet | Apakah Kartu pelaku overcall (East) diatur / tidak | 0/1 |
| minHcpOvc | Minimum HCP Overcall (East) | HCP |
| maxHcpOvc | Maximum HCP Overcall (East) | HCP |
| minFitOvc | Minimum fit East-West di salah satu suit | 0-11 |
| ovcElse | Kartu selain distribusi yang disebutkan di bawah | 0/1 |
| ovc6M | 6M with no 5+ Other Suit | 0/1 |
| ovcMM | 5+5+MM | 0/1 |
| ovcmm | 5+5+mm | 0/1 |
| ovcMm | 5+M + 5+m | 0/1 |
| ovc7x | any 7 cards | 0/1 |
| ovc8xup | any 8+cards | 0/1 |