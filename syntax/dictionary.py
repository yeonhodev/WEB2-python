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

#numbers 내부에 들어있는 숫자가 몇 번 등장하는지를 출력하는 코드
numbers = [1,2,6,8,4,3,2,1,9,5,4,9,7,2,1,3,5,4,8,9,7,2,3]
counter = {}

for number in numbers:
    if number in counter:
        counter[number] += 1
    else:
        counter[number] = 1

print()
print(counter)

#Falttening
character = {
    "name": "기사",
    "level": 12,
    "items": {
        "sword": "불꽃의 검", 
        "armor": "풀플레이트"
    },
     "skill": ["베기", "세게 베기", "아주 세게 베기"]
}

print()
for key in character:
    if type(character[key]) is dict:
        for k in character[key]:
            print("{} : {}".format(k, character[key][k]))
    elif type(character[key]) is list:
        for item in character[key]:
            print("{} : {}".format(key, item))
    else:
        print("{} : {}".format(key, character[key]))