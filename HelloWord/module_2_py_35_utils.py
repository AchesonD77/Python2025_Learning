# exercsie for training how to organize your code.
def find_max(numbers):
    # if we use max, we are changing the meaning of building-in python function.
    # shift + F6 to rename
    max1 = numbers[0]
    for number in numbers:
        if number > max1:
            max1 = number
    # we need to return statement
    return max1

