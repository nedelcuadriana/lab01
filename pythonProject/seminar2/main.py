import clase
from clase import Tara

#apelam metoda
e = clase.Entitate(1, "test")  #exemplu de instantiere
e.display()  #apel de metoda

a = Tara(1, "Spania", 67000000, 12345)
b = Tara(2, "Romania", 67000000, 12345)
c = Tara(3, "Italia", 67000000, 12345)
lista = [a, b, c]

for each in lista:
    print(each)
