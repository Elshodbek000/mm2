def maxSon(a,b,c):
    if a>b and a>c:
        return a;
    elif b>a and b>c:
        return b;
    elif c>a and c>b:
        return c;
    else:
        print("Barchasi teng!")

a=10
b=10
c=10

kataSon = maxSon(a,b,c)

print("Kata son: ", kataSon) 
def maxSon(a,b,c):
    if a>b and a>c:
        return a;
    elif b>a and b>c:
        return b;
    elif c>a and c>b:
        return c;
    else:
        return "Barchasi teng!";

def toqYokiJuft(son):
    if son%2==0:
        print("Juft son: ", son)
    else:
        print("Toq son: ", son)

a=int(input("A: "))
b=int(input("B: "))
c=int(input("C: "))

kataSon = maxSon(a,b,c)

print("Katta son: ", kataSon)
toqYokiJuft(kataSon)