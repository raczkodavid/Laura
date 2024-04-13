def percbe(ora, perc):
    return ora*60 + perc

def vissza_idobe(minute):
    ora = minute // 60
    perc = minute % 60
    return f'{ora}:{perc}'

szotar = {}
with open('vonat.txt','r', encoding='utf-8') as file:
    for i in file:
        i = i.strip().split()
        for index, x in enumerate(i):
            if index < len(i) - 1:
                i[index] = int(i[index])  
        
        ido = i[2] * 60 + i[3] 
        
        if i[0] not in szotar.keys():
            szotar[i[0]] = {}
        
        if i[1] not in szotar[i[0]]:
            szotar[i[0]][i[1]] = {}
        
        if i[4] == 'I':
            szotar[i[0]][i[1]]['indulas'] = ido
        
        elif i[4] == 'E':
            szotar[i[0]][i[1]]['erkezes'] = ido

#2. feladat
print(f'Az állomások száma: {len(szotar[1])}')
print(f'A vonatok száma: {len(szotar)}')

#3. feladat
print(f'3. feladat')
legtobb_varakozas = 0
vonat_szam = None
allomas_szam = None

for x in range(1, 13):
    for y in range(1, 10):
        if szotar[x][y]['indulas'] - szotar[x][y]['erkezes'] > legtobb_varakozas:
            legtobb_varakozas = szotar[x][y]['indulas'] - szotar[x][y]['erkezes']
            vonat_szam = x
            allomas_szam = y

print(f'A(z) {vonat_szam}. vonat a(z) {allomas_szam}. állomáson {legtobb_varakozas} percet állt')

#4. feladat
print(f'4. feladat')
valasztott_vonat = 2                        #int(input(f'Adja meg egy vonat azonosítóját! '))
valasztott_idopont = '8 45'.split()       #input(f'Adjon meg egy időpontot (óra perc)! ').split()
valasztott_idopont = percbe(int(valasztott_idopont[0]), int(valasztott_idopont[1]))

#5. feladat
print(f'5. feladat')
menetido = szotar[valasztott_vonat][10]['erkezes'] - szotar[valasztott_vonat][0]['indulas']
eloirt_menetido = 142

if menetido > eloirt_menetido:
    print(f'A(z) {valasztott_vonat}. vonat útja {menetido-eloirt_menetido} perccel hosszabb volt az előírtnál.')

elif menetido < eloirt_menetido:
    print(f'A(z) {valasztott_vonat}. vonat útja {abs(menetido-eloirt_menetido)} perccel rövidebb volt az előírtnál.')

elif menetido == eloirt_menetido:
    print(f'A(z) {valasztott_vonat}. vonat útja pontosan az előírt ideig tartott')

ujfile = open(f'halad{valasztott_vonat}.txt','w')
for i in range(1,11):
    print(f'{i}. állomás: {vissza_idobe(szotar[valasztott_vonat][i]["erkezes"])}', file=ujfile)

ujfile.close()

#7. feladat
for x in range(1, 13):
    for y in range(1,10):
        if szotar[x][0]['indulas'] <= valasztott_idopont <= szotar[x][10]['erkezes']:
            if szotar[x][y]['erkezes'] <= valasztott_idopont <= szotar[x][y]['indulas']:
                print(f'A(z) {x}. vonat a {y}. állomáson állt.')
            elif szotar[x][y]['indulas'] < valasztott_idopont < szotar[x][y+1]['erkezes']:
                print(f'A(z) {x}. vonat a {y}. és a {y+1}. állomás között járt.')

    if szotar[x][0]['indulas'] < valasztott_idopont < szotar[x][1]['erkezes']:
        print(f'A(z) {x}. vonat a kezdőállomás és az első állomás között haladt.')
    
    if szotar[x][9]['indulas'] < valasztott_idopont < szotar[x][10]['erkezes']:
        print(f'A(z) {x}. vonat a 9. és a végállomás között haladt.')


