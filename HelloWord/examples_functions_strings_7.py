# function len(), calculate the number of strings, calculate the number of items in a list
# to enter the specific methods (belongs to somethings, is specific to some objects) (functions) for strings -> strings.
course = 'Python for Beginners'
print(len(course))
print(course.upper())
print(course.lower())
print(course)
# find method: find index string.find(''), return the index, is sensitive to lower and upper,
# if it doesn't exist, return -1, also we can put the whole word, it returns the first index.
print(course.find('f'))
print(course.find('N'))

# replace method
print(course.replace('Beginners', 'Absolute Beginners'))
print(course.replace('P', 'J'))

# in operate to check if we have the words in the strings. return boolean value
print('python' in course)
print('Python' in course)

# title method: it capitalizes the first letter of each word in the string
print(course.title())
