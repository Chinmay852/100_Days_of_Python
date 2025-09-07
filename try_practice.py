# try:
#     a=int(input("Enter a number: "))
# except ValueError:
#     print("Enter a valid number")
    
    
try:
    num=int(input("Enter an string: "))
    a=("chinmay","kiran")
    print(a[num])
except IndexError:
    print("Index not defined")
    