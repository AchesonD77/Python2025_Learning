'''
class Dice:
        method -roll()
'''

# 1. import modules
import random


# 2. define class
class Dice:
# 3. define method
    def roll(self):
        first = random.randint(1, 6)
        second = random.randint(1, 6)
        # return a tuple
        return first,second


dice = Dice()
print(dice.roll())
