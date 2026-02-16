
try:
   result = 10/0
except ZeroDivisionError :
    print("There is a error")


fruits = {
    "apple": 5,
    "Bannana": 7,
    "orange": 3
}

try:
    print(fruits["cherry"])
except KeyError:
    print("The key does not exist")