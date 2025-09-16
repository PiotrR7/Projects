a=int(input("podaj rok urodzenia"))
b=int(input("podaj obecny rok"))

#ile lat upłyteło od narodzin
c=int(b-a)
print("od urodzenia upłyneło",c,"lat")

#ile było lat przestępnych od narodzin od obecnego roku
lata_przestępne=[]
for x in range(a-1,b+1):
    if x%4==0 and (x%100!=0 or x%400==0):
        lata_przestępne.append((x,"rok przestępny"))
print(lata_przestępne)

#ile mineło od 1.01 do grudnia tego roku
if x%4==0 and (x%100!=0 or x%400==0):
    d=int(366)
else:
    d=int(365)

print("od 01.01", int(a),"do 31.12",int(b),"mineło",int(c)*(d),"dni")