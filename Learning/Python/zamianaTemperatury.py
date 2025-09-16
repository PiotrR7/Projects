print("-----------------")
#zamiana 100 stopni celsjusza na fahrenheita
def temperatura():
    print("100°C to",(100*9/5)+32,"°F")
    
# wyświetlenie obliczen
temperatura()



print("-----------------")
# zamiana temperatury podanej przez użytkownika °C na °F
def temperatura2(x):
    print(x,"°C to",(x*9/5)+32,"°F")

#pobranie zmiennej
x=int(input("podaj °C:"))

# wyswietlenie obliczen
temperatura2(x)




print("-----------------")
# zamiana temperatury podanej przez użytkownika °F na °C
def temperatura3(y):
    print(y,"°F to",(x-32)*5/9,"°C")

#pobranie zmiennej
y=int(input("podaj °F:"))

# wyswietlenie obliczen
temperatura3(y)