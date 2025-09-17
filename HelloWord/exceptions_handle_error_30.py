# handle exceptions!

# 2. avoid crash
# run successfully, we can set this function to avoid crash
# Process finished with exit code 0
# code 1 means crash, we need to watch the type of error.
# how can we handle the errors
try:
    age = int(input('Age(cannot be alpha letter): '))
    print(age + age)
except ValueError:
    print("Invalid value")

# 3.
try:
    age = int(input('Age(Don\'t insert 0): '))
    income = 20000
    risk = income / age
    print(age)
except ZeroDivisionError:
    print('Age cannot be 0.')
except ValueError:
    print("Invalid value")

# 1. a small program get the user's age from terminal
age = int(input('The Age after ages: '))
print(age+age)