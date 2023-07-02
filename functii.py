def printGreeting():
    print('Buna ziua!Bine ati venit!')

def printGreetingByName(nume,prenume):
    print(f'Buna ziua {nume} {prenume}')

def mediaNr(a,b,c ):
    return (a + b + c)/3

def piValue():
    return 3.14

#exercitiu
#daca pers este majora,altfel false

def verificareMajor(varsta):
    if varsta >= 18:
        return True
    else:
        return False


#zona de apelare
printGreeting()
printGreetingByName('Circiumaru' ,'Ruxandra')
printGreetingByName('Circiumaru' ,'Ofelia')
printGreetingByName('Circiumaru' ,'Daniel')
print(mediaNr(3,6,4))
print(piValue())

#se ia varsta utilizatorului
age = int(input('Introduceti varsta: '))
if verificareMajor(age):
    print('Cont creat, bine ai venit in aplicatie')
else:
    print('Nu ai varsta necesara(18) pt a paria')