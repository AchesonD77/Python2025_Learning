# while loops, excute a block of codes multiple times.
# while method, basical of while
count_number = 1
while count_number <= 5:
    print(count_number)
    count_number = count_number + 1
print("Done")
# a simple game
count_number = 1
while count_number <= 5:
    print("*" * count_number)
    count_number = count_number + 1
print("Done")

# A guess game
secret_number = 9
# rename all the characters
count_number = 0
guess_limit = 3
while count_number < guess_limit:
    guess = int(input(f"Guess: "))
    count_number += 1
    if count_number < guess_limit-1:
        print("Try again!")
    if count_number == (guess_limit-1):
        print("Last chance")
    if guess == secret_number:
        print("You won!")
        # break: terminate the loop
        break
else:
    print("Sorry, you faild!")



