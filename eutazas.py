adatok = []
with open(f'utasadat.txt','r',encoding='utf-8') as file:
    for i in file:
        i = i.strip().split()
        dict = {}
        dict['megallo'] = int(i[0])
        dict['datum'] = i[1]
        dict['id'] = int(i[2])
        dict['tipus'] = i[3]
        dict['ervenyes'] = i[4]
        adatok.append(dict)

print(f'2. feladat')
print(f'A buszra {len(adatok)} utas akart felszállni.')

print(f'3. feladat')
nem_szallhatott_fel = []
for x in adatok:
    if x['datum'][:8] > x['ervenyes'] and x['tipus'] != 'JGY':
        nem_szallhatott_fel.append(x['id'])
    elif x['tipus'] == 'JGY' and x['ervenyes'] == '0':
        nem_szallhatott_fel.append(x['id'])

print(f'A buszra {len(nem_szallhatott_fel)} utas nem szállhatott fel.')

print(f'4. feladat')
legtobb_felszallo = 0
l_megallo = None

for x in range(30):
    szamlalo = 0
    for y in adatok:
        if x == y['megallo']:
            szamlalo += 1
            if szamlalo > legtobb_felszallo:
                legtobb_felszallo = szamlalo
                l_megallo = y['megallo']

print(f'A legtöbb utas ({legtobb_felszallo} fő) a {l_megallo}. megállóban próbált felszállni.')

print(f'5. feladat')
kedvezmenyes = 0
ingyenes = 0
for x in adatok:
    if x['id'] not in nem_szallhatott_fel:
        if x['tipus'] == 'TAB' or x['tipus'] == 'NYB':
            kedvezmenyes += 1
        elif x['tipus'] == 'NYP' or x['tipus'] == 'RVS' or x['tipus'] == 'GYK':
            ingyenes += 1

print(f'Ingyenesen utazók száma: {ingyenes} fő')
print(f'A kedvezményesen utazók száma: {kedvezmenyes} fő')

def napokszama(e1, h1, n1, e2, h2, n2):
	h1 = (h1 + 9) % 12
	e1 = e1 - h1 // 10
	d1= 365*e1 + e1 // 4 - e1 // 100 + e1 // 400 + (h1*306 + 5) // 10 + n1 - 1
	h2 = (h2 + 9) % 12
	e2 = e2 - h2 // 10
	d2= 365*e2 + e2 // 4 - e2 // 100 + e2 // 400 + (h2*306 + 5) // 10 + n2 - 1
	return d2-d1

ujfile = open(f'figyelmeztes.txt','w')


for x in adatok:
    if x['tipus'] != 'JGY':
        e1 = int(x['datum'][:4])
        h1 = int(x['datum'][4:6])
        n1 = int(x['datum'][6:8])
        e2 = int(x['ervenyes'][:4])
        h2 = int(x['ervenyes'][4:6])
        n2 = int(x['ervenyes'][6:8])

        if napokszama(e1, h1, n1, e2, h2, n2) <= 3 and x['id'] not in nem_szallhatott_fel:
            print(f'{x["id"]} {e2}-{h2}-{n2}', file=ujfile)

ujfile.close()

    

    





