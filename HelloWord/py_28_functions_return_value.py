# 1. function: return statement: It is very useful to return what you want to get the value.
def square(number):
    return number * number


# 2. store it (the return value) in a variable
result = square(3)
print(result)

# 3. an easy output
print(square(5))

# 4. by return, in default, all the fuctions will return none
def plus_itself(number):
    print(number+number)
    return None


print(plus_itself(9))