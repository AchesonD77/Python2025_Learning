# A good exercise for convert pounds to kilograms
# input function always return the string
weight = int(input("Weight: "))
unit = input('(L)bs or K(g): ')
if unit.upper() == 'L':
    converted = weight * 0.45
    print(f"You are {converted} kilos")
elif unit.upper() == 'K':
    converted = weight / 0.45
    print(f'You are {converted} pounds')
else:
    print("Wrong input! Try again!")