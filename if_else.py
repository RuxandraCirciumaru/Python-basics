piesa_faina = True
print('Pornim radio')
if piesa_faina == True:
    print('Dau muzica mai tare')

print('Oprim radio')

#if-else
#daca nr-par,printam par, daca nu, printam impar
number = 9

if number % 2 == 0:
     print('Numarul este par')
else:
     print('Numarul este impar')

#este un numar pozitiv?

if number > 0:
    print('nr este pozitiv')
else:
    print('nr este negativ')

#if else if else

#cum ne saluta un robotel dimineata?

#luam date de la tastatura si ne asiguram ca sunt transformate din string in int

ora = int(input('Introduceti ora'))
if ora < 0:
    print('Introduceti o ora valida')
elif ora <= 11:
    print('Buna dimineata')
elif ora>11 and ora <= 18:
    print('Buna ziua')
elif ora > 18 and ora<= 22 :
    print('Buna seara')
elif ora > 22 and ora <= 24:
    print('Noapte buna')
else:
    print('Introduceti o ora in intervalul 0-24')

#robotel telefonic

optiune =int(input('alegeti optiunea'))

if optiune == 0:
    print('Meniu anterior')
elif optiune == 1:
    print('Romana')
elif optiune == 2:
    print('Engleza')
elif optiune == 3:
    print('Franceza')
else:
    print('Nu ati ales niciuna din optiunile valabile')

