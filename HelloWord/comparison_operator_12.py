# comparison operator
temperature = 35

# we have >=,>,<=,<,==,!=
if temperature > 30:
    print("It is a hot day!")
else:
    print("It is not a hot day!")

# exercise test name length to output warning
name = input("Your name: ")
print(f"Your name is: {name}")
if len(name) < 3:
    print(f'WARNING: your name length is {len(name)}, name must be at least 3 characters')
elif len(name) > 50:
    print(f'WARNING: your name length is {len(name)}, name must be a maximum of 50 characters')
else:
    print(f'Congratulations: your name length is {len(name)}, it is a good name!')