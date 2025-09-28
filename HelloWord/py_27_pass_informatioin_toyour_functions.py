# 1. we can add parameters
# 1. we define a local variable that we defined inside of this function,
# it has specific purpose and put them inside a function
def greet_user(first_name, last_name):
    print(f"Hi, {first_name} {last_name}!")
    print('welcome aboard!')

print('Start')
# 2. if we set a parameter, we must to put a argument
# parameters = when we define the function()
# argument =  when we give the real information
# 3. positional arguments:
greet_user("Wu", "Dan")
# 4. keyword argument, but most of time we use positional arguments:
greet_user(last_name="Feng", first_name="Li")
# we can use it to increase the readability of this code by using keyword arguments
# calc_cost(total=50, shipping=5, discount=0.1)

# 5. It is a rule, We can only use positional arguments first, and then keyword arguments.
print('Finish')