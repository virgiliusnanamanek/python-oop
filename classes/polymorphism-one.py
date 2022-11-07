class Car:
    def __init__(self, types, color):
        self.type = types
        self.color = color

    def wheels(self):
        print(f"{self.type} is 4 wheels")

    def color_type(self):
        print(f"All {self.type} are {self.color}")


class Mercedez(Car):
    def __init__(self, types, color):
        super().__init__(types, color)

    def color_type(self):
        print(f"{self.type}'s color is {self.color}")


class Tesla(Car):
    def __init__(self, types, color):
        super().__init__(types, color)

    def color_type(self):
        print(f"{self.type}'s color is {self.color}")


class Ferary(Car):
    def __init__(self, types, color):
        super().__init__(types, color)

    def color_type(self):
        print(f"{self.type}'s color is {self.color}")


obj_car = Car("Cars", "colorful")
obj_merci = Mercedez("Mercedes", "gray")
obj_tesla = Tesla("Tesla", "black")
obj_ferary = Ferary("Ferary", "yellow")

obj_car.wheels()
obj_merci.wheels()
obj_tesla.wheels()
obj_ferary.wheels()

obj_car.color_type()
obj_merci.color_type()
obj_tesla.color_type()
obj_ferary.color_type()
