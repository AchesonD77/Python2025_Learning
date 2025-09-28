# 1. for loop, iterate over items. each character of string.
for item in 'Python':
    print(item)

# 2. define lists using square brackets [], a list of a lot of things.
for item in ['Dan', 'John', 'Ronaldo']:
    print(item)

for item in [1, 2, 3, 4, 'stop']:
    print(item)

# 3. range() function to create a range of numbers (10); (5, 10); (5, 10, 2); start from the first default number is 0;
for item in range(5, 10, 2):
    print(item)

# 4. exercise
# we can change the name of item to whatever we want. We define a variable out of the loop
prices = [13, 23, 44]
total = 0
for price in prices: # price meanseach iteration value from prices list.
    total += price
print(f"Total money: {total}")


