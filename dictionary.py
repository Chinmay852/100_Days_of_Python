# dict = {
#     852: "Chinmay",
#     565: "Shivam"
# }

# print(dict["Chinmay"])

info= {"name":"Chinmay", "age":23, "eligible":True}
print(info.keys())
print(info.values())

for key, values in info.items():
    print(f"The value of corresponding to the key {key} is {values}")