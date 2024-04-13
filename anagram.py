print(f'1. feladat')
valasztott_szo = "Misihusi"               #input(f'Adjon meg egy szót! ')
valasz1 = set(i for i in valasztott_szo)
print(f'A megadott szóban összesen {len(valasz1)}, a karakterek: {" ".join(sorted(valasz1))}')

print(f'2. feladat - Adatok beolvasása')
with open(f'szotar.txt','r', encoding='utf-8') as file:
    adatok = [i.rstrip() for i in file]

print(f'3. feladat - file kialakítása')
ujfile = open(f'abc.txt','w')
for i in adatok:
    print("".join(sorted(i)), file=ujfile)
ujfile.close

print(f'4. feladat')
elso_szo = "ajak"       #input(f'Adja meg az első szót! ')
masodik_szo = "kaja"    #input(f'Adja meg a második szót! ')

if sorted(elso_szo) == sorted(masodik_szo):
    print(f'Anagramma')
else:
    print(f'Nem anagramma')

print(f'5. feladat')
otodik_szo = 'takar' #input(f'Adjon meg egy szót! ')
for x in adatok:
    if sorted(x) == sorted(otodik_szo):
        print(x)

print(f'6. feladat')
max_hossz = 0
for x in adatok:
    if len(x) > max_hossz:
        max_hossz = len(x)

        set6 = set(x for x in adatok if len(x) == max_hossz)
print("\n".join(set6))

print(f'7. feladat - rendezve.txt elkészítése')
ujfile2 = open(f'rendezve.txt','w')

def novekvo(x):
    return len(list(x)[0])

osszes_szo = set(sorted(set(''.join(sorted(x)) for x in adatok),key=novekvo))
lista7 = []

for x in osszes_szo:
    seged = set()
    for y in adatok:
        if ''.join(sorted(y)) == x:
            seged.add(''.join(y))
    lista7.append(seged)

lista7 = sorted(lista7, key=novekvo)
elozo_hossz = len(list(lista7[0])[0])

for x in lista7:
    if len(list(x)[0]) > elozo_hossz:
        print(f"\n{' '.join(sorted(x))}", file=ujfile2)
    else:
        print(f'{" ".join(sorted(x))}', file=ujfile2)
    elozo_hossz = len(list(x)[0])

ujfile2.close()
        



    