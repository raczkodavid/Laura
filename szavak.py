#1. feladat
bekert_szo1 = input(f'1. feladat Adjon meg egy szót: ')
maganhangzok = ['a', 'e', 'i', 'o', 'u']
van_benne = False

for x in bekert_szo1:
    if x in maganhangzok:
        van_benne = True

if van_benne:
    print(f'Van benne magánhangzó.')
else:
    print(f'Nincs benne magánhangzó.')
#-------------------------------------------------------------------------------------------------------------------------
print(f'\n2. feladat')
with open(f'szoveg.txt','r',encoding='UTF-8') as file:
    adatok = [i.rstrip() for i in file]

legtobb_karakter = sorted(list(map(len, adatok)), reverse=True)[0]
leghosszabb_szo = None

for x in adatok:
    if len(x) == legtobb_karakter:
        leghosszabb_szo = x
        break

print(f'Az állomány leghosszabb szava {leghosszabb_szo}, ami {legtobb_karakter} karakterből áll.')
#-------------------------------------------------------------------------------------------------------------------------
print(f'\n3. feladat')
talalat = 0
for x in adatok:
    mg = 0
    egyeb = 0
    for y in x:
        if y in maganhangzok:
            mg += 1
        else:
            egyeb += 1
    if mg > egyeb:
        talalat += 1
        print(x, end=' ')

print(f'\n{talalat}/{len(adatok)} : {round(talalat/len(adatok) * 100, 2)}%')
#-------------------------------------------------------------------------------------------------------------------------
print(f'\n4. feladat')
otkarakteres = [x for x in adatok if len(x) == 5]
haromkarakteres_reszlet = input(f'Adjon meg egy háromkarakteres szórészletet: ')

for x in otkarakteres:
    if x[1:4] == haromkarakteres_reszlet:
        print(x, end=' ')
#-------------------------------------------------------------------------------------------------------------------------
print(f'\n\n5. feladat - letra.txt elkészítése')
ujfile = open(f'letra.txt', 'w')

harombetusok = set(x[1:4] for x in otkarakteres)
harombetus_talalatok = []

for x in harombetusok:
    db = 0
    for y in otkarakteres:
        if y[1:4] == x:
            db += 1
    harombetus_talalatok.append(db)

seged = list(zip(harombetusok, harombetus_talalatok))

for x in seged:
    if x[1] > 1:
        for y in otkarakteres:
            if y[1:4] == x[0]:
                print(y, file=ujfile)
        print(file=ujfile)

ujfile.close()
#-------------------------------------------------------------------------------------------------------------------------
