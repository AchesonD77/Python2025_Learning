# we use classes to define new types, a different kind of thing, to model real concepts
# numbers/strings/boolean/lists/dictionaries
# for variables and functions, we always use lower case letter, in here,
# we capitalize the first letter of ever word.(For Class)

# we use classes to define new types, also have attributes that we can set anywhere in our programs.
class Point:
    # constructor:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        print('move')

    def draw(self):
        print('draw')


point1 = Point(15, 20)
point1.x = 10

print(point1.x, point1.y)

# define a class called person
'''
person
    -name
    -talk
'''
class Person:
    # define name
    def __init__(self, name):
        self.name = name
    def talk(self):
        print('talk')
    def talk_special(self):
        print(f"Hi, I am {self.name}")


john = Person("john smith")
john.talk()
# print(john.name)
john.talk_special()

# another example:
bob = Person("Dan")
bob.talk_special()