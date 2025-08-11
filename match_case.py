x= int(input("Enter your number: "))
match x:
    case 0:
        print("x is zero")
        
    case _ if x!=0:
        print("You didnt choose zero")