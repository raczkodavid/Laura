#1. feladat
sor = None
oszlop = None
adatok = []

with open(f'melyseg.txt','r', encoding='utf-8') as file:
    for index, i in enumerate(file):
        if index > 1:
            i = list(map(int, i.strip().split()))
            adatok.append(i)
        else:
            i = i.strip()
            if index == 0:
                sor = int(i)
            elif index == 1:
                oszlop = int(i)

#2. feladat
print(f'2. feladat')
valasztott_sorid = int(input(f'A mérés sorának azonosítója= '))
valasztott_oszlopid = int(input(f'A mérés oszlopának azonosítója= '))
print(f'A mért mélység az adott helyen {adatok[valasztott_sorid-1][valasztott_oszlopid-1]} dm')

print(f'3. feladat')
nem_nulla = 0
melysegek_osszege = 0
for x in adatok:
    for y in x:
        if y != 0:
            nem_nulla += 1
            melysegek_osszege += y

print(F'A tó felszíne: {nem_nulla} m2, átlagos mélysége: {round(melysegek_osszege/nem_nulla/10,2)} m')
            
print(f'4. feladat')
legnagyobb = 0
for x in adatok:
    if max(x) > legnagyobb:
        legnagyobb = max(x)

print(f'A tó legnagyobb mélysége: {legnagyobb} dm ')
print(f'A legmélyebb helyek sor-oszlop koordinátái:')
for index, x in enumerate(adatok):
    if legnagyobb in x:
        print(f'({index+1}; {x.index(legnagyobb)+1})\t',end='')

print(F'5. feladat')
teljes_kerulet = 0
for i in range(sor):
    for x in range(oszlop):
        if 0 < i < sor - 1 and 0 < x < oszlop - 1:
            if adatok[i][x] != 0:
                kerulet = 4
                #felső cella vizsgálat
                if adatok[i+1][x] != 0:
                    kerulet -= 1
                #alsó cella vizsgálat
                if adatok[i-1][x] != 0:
                    kerulet -= 1
                #bal cella vizsgálat
                if adatok[i][x-1] != 0:
                    kerulet -= 1
                #jobb cella vizsgálat
                if adatok[i][x+1] != 0:
                    kerulet -= 1
                
                teljes_kerulet += kerulet

print(f'A tó partvonala {teljes_kerulet} m hosszú')

bekert_oszlop_id = int(input(f'A vizsgált szelvény oszlopának azonosítója='))
ujfile = open(f'diagram.txt','w')

for i in range(sor):
    if i < 9:
        print(f'0{i+1} {int(round(adatok[i][bekert_oszlop_id-1],-1)/10)*"*"}', file=ujfile)
    else:
        print(f'{i+1} {int(round(adatok[i][bekert_oszlop_id-1],-1)/10)*"*"}', file=ujfile)

ujfile.close()
