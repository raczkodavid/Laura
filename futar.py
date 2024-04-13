print(f'1. feladat - adatok beolvasása')
adatok = []
with open(f'tavok.txt','r',encoding='utf-8') as file:
    for x in file:
        dict = {}
        x = list(map(int, x.strip().split()))
        dict['napsorszam'] = x[0]
        dict['fuvarszam'] = x[1]
        dict['km'] = x[2]
        adatok.append(dict)

print(f'\n2. feladat')
def novekvo(x):
    return x["napsorszam"]

elso_nap = sorted(adatok, key=novekvo)[0]["napsorszam"]
utolso_nap = sorted(adatok, key=novekvo)[-1]["napsorszam"]

for x in adatok:
    if x["napsorszam"] == elso_nap and x["fuvarszam"] == 1:
        print(f'A hét legelső útja {x["km"]} kilóméter volt.')
        break

print(f'\n3. feladat')
fuvarszam = 0
utolso_km = 0

for x in adatok:
    if x["napsorszam"] == utolso_nap:
        if x["fuvarszam"] > fuvarszam:
            fuvarszam = x["fuvarszam"]
            utolso_km = x["km"]

print(f'A hét utolsó útja {utolso_km} kilóméter volt.')

print(f'\n4. feladat')
szabadnapok = [x for x in range(1, 8)]
munkanapok = set()

for x in adatok:
    munkanapok.add(x["napsorszam"])
    if x["napsorszam"] in szabadnapok:
        szabadnapok.remove(x["napsorszam"])

munkanapok = sorted(munkanapok)

print(f'A futár a hét {", ".join(map(str, szabadnapok))} napján/napjain nem dolgozott.')

print(f'\n5. feladat')
legtobb_fuvar = 0
for x in adatok:
    if x["fuvarszam"] > legtobb_fuvar:
        legtobb_fuvar = x["fuvarszam"]

for x in adatok:
    if x["fuvarszam"] == legtobb_fuvar:
        print(f'A legtöbb fuvar a hét {x["napsorszam"]}. napján volt.')

print(f'\n6. feladat')
napok = [x for x in range(1, 8)]
for x in napok:
    km = 0
    for y in adatok:
        if y['napsorszam'] == x:
            km += y['km']
    print(f'{x}. nap: {km} km')

print(f'\n7. feladat')
def fizetes(km):
    if 1 <= km <= 2:
        osszeg = 500
    
    elif 3 <= km <= 5:
        osszeg = 700
    
    elif 6 <= km <= 10:
        osszeg = 900
    
    elif 11 <= km <= 20:
        osszeg = 1400
    
    elif 21 <= km <= 30:
        osszeg = 2000
    
    return osszeg

bekert_tavolsag = 15    #int(input(f'Adjon meg egy tetszóleges távolságot (<=30km): '))
print(f'Ezért a távolságért {fizetes(bekert_tavolsag)}Ft-ot kapna a futár.')

print(f'\n8. feladat')
ujfile = open(f'dijazas.txt','w')
heti_fizetes = 0

def fuvarszam_nov(x):
    return x["fuvarszam"]

for x in munkanapok:
    seged = []
    for y in adatok:
        if y["napsorszam"] == x:
            seged.append(y)
    seged = sorted(seged, key=fuvarszam_nov)
    for z in seged:
        print(f'{z["napsorszam"]}. nap {z["fuvarszam"]}. út: {fizetes(z["km"])} Ft', file=ujfile)
        heti_fizetes += fizetes(z["km"])

ujfile.close()

print(f'\n9. feladat')
print(f'A futár a heti munkájáért {heti_fizetes}Ft-ot kap.')