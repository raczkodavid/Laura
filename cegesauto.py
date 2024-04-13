adatok = []
with open(f'autok.txt','r',encoding='utf-8') as file:
    for i in file:
        i = i.strip().split()
        dict = {}
        dict['nap'] = int(i[0])
        dict['ido'] = i[1]
        dict['rendszam'] = i[2]
        dict['szemelyid'] = int(i[3])
        dict['km'] = int(i[4])
        if i[5] == '0':
            dict['kapu'] = 'ki'
        else:
            dict['kapu'] = 'be'
        adatok.append(dict)

print(f'2. feladat')
utolso_rendszam = None
utolso_nap = None
autok = set()
for x in adatok:
    autok.add(x["rendszam"])
    if x['kapu'] == 'ki':
        utolso_rendszam = x['rendszam']
        utolso_nap = x['nap']

print(f'{utolso_nap}. nap rendszám: {utolso_rendszam}')

print(f'3. feladat')
valasztott_nap = 4                                  #int(input(f'Nap: '))
print(f'Forgalom a(z) {valasztott_nap}. napon:')
for x in adatok:
    if x['nap'] == valasztott_nap:
        print(f'{x["ido"]} {x["rendszam"]} {x["szemelyid"]} {x["kapu"]}')

print(f'4. feladat')
parkoloban = []
for x in adatok:
    if x['kapu'] == 'ki':
        parkoloban.append(x["rendszam"])
    elif x['kapu'] == 'be':
        if x["rendszam"] in parkoloban:
            parkoloban.remove(x["rendszam"])

print(f'A hónap végén {len(parkoloban)} autót nem hoztak vissza.')
print(parkoloban)

print(f'5. feladat')
megoldas_lista = []
for x in autok:
    kezdo_km = None
    veg_km = None
    for y in adatok:
        if y['rendszam'] == x:
            if kezdo_km == None:
                kezdo_km = y["km"]
            else:
                veg_km = y["km"]
    print(f'{x} {veg_km-kezdo_km} km')

print(f'6. feladat')
legtobb_km_egyben = 0
legtobb_km_egyben_szemely = None

for x in autok:
    kezdo_km = None
    veg_km = None
    for y in adatok:
        if x == y['rendszam']:
            if y['kapu'] == 'ki':
                kezdo_km = y['km']
            elif y['kapu'] == 'be':
                veg_km = y['km']
                if veg_km - kezdo_km >= legtobb_km_egyben:
                    legtobb_km_egyben = veg_km - kezdo_km
                    legtobb_km_egyben_szemely = y['szemelyid']

print(f'Leghosszabb út: {legtobb_km_egyben} km, személy: {legtobb_km_egyben_szemely}')

print(F'7. feladat')
valasztott_rendszam = 'CEG304'      #input(f'Rendszám: ')
ujfile = open(f'{valasztott_rendszam}.txt','w')

ki = None
be = None

for x in adatok:
    if x["rendszam"] == valasztott_rendszam:
        if x["kapu"] == 'ki':
            ki = x
        else:
            be = x
            print(f'{ki["szemelyid"]}\t{ki["nap"]}.\t{ki["ido"]}\t{ki["km"]} km\t{be["nap"]}.\t{be["ido"]}\t{be["km"]} km', file=ujfile)

if valasztott_rendszam in parkoloban:
    print(f'{ki["szemelyid"]}\t{ki["nap"]}.\t{ki["ido"]}\t{ki["km"]} km', file=ujfile)

ujfile.close()
