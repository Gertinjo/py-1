from tabnanny import check

names = ["Dreni", "Gerti" , "Deon", "Amant"]

for name in names :
    print(name)

# numbers = ["1", "2", "3"]
#
# for number in numbers:
#     print(number)
fjali = "Hello , World"

for shkronja in fjali :
    if not shkronja.isalpha():
        print(shkronja)


for x in range(1,6) :
    print(x)

numbers = [12 , 35 ,45 , 20 ,65, 22 , 21, 16 , 8 ,4]
maximum = numbers[0]
for number in numbers :
        if maximum < number:
            maximum = number
print(maximum)
