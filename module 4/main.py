# count = 1
# while count <= 18:
#     print("Number", count)
#     count += 1
while True:
    user_input = input("Enter a postive number: ")

    if user_input.isnumeric():
        number = int(user_input)
        if number > 0:
            break


    print("Invalid input. Please try again.")
print("You entered a valid positive number: ", number)