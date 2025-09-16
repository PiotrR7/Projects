napis="To jest napis, który będzie przeszukiwany"

def czywystepuje(x):
    if(x in napis):
        print("jest w ciągu")
    else:
        print("nie ma w ciągu")
x=input(":")

czywystepuje(x)