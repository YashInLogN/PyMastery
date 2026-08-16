class PEOPLE:

    status = True # Active

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

class MALE(PEOPLE):

    def greet(self):
        print(f"Mr.{self.name} saying you hello")

class FEMALE(PEOPLE):

    def greet(self):
        print(f"Mrs.{self.name} told you to fuckoff")


gender = input("Gender: ")
cls = MALE if gender.lower() == "male" else FEMALE

class_1 = cls(name := input("Name: "), age := int(input("Age: ")), gender)

# class_2 = cls(name := input("Name: "), age := int(input("Age: ")), gender)

class_1.greet()
print(class_1.status)
print(issubclass(MALE, PEOPLE))
print(isinstance(MALE, PEOPLE))