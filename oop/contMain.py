from oop.contBancar import ContBancar

cont1 = ContBancar('Ruxi','RO001')
cont2 = ContBancar('Elena','RO002')

cont1.ActivareCont(5555)
cont2.ActivareCont(7777)
cont1.ActivareCont(7777)

cont1.alimentareCont(400)
cont2.alimentareCont(700)
cont1.alimentareCont(600)

cont1.sumaCheltuita(1100)
cont1.sumaCheltuita(400)
cont2.sumaCheltuita(700)

cont1.InterogareSold()
cont2.InterogareSold()