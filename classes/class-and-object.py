class Parrot:
    # attributes
    species = "bird"

    # instance attributes
    def __init__(self, name, color, age):
        self.name = name
        self.color = color
        self.age = age


# instantiate the Parrot class
blu = Parrot("Blu", "Red", 10)

# access the class attributes

print("Blu is a {}".format(blu.__class__.species))

# access the instance attributes
print("{}'s color is {} and his age is {}".format(blu.name, blu.color, blu.age))

