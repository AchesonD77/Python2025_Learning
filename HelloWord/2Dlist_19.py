# two dimensional lists, data science and machine learning
# math - matrix, rows and colonms
# one list nested one list
'''
[
    1 2 3
    4 5 6
    7 8 9
]
'''
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# how do we access this matrix?
# we can also directly change it
matrix[0][0] = 2
print(matrix[0][1])
for row in matrix:
    for item in row:
        print(item)
    print("\n")

