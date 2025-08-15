def greet(fname, lname):
    print("Hello", fname, lname)
    
greet("Chinmay", "Satam")

def avg(*numbers):
    sum = 0
    for i in numbers:
        sum = sum+i
    print("Average is: ", sum/len(numbers))
    
avg(2,4,8)