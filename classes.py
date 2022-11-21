class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Hello, I'm {self.name} and I'm {self.age} years old"


first_person = Person("Nana", 20)

print(first_person)
# The __init__() function is called automatically every time the class is being used to create a new object.
