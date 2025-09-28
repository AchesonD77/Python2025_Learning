# powerful unpacking, same results with far less code
# use tuples
coordinates = (1, 2, 3)
'''
x = coordinates[0]
y = coordinates[1]
z = coordinates[2]
'''
x, y, z = coordinates
print(y)

# we can use this feature in list too
coordinates_list = [1, 2, 5]
x, y, z = coordinates_list
print(z)
