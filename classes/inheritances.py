class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def who_are_you(self):
        print(f"I am {self.name}")

    def how_old_are_you(self):
        print(f"I am {self.age} years old")


class Student(Person):

    def __init__(self, name, age, year):
        super().__init__(name, age)
        self.graduation_year = year

    def welcoming(self):
        print(f"Hello, I'm {self.name} and I'm {self.age}. I was graduated at {self.graduation_year}")


student01 = Student("John", 20, 2020)
student02 = Student("Nana", 22, 2023)
student03 = Student("Mina", 19, 2021)

print("=========================================")

student01.who_are_you()
student02.who_are_you()
student03.who_are_you()

print("===========================================")

student01.how_old_are_you()
student02.how_old_are_you()
student03.how_old_are_you()

print("===========================================")

student01.welcoming()
student02.welcoming()
student03.welcoming()
