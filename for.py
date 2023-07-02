#dalmatienii

for i in range(0,102):
    print(f'Dalmatianul cu numarul {i} ')

#parcurgere lista cu for cu ajutorul indexului
numere  = [3,7,10, 20 ,30]

for i in range(0, len(numere)):
    print(f'Indexul curent este {i}')
    print(f'Numarul curent este {numere[i]}')

#for each
s = 0
for numar in numere:
    print(f'Numarul curent este {numar}')
    s = s + numar
    print(f'Suma este {s}')