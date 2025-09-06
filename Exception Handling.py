# a= int(input("Enter the number: "))
# print(f"Multiplication of table of {a} is: ")


# try:
#     for i in range(1,6):
#         print(f"{a} X {i} = {a*i}")
#         # print(f"{int(a)} X {i} = {int(a)*i}")
#         # print("Print of table is", (a), "X" (i), "=" (a*i))
        
# except:
#     print("Invalid Error")
    
# print("Some imp lines of code")
# print("End of the program")



try:
    num= int(input("Enter an integer: "))
    a= [6,3]
    print(a[num])
except ValueError:
    print("Number entered is not an integer")
    
except IndexError:
    print("IndexError")    