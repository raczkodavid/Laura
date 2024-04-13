osszes_adat = []
ideiglenes = []

with open(f'kep.txt','r',encoding='utf-8') as file:
    for x in file:
        x = list(map(int, x.strip().split()))
        
        if len(ideiglenes) != 50:
            ideiglenes.append(x)
        
        elif len(ideiglenes) == 50:
            osszes_adat.append(ideiglenes)
            ideiglenes = []
            ideiglenes.append(x)

osszes_adat.append(ideiglenes)

bekert_rgb_kod = input(f'2. feladat: Adjon meg egy tetszőleges RGB-kódot! ')
bekert_rgb_kod = list(map(int, bekert_rgb_kod.strip().split()))

megtalalhato = False

for x in osszes_adat:
    if bekert_rgb_kod in x:
        megtalalhato = True

if megtalalhato:
    print(f'Az adott szín megtalálható a képen.')
else:
    print(f'Az adott szín nincs a képen.')

print(f'\n3. feladat')
vizsgalando_szin = osszes_adat[34][7]
sor35db = osszes_adat[34].count(osszes_adat[34][7])

oszlop8db = 0
for x in osszes_adat:
    if x[7] == vizsgalando_szin:
        oszlop8db += 1

print(f'Sorban: {sor35db} Oszlopban: {oszlop8db}')

print(f'\n4. feladat')
voros = 0
zold = 0
kek = 0
van_kiiras = False

for x in osszes_adat:
    voros += x.count([255, 0, 0])
    zold += x.count([0, 255, 0])
    kek += x.count([0, 0, 255])

if voros == max(voros, kek, zold) and not van_kiiras:
    print('vörös')
    van_kiiras = True

if zold == max(voros, kek, zold) and not van_kiiras:
    print('zöld')
    van_kiiras = True

if kek == max(voros, kek, zold) and not van_kiiras:
    print('kék')
    van_kiiras = True

print(f'\5. feladat')
keretes_kep = []
fekete_sorok = [0, 1, 2, 49, 48, 47]

for index, x in enumerate(osszes_adat):
    if index in fekete_sorok:
        for y in range(50):
            osszes_adat[index][y] = [0,0,0]
    else:
        x[-1] = x[-2] = x[-3] = x[0] = x[1] = x[2] = [0, 0, 0]
    keretes_kep.append(x)

print(f'\n6.feladat')
ujfile = open(f'keretes.txt','w', encoding='utf-8')
for x in keretes_kep:
    for y in x:
        print(' '.join(list(map(str, y))), file=ujfile)
ujfile.close()

    


    

        

