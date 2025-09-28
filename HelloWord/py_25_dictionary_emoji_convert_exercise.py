# exercise in dictionary

# 1. input
message = input(">")

# 2. split("")
# message.split(" "), method uses " " to seperate the string
words = message.split(" ")
print(words)

# 3. define a dictionary mapping, mac : control + command + space
emojis = {
    ":)": "😜",
    ":(": "😞"
}
# output
output = ""

# 4. for loop to see if we have the items to map the key
# we use get() method again: get(word, word), to return we input but don't have in our dictionary
for word in words:
    output += emojis.get(word, word) + " "
print(output)
