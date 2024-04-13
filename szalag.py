class szallitas ():
    def __init__(self, mikor, honnan, hova, tomeg):
        self.mikor = int(mikor)
        self.honnan = int(honnan)
        self.hova = int(hova)
        self.tomeg = int(tomeg)
        
adatok = []
sz_hossz, elmozd_ido = 0, 0
with open("szallit.txt", "r", encoding="UTF-8") as file:
    for index, i in enumerate(file):
        i = i.strip().split()
        if index > 0 :
            adatok.append(szallitas(i[0], i[1], i[2], i[3]))
        else:
            sz_hossz = int(i[0])
            elmozd_ido = int(i[1])

print("2. feladat")
feladatsor = 3  #int(input(f"Adja meg, melyik adatsorra kíváncsi! "))
print(f"Honnan: {adatok[feladatsor-1].honnan} Hova: {adatok[feladatsor-1].hova}")

def tav(szalaghossz, indulashelye, erkezeshelye):
    if indulashelye > erkezeshelye:
        return szalaghossz - indulashelye + erkezeshelye
    else:
        return erkezeshelye - indulashelye

print(f"\n4. feladat")
legnagyobb_tavolsag = 0
legnagyobb_tavolsag_indexek = []
for x in adatok:
    if tav(sz_hossz, x.honnan, x.hova) > legnagyobb_tavolsag:
        legnagyobb_tavolsag = tav(sz_hossz, x.honnan, x.hova)

for index, y in enumerate(adatok):
    if tav(sz_hossz, y.honnan, y.hova) == legnagyobb_tavolsag:
        legnagyobb_tavolsag_indexek.append(str(index+1))

print(f"A legnagyobb távolság: {legnagyobb_tavolsag}\nA maximális távolságú szállítások sorszáma: {' '.join(legnagyobb_tavolsag_indexek)}")

print(f"5. feladat")
ossztomeg = 0
for x in adatok:
    if x.hova != 0 and x.honnan != 0 and (x.honnan > x.hova):
        ossztomeg += x.tomeg

print(f"A kezdőpont előtt elhaladó rekeszek össztömege: {ossztomeg}")

print(f"6. feladat")
idopont = 300 #int(input(f"Adja meg a kívánt időpontot! "))
sz_rekeszek = []
for index, x in enumerate(adatok):
    ido_min = x.mikor
    ido_max = tav(sz_hossz, x.honnan, x.hova) * elmozd_ido
    if ido_min <= idopont < ido_max:
        sz_rekeszek.append(str(index+1))

print(f"A szállított rekeszek halmaza: {' '.join(sz_rekeszek)}")

ujfile = open("tomeg.txt", "w", encoding="UTF-8")
szallitasok_kezdete = set(x.honnan for x in adatok)
sz_fileba = []
for x in szallitasok_kezdete:
    t = 0
    for y in adatok:
        if y.honnan == x:
            t += y.tomeg
    sz_fileba.append([x, t])

sz_fileba = sorted(sz_fileba, key= lambda x: x[0])
for x in sz_fileba:
    print(" ".join(list(map(str, x))), file=ujfile)

ujfile.close()