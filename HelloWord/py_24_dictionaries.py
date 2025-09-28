# in situation we want to store information that comes from key value pairs
# name Dan, email 21321@gmail.com , phone 213333
# this is a bunch of key value pairs
# 1. dictionaries, curly braces, every key value should be unique. values can be anything any type
customer = {
    "name": "Dan",
    "age": 100,
    "is verified": True
}
# 2. access and update
customer["name"] = "Jack"
customer["birthdate"] = "Apr 14 1000"
# 3. print(customer.get("birthdate", "Jan 1 1980"))
print(customer["name"])
print(customer["birthdate"])

# 4. exercise: translate number to number words
# 1. get user's phone number
phone = input("Phone: ")
# 2. core algorithm: we choose dictionaries, because it can map 1 -> one
digits_mapping = {
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four"
}
output = ""
# get() method in dictionary, means our program don't yield people,
# if we don't have the ch in our dictionary, we set a default value.
for ch in phone:
    output += digits_mapping.get(ch , "WRONG") + " "
print(output)




