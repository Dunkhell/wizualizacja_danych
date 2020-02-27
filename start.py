print("WITAJ SWIECIE!!!")
tekst= "hello world!"
tekst= 'hello world!'
tekst= """hello
world"""
#nie określamy typu zmiennej bo to wartość jaką przyjmuje decyduje czym ona jest

print(type(tekst))
print(type(5))
print(type(True))
print(type(None))
print(tekst)

print(2+2)
#Można wykonywać wszystkie działania
# // DZIELENIE BEZ RESZTY
# % RESZTA Z DZIELENIA
# ** POTĘGOWANIE

print("Ala " + "ma kota.") #konkatencja
# print("Ala " + "ma " + 5 + " lat") nie zadziała
print("Ala " + "ma " + str(5) + " lat") 
liczba = int("100")
print(liczba)

print("Ala " * 10)

#listy

lista= []
print(type(lista))
lista2= [1, 2, 3]
print(lista2[0])

imie= "Anna"
print(imie[0])

lista2[0]= 5
# imie[0]= "B" BŁĄD
print(imie.swapcase())
imie = imie.swapcase()
print(imie)

"Ala".swapcase()
lista3= [1, "Ala", 4.5, None, True, [1, 2]] #W LIŚCIE MOŻNA PRZECHOWYWAĆ RÓŻNE WARTOŚCI I TYPY DANYCH
# LISTY POWYŻEJ NIE DA SIĘ POSORTOWAĆ 
lista3[5][1]

macierz= [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(macierz[1][1])
nowa = lista2 + macierz

# słownik
slownik= {}
slownik["imie"] = "Piotr"
slownik[0]= "Adam"
#nie odwołuje się po indeksie (np. 0,1,2,3) tylko po nazwie klucza którą sami ustalamy
#klucz musi być unikalny 
print(slownik)

print(slownik.keys())
print(slownik.values())

def pow(): 
    pass

from math import * #nadpisuje funckje jeżeli maja taka sama nazwe jak te użyte w kodzie
import math as m #lepszy sposob nadajacy allias zeby móc lepiej używać całej bioblioteki
from math import pow as mpow 
from math import pow , sin , sqrt



#ZADANIE 1 
a = 5
b = 3
imie = "Jan"
nazwisko = "Nowak"
print(a)
print(b)
print(imie)
print(nazwisko)

#zadanie 2
a=1
b=2
c=3

dzielenie= a/b
print(dzielenie)
dzielenie= a/c
print(dzielenie)
dodawanie=a+b
print(dodawanie)
dodawanie=a+c
print(dodawanie)
mnozenie=a*b
print(mnozenie)
mnozenie=a*c
print(mnozenie)
potega=a**b
print(potega)
potega=a**c
print(potega)

#ZADANIE 3

a=2
a+=1
print(a)
b=5
b-=1
print(b)
c=2
c*=3
print(c)
a=10
a/=2
print(a)
a=5
a**=2
print(a)
a=10
a%=3
print(a)

#ZADANIE 4
a = e
a**=10
print(a)

