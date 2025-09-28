# string syntax
# python's courses for beginners
# we use "" to make this when we use '', vice versa
course = "python's courses for beginners"
course2 = 'python for "Beginners"'
print(course)
print(course2)

# three quotes to define long sentences. """ or '''
text1 = '''
Hi, john.
How are you?
Here is your support team,
Best regards.
'''
print(text1)

# get character, 0 is the first one, -1 is the last one
get_character = "Python is a good code language"
print(get_character[0])
print(get_character[-2])
# 0:3 start from 0 to 3-1 character
print(get_character[0:3])
# print all, we don't imply the end index
print(get_character[1:])
# we don't use the first index
print(get_character[:7])
# copy string variable
copy_get_character = get_character[:12]
print(copy_get_character)

# exercise
name = 'Jennifer'
print(name[1:-1])
# the result will start from character 'e', and end at 'e' exclusive the last one character 'r'