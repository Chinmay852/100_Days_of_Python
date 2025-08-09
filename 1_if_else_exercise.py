applePrice = 210
budget = int(input("Enter your Budget: "))

if(applePrice <= budget):
    budget -=applePrice
    print("Apples are added to the cart")
    print("Updated Balance: ", budget)
else:
    print("Insufficient Balance")
    