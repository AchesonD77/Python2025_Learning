# build-in modules
# python comes with a standard library that contains serveral modules for common tasks.
# there are a lot of functions we can reuse!
# google: python 3 module index

# generate random modules
import random

# object -> random
for i in range(3):
    # print(random.random()) # print 0-1 random values
    print(random.randint(20,50)) # print ages incluing.

# another way to choose a person
numbers = ['Dan', 'Kaka', 'Messi', 'Pepe', 'Wang']
leader = random.choice(numbers)
print(leader)





