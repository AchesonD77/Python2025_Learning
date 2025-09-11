# converting one type(string) to another type
# 2025 - "2000" : a interger minus a string, wrong!
# case all we get from input fuction, it is a string!
# int() float() bool()
# There is a very useful function to get the type of variable.
birth_year = input("Birth year: ")
print(type(birth_year))
# old wrong version, age = 2025 - birth_year
age = 2025 - int(birth_year)
print(age)
print(type(age))

# example convert pounds to kilograms
weight_pounds = input("Hi, Bro, What is your weight(in pounds)? ")
weight_kilograms = 0.45359237 * float(weight_pounds)
print( str(weight_kilograms) + " kilograms ")


