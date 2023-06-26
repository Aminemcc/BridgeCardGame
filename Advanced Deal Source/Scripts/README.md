# Documentation
This documentation is for settings available in each script.<br>
Copy and paste the script from the file / full script to use the script!<br>

## List Available Scripts
- [1C Precision](#1c-precision)
- [1D Precision]
- [1NT]
- [2C Precision]
- [2M (2H/S)]

## 1C Precision
[Back](#list-available-scripts)<br>
[Link to Script](./1C.txt)<br>
Berikut Penjelasan pengaturan yang bisa diubah ubah di dalam script :<br>
<br>

Player who can receive opening cards.<br>
- Atur menjadi nilai 0 agar player tersebut tidak mendapatkan kartu opening <br>
```
//Player who can receive opening card
northOpen = 1
eastOpen = 1
southOpen = 1
westOpen = 1
```

Opening HCP
- Jika minOpenHCP < 16, maka tidak akan menghasilkan distribusi 1C
```
//Opener settings
minOpenHCP = 16
maxOpenHCP = 40
```

Balance Setting<br>
- Jika ingin fokus ke 1C-any-1NT, bisa nonaktifkan unbalOpener.<br>
- 5332 dengan 5 lembar Major(H/S) dianggap sebagai unbalance.<br>
```
//5332 5M considered unbalance  {0 : off, 1 : on}
balOpener = 1
unbalOpener = 1
```

Minimum total HCP<br>
- Jika min_hcp 24/25++, maka pasti game distribusi yang dihasilkan.<br>
```
//Minimum HCP 1C Opener & Partner
min_hcp = 21
max_hcp = 40
```


Responder settings<br>
- respMinHCP & respMaxHCP : Mengatur interval HCP responder
- resp4441 : Responder tangan three suiter
- respAny5 : Responder tangan 5 lembar any suit
- respAny6UP : Responder tangan 6+ lembar any suit
- respBal : Responder tangan any 4432 / any 4333
- resp2Suiter : Responder tangan any 2 suiter (5+5+)

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

Opponents Settings<br>
- Ini dibuat agar musuh tidak melakukan overcall dengan membuat kartunya tidak bagus
- Settings
    - quality_set : Mengatur Kualitas kartu musuh, average opening quality = 1200
        - minQuality
        - maxQuality : Maksimum quality adalah 3000
    - balancedOpps : Mengatur agar kartu musuh balance, sehingga jarang ovc 8-11 HCP
- Jika ingin musuh overcall ubah
    - quality_set = 0
    - balancedOpps = 0
```

//quality one of opponents card (0 : off, 1 : on)
quality_set = 1
//interval is : [0-3000] quality of normal opening around 1200
minQuality = 0
maxQuality = 1100
//balanced card and HCP between opps (0 : off, 1 : on)
balancedOpps = 1
```

## 1D Precision
[Back](#list-available-scripts)<br>
[Link to Script](./1D.txt)<br>
Berikut Penjelasan pengaturan yang bisa diubah ubah di dalam script :<br>
<br>

```
//----- Open 1D -----//
//1D = 12-15 HCP 2+D
//Can't open 1M/1NT/2C
```

Kartu Balance
- Ubah menjadi 0 jika tidak ingin kartu balance
```
Balanced_set = 1
```

Minimum total HCP
- Jika 24/25+, maka distribusi pasti game+
```
//Minimum HCP 2M Opener & Partner
min_hcp = 21
max_hcp = 40
```

Player who can receive opening cards.<br>
- Atur menjadi nilai 0 agar player tersebut tidak mendapatkan kartu opening <br>
```
//Player who can receive opening card
northOpen = 1
eastOpen = 1
southOpen = 1
westOpen = 1
```

Opponents Settings<br>
- Ini dibuat agar musuh tidak melakukan overcall dengan membuat kartunya tidak bagus
- Settings
    - quality_set : Mengatur Kualitas kartu musuh, average opening quality = 1200
        - minQuality
        - maxQuality : Maksimum quality adalah 3000
    - balancedOpps : Mengatur agar kartu musuh balance, sehingga jarang ovc 8-11 HCP
- Jika ingin musuh overcall ubah
    - quality_set = 0
    - balancedOpps = 0
```

//quality one of opponents card (0 : off, 1 : on)
quality_set = 1
//interval is : [0-3000] quality of normal opening around 1200
minQuality = 0
maxQuality = 1100
//balanced card and HCP between opps (0 : off, 1 : on)
balancedOpps = 1
```

## 1NT