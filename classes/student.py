class Student:
    # instance methods to initialize the content of an object
    def __init__(self, name, house):
        self.name = name
        self.house = house


def main():
    # name = get_name()
    # house = get_house()
    # name, house = get_student()
    student = get_student()
    # sentence = f"{name} from {house}"
    # sentence = f"{student[0]} from {student[1]}"
    sentence = f"{student.name} from {student.house}"
    print(sentence)


# def get_name():
#     return input("Name: ")
#
#
# def get_house():
#     return input("House: ")

def get_student():
    # name = input("Name: ")
    # house = input("House: ")
    # # return name, house
    # return name, house
    name = input("Name: ")
    house = input("House: ")
    student = Student(name, house)
    return student


if __name__ == "__main__":
    main()
