# #reading a file
# f = open("myfile.txt", "r")
# text = f.read()
# print(text)
# f.close()

# f=open('myfile2.txt', 'a')
# f.write(" Hello World")
# f.close()

with open('myfile.txt', 'a') as f:
    f.write("Hello World")