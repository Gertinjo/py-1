greating = "Hello"

def greet(name):

    global  message

    message = f"{greating}, {name}"
    print(message)

greet("Gerti")
print(message)


message = f"{greating}, student!"
print(message)