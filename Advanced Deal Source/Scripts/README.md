# Documentation
This documentation is for settings available in each script.<br>
Copy and paste the script from the file / full script to use the script!<br>

## List Available Scripts
- [1C Precision](#1c-precision)
- [1D Precision]
- [1NT]
- [2C Precision]
- [2M (2H/S)]

### 1C Precision
[Link to Full Script](./1C.txt)<br>

- Player who can receive opening cards
```
//Player who can receive opening card
northOpen = 1
eastOpen = 1
southOpen = 1
westOpen = 1
```
Atur menjadi nilai 0 agar player tersebut tidak mendapatkan kartu opening <br>

- Opening HCP
```
//Opener settings
minOpenHCP = 16
maxOpenHCP = 36
```

- Balance Setting
```
//5332 5M considered unbalance  {0 : off, 1 : on}
balOpener = 1
unbalOpener = 1
```
Jika ingin fokus ke 1C-any-1NT, bisa nonaktifkan unbalOpener.<br>
5332 dengan 5 lembar Major(H/S) dianggap sebagai unbalance.<br>

- Minimum total HCP
```
//Minimum HCP 1C Opener & Partner
min_hcp = 21
max_hcp = 40
```
Jika min_hcp 24/25++, maka pasti game distribusi yang dihasilkan.<br>

- Responder settings
```
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
```
- respMinHCP & respMaxHCP
    - Mengatur interval HCP responder
- 