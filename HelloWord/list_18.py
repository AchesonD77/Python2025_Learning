# list
# 1. list of name
names = ['Dan', 'J', 'Patrick', 'W', 'F']
# 2. using index in list to find a specific/particulare value, starting from 0. -1 means first item end of the list.
# 3. don't change the list, creat a new one.
names[0] = 'D'
print(names[2])
print(names[-2])
print(names[2:])
print(names[2:4]) # 'p' 'w'
print(names)

# 4. write a program to find the largest number in a list
numbers = [3, 6, 9, 11, 23, 1]
max = numbers[0]
for number in numbers:
    if number > max:
        max = number
print(max)