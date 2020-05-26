#Create a new dictionary
dictionary1 = {
    "keyA": "valueA",
    273: [1, 2, 3, 4],
     True: False
}

#Use with for loop
for key in dictionary1: 
    print("{} : {}".format(key, dictionary1[key]))

#Add a new element
dictionary1["keyB"] = "valueB"
print()
for key in dictionary1: 
    print("{} : {}".format(key, dictionary1[key]))

#Delete a new element
del dictionary1["keyB"]
print()
for key in dictionary1: 
    print("{} : {}".format(key, dictionary1[key]))

#Check if there is a key in dictionary to avoid an error message
if "keyC" in dictionary1:
    print(dictionary1["keyC"])
else:
    print("No keyC is in dictionary1")

#Another way to get value from dictionary and check with if

if dictionary1.get("keyC"):
    print("No keyC in dictionary1")
else:
    dictionary1.get("keyC")

#Add a new dictionary
pets = [
    {"name": "구름", "age": 5 },
    {"name": "초코", "age": 3 },
    {"name": "아지", "age": 2 },
    {"name": "호랑이", "age": 1 }
]
print()
print("# 우리 동네 애완 동물들")
for pet in pets:
    print("{} {}살".format(pet["name"], pet["age"]))

