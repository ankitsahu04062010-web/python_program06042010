temp = int(input("Enter your local temprature"))
if 2< temp <= 20 :
    print("Winter")
if 21< temp <= 25 :
    print("Spring")
if 25< temp <=  48  :
    if 30 <= temp <= 38 :
        print("Monsoon")
    else :
        print("Summer")