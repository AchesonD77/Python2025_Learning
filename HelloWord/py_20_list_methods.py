# list methods -> list.method()
numbers = [5, 2, 1, 7, 4]
numbers2 = numbers.copy()
# 1. append() add a number in the end of the list
numbers.append(20)
print(numbers)
# 2. insert() choose an index and put what we want
numbers.insert(0, 10)
print(numbers)
# 3. remove() remove an item, put which value you want delete
numbers.remove(5)
print(numbers)
# 4. pop() remove the last one item in our list
numbers.pop()
print(numbers)
# 5. index(), call the index method to identify if the item in our list, return the index of it
print(numbers.index(10))
# another way to check, in operator. return True or False
print(50 in numbers)
# 6. count() check how many the same items in our list
print(numbers.count(1))
# 7. sort() method, it did the job but don't return any values
numbers.sort()
print(numbers)
# 8. reverse() , simply reverse out list
numbers.reverse()
print(numbers)
# 9. copy(), we can get a copy in new variable
print(numbers2)
# . clear all the list
numbers.clear()
print(numbers)