adatok = []
dict = {}
with open(f'beosztas.txt','r',encoding='utf-8') as file:
    for x in file:
        dict['tanar'] = x.strip()
        dict['tantargy'] = next(file).strip()
        dict['osztaly'] = next(file).strip()
        dict['oraszam'] = int(next(file).strip())
        adatok.append(dict)
        dict = {}

print(f'2. feladat')
print(f'A fájlban {len(adatok)} bejegyzés van.')

print(f'3. feladat')
ossz_oraszam = sum([x['oraszam'] for x in adatok])
print(f'Az iskolában a heti összóraszám: {ossz_oraszam}')

print(f'4. feladat')
valasztott_tanar = 'Albatrosz Aladin'   #input(f'Egy tanár neve= ')
v_tanar_oraszam = sum([x['oraszam'] for x in adatok if x['tanar'] == valasztott_tanar])
print(f'A tanár heti óraszáma: {v_tanar_oraszam}')

osztalyok = set(x['osztaly'] for x in adatok if 'x' not in x['osztaly'])
ujfile = open(f'of.txt','w')
for x in osztalyok:
    of = None
    for y in adatok:
        if y['osztaly'] == x:
            if y['tantargy'] == 'osztalyfonoki':
                of = y['tanar']
    print(f'{of} - {x}', file=ujfile)

ujfile.close()

print(f'6. feladat')
bekert_osztaly = '10.b'     #input(f'Osztály= ')
bekert_tantargy = 'kemia'   #input(f'Tantárgy= ')
szamlalo = 0

for x in adatok:
    if x['osztaly'] == bekert_osztaly and x['tantargy'] == bekert_tantargy:
        szamlalo += 1

if szamlalo > 1:
    print(f'Csoportbontásban tanulják.')
else:
    print(f'Osztályszinten tanulják.')

print(f'7. feladat')
tanarok = set(x['tanar'] for x in adatok)
print(F'Az iskolában {len(tanarok)} tanár tanít.')
