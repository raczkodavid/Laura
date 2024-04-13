import random
#1. feladat
adatok = []
with open('kerites.txt', 'r', encoding='utf-8') as file:
    for i in file:
        szotar = {}
        i = i.strip().split()
        if int(i[0]) == 0:
            szotar['paritas'] = 'páros'
        elif int(i[0]) == 1:
            szotar['paritas'] = 'páratlan'
        
        szotar ['szelesseg'] = int(i[1])
        szotar['kerites'] = i[2]
        adatok.append(szotar)

print(f'2. feladat')
print(f'Az eladott telkek száma: {len(adatok)}')

print(f'3. feladat')
print(f'A {adatok[-1]["paritas"]} oldalon adták el az utolsó telket.')
paros_telkek = 0
paratlan_telkek = 0
for i in adatok:
    if i['paritas'] == 'páros':
        paros_telkek += 1
    else:
        paratlan_telkek += 1

if adatok[-1]['paritas'] == 'páros':
    print(f'Az utolsó telek házszáma: {paros_telkek*2}')
else:
    print(f'Az utolsó telek házszáma: {paratlan_telkek*2}')

print(f'4. feladat')
paratlan_telkek_lista = []
paros_telkek_lista = []

for index, x in enumerate(adatok):
    if x['paritas'] == 'páratlan':
        paratlan_telkek_lista.append(adatok[index])
    else:
        paros_telkek_lista.append(adatok[index])

for index, i in enumerate(paratlan_telkek_lista):
    if index < len(paratlan_telkek_lista) - 1:
        if paratlan_telkek_lista[index]['kerites'] == paratlan_telkek_lista[index+1]['kerites']:
            if paratlan_telkek_lista[index]['kerites'] != ':' and paratlan_telkek_lista[index]['kerites'] != '#':
                print(f'A szomszédossal egyezik a kerítés színe: {(index)*2+1}')
                break

print(f'5. feladat')
bekert_hazszam = 4         #int(input('Adjon meg egy házszámot! '))
elotte_kerites = None
utana_kerites = None

if bekert_hazszam %2 != 0:
    print(f'A kerítés színe / állapota: {paratlan_telkek_lista[bekert_hazszam//2]["kerites"]}')
    elotte_kerites = paratlan_telkek_lista[bekert_hazszam//2-1]["kerites"]
    utana_kerites = paratlan_telkek_lista[bekert_hazszam//2+1]["kerites"]
else:
    print(f'A kerítés színe / állapota: {paros_telkek_lista[bekert_hazszam//2]["kerites"]}')
    elotte_kerites = paros_telkek_lista[bekert_hazszam//2-1]["kerites"]
    utana_kerites = paros_telkek_lista[bekert_hazszam//2+1]["kerites"]

karakterek = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

valasztott_szin = random.choice(karakterek)
while valasztott_szin == elotte_kerites or valasztott_szin == utana_kerites:
    valasztott_szin = random.choice(karakterek)

print(f'Egy lehetséges festési szín: {valasztott_szin}')

#6. feladat
ujfile = open('utcakep.txt', 'w')
szamok_lista = []
for index, i in enumerate(paratlan_telkek_lista):
    szamok_lista.append(f'{index*2+1}{(paratlan_telkek_lista[index]["szelesseg"]-len(str(index*2+1)))*" "}')

for index, i in enumerate(paratlan_telkek_lista):
    print(f'{paratlan_telkek_lista[index]["kerites"]*paratlan_telkek_lista[index]["szelesseg"]}', end='', file=ujfile)
print(file=ujfile)
print(''.join(szamok_lista), file=ujfile)

ujfile.close()

