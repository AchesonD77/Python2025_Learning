# make sure indented
is_hot = False
is_cold = True
if is_hot:
    print("It is a hot day!")
    print("Drink plenty of water!")
elif is_cold:
    print("It is a cold day!")
    print("Wear warm clothes!")
else:
    print("It is a lovely day!")
print("Enjoy your day!")

# exercise buying house with credit
is_good_credit = True
price = 1
print(type(price))
print("House price is $" + str(price) + "M")
if is_good_credit:
    down_payment = price * 0.1
else:
    down_payment = price * 0.2
print("After we checked your credit, House down payment can be  $" + str(down_payment) + "M")
# a good expression
print(f"Down payment shoud be: ${down_payment} M" )

