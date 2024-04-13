adatok = []
with open(f'naplo.txt','r',encoding='utf-8') as file:
    for i in file:
        dict = {}
        i = i.strip().split()
        if i[0] == '#':
            honap = int(i[1])
            nap = int(i[2])
        elif i[0] != '#':
            dict['honap'] = honap
            dict['nap'] = nap
            dict['nev'] = f'{i[0]} {i[1]}'
            dict['hianyzas'] = i[2]
            adatok.append(dict)

print(f'2. feladat')
print(f'A naplóban {len(adatok)} bejegyzés van.')

print(f'3. feladat')
igazolt = 0
igazolatlan = 0
tanulok = set()

for x in adatok:
    tanulok.add(x['nev'])
    for y in x['hianyzas']:
        if y == 'X':
            igazolt += 1
        elif y == 'I':
            igazolatlan += 1

print(f'Az igazolt hiányzások száma {igazolt}, az igazolatlanoké {igazolatlan} óra.')

#4. feladat
def hetnapja(honap, nap):
    napnev = ("vasarnap", "hetfo", "kedd", "szerda", "csutortok", "pentek", "szombat")
    napszam= (0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 335)
    napsorszam = (napszam[honap-1]+nap) % 7
    return napnev[napsorszam]

print(f'5. feladat')
bekert_honap = 2        #int(input(f'A hónap sorszáma= '))
bekert_nap = 3          #int(input(f'A nap sorszáma= '))
print(f'Azon a napon {hetnapja(bekert_honap, bekert_nap)} volt.')

print(F'6. feladat')
bekert_nap = 'szerda'     #input(f'A nap neve= ')
bekert_ora = 3            #int(input(f'Az óra sorszáma= '))

hianyzasok = 0
for i in adatok:
    if hetnapja(i['honap'], i['nap']) == bekert_nap:
        if i['hianyzas'][bekert_ora-1] == 'I' or i['hianyzas'][bekert_ora-1] == 'X':
            hianyzasok += 1

print(f'Ekkor összesen {hianyzasok} óra hiányzás történt.')

print(f'7. feladat')
seged_lista = []
for x in tanulok:
    ossz_hianyzas = 0
    for y in adatok:
        if y['nev'] == x:
            for z in y['hianyzas']:
                if z == 'I' or z == 'X':
                    ossz_hianyzas += 1
    seged_lista.append([x, ossz_hianyzas])

max_hianyzas = 0
for x in seged_lista:
    if x[1] > max_hianyzas:
        max_hianyzas = x[1]

print(f'A legtöbbet hiányzó tanulók: ',end='')
for x in seged_lista:
    if x[1] == max_hianyzas:
        print(f'{x[0]} ',end='')


