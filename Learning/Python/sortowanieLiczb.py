parzyste=[]
nieparzyste=[]
liczby=[]

for x in range(0,10):
    a=int(input('podaj liczbe: '))
    liczby.append(a)
    if a%2==0:
        parzyste.append(a)
    elif a%2!=0:
        nieparzyste.append(a)

print('Przed sortowaniem')
print('parzyste',parzyste)
print('nieparzyste',nieparzyste)
print('wszystkie liczby',liczby)



for x in range(len(parzyste)):
    for y in range(0,len(parzyste)-x-1):
        while parzyste[y] > parzyste[y+1]:
            pom=parzyste[y]
            parzyste[y]=parzyste[y+1]
            parzyste[y+1]=pom

for h in range(len(nieparzyste)):
    for g in range(0,len(nieparzyste)-h-1):
        while nieparzyste[g] > nieparzyste[g+1]:
            pom=nieparzyste[g]
            nieparzyste[g]=nieparzyste[g+1]
            nieparzyste[g+1]=pom




print('Po sortowaniu')
print('parzyste',parzyste)
print('nieparzyste',nieparzyste)
