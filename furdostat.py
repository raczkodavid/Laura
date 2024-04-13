def mpbe(ora, perc, mp):
    return ora*3600 + perc*60 + mp

def vissza_idobe(mp):
    ora = mp // 3600
    perc = mp % 3600 // 60
    masodperc = mp % 60
    return f'{ora}:{perc}:{masodperc}'

adatok = {}
with open(f'furdoadat.txt','r',encoding='utf-8') as file:
    for x in file:
        x = list(map(int, [y for y in x.strip().split()]))
        dict = {}
        if x[0] not in adatok.keys():
            adatok[x[0]] = {}
        if x[1] not in adatok[x[0]].keys():
            adatok[x[0]][x[1]] = []
        adatok[x[0]][x[1]].append(mpbe(x[3], x[4], x[5]))

print(f'2. feladat')
print(f'Az első vendég {vissza_idobe(adatok[list(adatok)[0]][0][0])}-kor lépett ki az öltözőből.')
print(f'Az utolsó vendég {vissza_idobe(adatok[list(adatok)[-1]][0][0])}-kor lépett ki az öltözőből. ')

print(f'\n3. feladat')
egy_reszlegen = [x for x in adatok if len(adatok[x].keys()) == 2]
print(f'A fürdőben {len(egy_reszlegen)} vendég járt csak egy részlegen.')

print(f'\n4. feladat')
legtobb_eltoltott = 0
legtobb_eltoltott_szemely = None
for x in adatok:
    if adatok[x][0][1] - adatok[x][0][0] > legtobb_eltoltott:
        legtobb_eltoltott = adatok[x][0][1] - adatok[x][0][0]
        legtobb_eltoltott_szemely = x

print(f'A legtöbb időt eltöltő vendég: ')
print(f'{legtobb_eltoltott_szemely}. vendég {vissza_idobe(legtobb_eltoltott)}')

print(f'\n5. feladat')
hatkilenc = 0
kilenctizenhat = 0
tizenhathusz = 0

for x in adatok:
    if 6*3600 <= adatok[x][0][0] < 9*3600:
        hatkilenc += 1
    elif 9*3600 <= adatok[x][0][0] < 16*3600:
        kilenctizenhat += 1
    elif 16*3600 <= adatok[x][0][0] < 20*3600:
        tizenhathusz += 1

print(f'6-9 óra között {hatkilenc} vendég\n9-16 óra között {kilenctizenhat} vendég\n16-20 óra között {tizenhathusz} vendég')

#6. feladat
ujfile = open('szauna.txt','w')
for x in adatok:
    eltoltott = 0
    if 2 in adatok[x]:
        for y in range(0, len(adatok[x][2]), 2):
            if y < len(adatok[x][2]) - 1:
                eltoltott += adatok[x][2][y+1] - adatok[x][2][y]
    if eltoltott != 0:
        print(x, vissza_idobe(eltoltott), sep=' ', file=ujfile)

ujfile.close()
print(f'\n7.feladat')
uszoda = 0
szauna = 0
gyogy = 0
strand = 0

for x in adatok:
    if 1 in adatok[x]:
        uszoda += 1
    if 2 in adatok[x]:
        szauna += 1
    if 3 in adatok[x]:
        gyogy += 1
    if 4 in adatok[x]:
        strand += 1

print(f'Uszoda: {uszoda}\nSzaunák: {szauna}\nGyógyvizes medencék: {gyogy}\nStrand: {strand} ')



            
    

        
        