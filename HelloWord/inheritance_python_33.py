# iniheritance in python, most lauguages have it.

class Mammal:
    def walk(self):
        print("walk")


# inherit from Mammal
class Dog(Mammal):
    # if we don't add other functions, just use pass
    # pass
    def bark(self):
        print("bark")


class Cat(Mammal):
    pass

dog1 = Dog()
dog1.walk()
dog1.bark()