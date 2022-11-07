class Penguin:
    def fly(self):
        print("Can't fly")

    def swim(self):
        print("Can swim")


class Bird:
    def fly(self):
        print("Can fly")

    def swim(self):
        print("Can't fly")


def flying_test(bird):
    bird.fly()

pygy = Penguin()
birdy = Bird()

flying_test(pygy)
flying_test(birdy)