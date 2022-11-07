class Parrot:
    # instance attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # instance method
    def sing(self, sing):
        return f"{self.name} sings {sing}"

    def dance(self):
        return f"{self.name} is now dancing"


# instantiate the object
blu = Parrot("Blu", 10)

# call our instance methods
print(blu.sing("'Happy'"))
print(blu.dance())
