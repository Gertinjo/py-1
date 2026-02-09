greeting = "Hello"
name ="Gerti"

def greet():

    global greeting
    greeting = "Goodbye"

    name ="Dren"

    message = f"{greeting}, {name}"
    print(message)


greet()

print(greeting)

print(name)