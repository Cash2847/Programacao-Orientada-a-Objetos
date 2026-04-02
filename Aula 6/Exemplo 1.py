import Teste as fun

cachorro = fun.Cachorro("Matheus", "Pastor Alemão", 10)
gato = fun.Gato("Susana", "Nuvem", 7)
vaca = fun.Vaca("Chloe", "Holstein-Frísia", 20)

lista = [cachorro, gato, vaca]
for i in lista:
    print(i.ruido()) 
    
print(json)