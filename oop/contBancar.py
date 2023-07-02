class ContBancar:
    #constructor
    def __init__(self, titularCont, iban):
        #atribute,fields
        self.titularCont = titularCont
        self.iban = iban
        self.sold = 0
        self.pin = 7777
        self.activ = False
        self.incercariActivare = 0

    def InterogareSold(self):
        print(f'Titular {self.titularCont}')
        print(f'iban {self.iban}')
        print(f'Sold {self.sold}')
        print(f'Activare cont {self.activ}')
        print(f'Incercari activare {self.incercariActivare}')
        print('---------------------------------------------')

    def ActivareCont(self,pinUtilizatir):
        print(f'Buna {self.titularCont}')
        if pinUtilizatir == self.pin:
            print('Card activat')
            self.activ = True
        else:
            print('Pin gresit')
            self.incercariActivare = self.incercariActivare + 1
            #self.incercariActivare+=1

    def alimentareCont(self,suma):
        print(f'Buna {self.titularCont}')
        self.sold +=suma
        print(f'Ati alimenta cu {suma}')
        print(f'Aveti un sold de { self.sold}')

    def sumaCheltuita(self,suma):
        print(f'Buna {self.titularCont}')
        if suma <= self.sold:
            self.sold -=suma
            print(f'Ati cheltuit {suma}')
            print(f'Aveti in cont {self.sold}')
        else:
            print('Fonduri insuficiente')





