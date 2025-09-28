# creating reusable functions
# reorganize the py_25_dictionary_emoji_convert_exercise.py to be a new reusable function
# we don't set up input and output, because maybe they have different ways.
# each function can only work on one specific task, and we neet to show the task through our define name

# define it
def emoji_convert(message):
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
    # return statement
    return output
# remember after define a function, we need to make two blank lines


# call it
message = input(">")
print(emoji_convert(message))

