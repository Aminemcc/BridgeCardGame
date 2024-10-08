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
| Setting   | Description                         |
|-----------|-------------------------------------|
| minHcpOpen| Minimum HCP Opener 1NT              |
| maxHcpOpen| Maximum HCP Opener 1NT             |
| openNo5   | any 4432, any 4333                 |
| open5M    | any 5332 with 5M                   |
| open5m    | any 5332 with 5m                   |
| semiBal   | any 5422                           |

```
//--Responder Setting Start--//
minHcpRes = 0
maxHcpRes = 20

resBalNo5 = 0
res3suiter = 0
res5M = 1
res54M = 0
res6M = 0
res7Mup = 0
res5m = 0
res54m = 0
res6m = 0
res7mup = 0
resMM = 0
resmm = 0
resMm = 0

alwaysVoid = 0
//--Responder Setting End--//
```
| Setting     | Description                            |
|-------------|----------------------------------------|
| resBalNo5   | any 4432, any 4333                    |
| res3suiter  | any 4441                              |
| res5M       | any 5M with no 4OM and no 5+ other Suit |
| res54M | any 54MM |
| res6M | any 6M with no 5+ other suit |
| res7Mup | any 7+M with no 5+ other suit|
| res5m | any 5m with no 4Om and no 5+ other Suit |
| res54m | any 54m |
| res6m | any 6m with no 5+ other suit |
| res7mup | any 7+m with no 5+ other suit |
| resMM | any 5+5+MM |
| resmm | any 5+5+mm |
| resMm | any 5+M + 5+m |
| alwaysVoid | **Must** have a void |