tablica=['2','7','8','4','3']
dl=len(tablica)

for x in range(dl):
    for y in range(0,dl-x-1):
        if tablica[y]>tablica[y+1]:
            pom=tablica[y]
            tablica[y]=tablica[y+1]
            tablica[y+1]=pom

print(tablica)