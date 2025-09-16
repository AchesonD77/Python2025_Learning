# 1. nested loop, adding one loop inside of another loop
# we can do some amazing things, like easily generate a list of coordinates
for x in range(4):
    for y in range(3):
        print(f'({x},{y})')
    print(f"\n")

# 2. chanllenging - creating a F shape
numbers = [5, 2, 5, 2, 2]
for x in numbers:
    output = ""
    for y in range(x):
        output += 'X'
    print(output)