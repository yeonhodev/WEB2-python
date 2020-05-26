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