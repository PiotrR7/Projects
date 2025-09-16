#data=["parzysta" if x % 2==0 else "nieparzysta" for x in range(5)]
#print(data)

#data=[]
#for x in range(5):
#    if(x%2==0):
#        data.append("parzysta")
#    else:
#        data.append("nieparzysta")
#
#print(data)

for x in range(0,2023):
    if x%4==0 and (x%100!=0 or x%400==0):
        print(x,"rok przestępny")
    else:
        print(x,"rok nieprzestępny")

rok_przestępny=["przestępny" if x%4==0 and (x%100!=0 or x%400==0) else "nieprzestępny" for x in range(0,2023) ]
print(rok_przestępny)