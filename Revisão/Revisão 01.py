from Classes import Vendedor

vendedor1 = Vendedor("Lira")
vendedor1.vender(430)
vendedor1.bater_meta(500)
print(vendedor1.vendas)

vendedor2 = Vendedor("Alan")
vendedor2.vender(700)
vendedor2.bater_meta(600)
print(vendedor2.vendas)