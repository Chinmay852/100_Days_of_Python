marks = [12, 56, 32, 98, 12, 45, 1, 4]

# index = 0
# for mark in marks:
#     print(mark)
#     if(index==3):
#         print("Chinmay Awesome")
#     index +=1

for index, mark in enumerate(marks, start=100):
    print(index,mark)
    if(index==3):
        print(index,mark,"Chinmay, Awesome")
    elif(mark==1):
        print(mark,"Work Hard")
        
## NEXT EXAMPLE

fruits = ['Apple', 'Banana', 'Cherry']
for index, fruit in enumerate(fruits):
    print(index,fruit)