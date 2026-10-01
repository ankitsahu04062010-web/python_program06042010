a = int(input("Enter first side of triangle --> "))
b = int(input("Enter first side of triangle --> "))
c = int(input("Enter first side of triangle --> "))
if a+b > c and b+c> a and c+a>b :
    if a!=b and b!=c and c!=a :
        if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or c**2 + b**2 == a**2 :
        print("it is an right angle triangle")
        else:
        print ("it is an scalen tringle")
    elif a==b==c :
    print("it is an equiulateral triangle")
    else :
    print("it is an issoscales triangle")
else :
    print("It doesn't form a triangle")
