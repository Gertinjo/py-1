from email.policy import default

from globalkeyword1 import message, greet


def greet_person(name,greeting="Hello"):

    message= f"{greeting}, {name}"

    return message

default_greating = greet_person("Gert")

custom_greeting = greet_person("Dren" , "Hi")

print(default_greating)
print(custom_greeting)