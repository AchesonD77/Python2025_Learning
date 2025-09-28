# write a car game， using while method, store in the memory, not boolean value
print(f"Welcome to our car game!")
command = ''
started = False
# true + break
while True:
    command = input("> ").lower()
    if command == 'start':
        if started:
            print("Warning: Car is already started!")
        else:
            started = True
            print("Car started...")
            # after this block, the started value is True.
    elif command == 'stop':
        if not started:
            print("Warning: Car is already stopped!")
            # started stays False.
        else:
            started = False
            print("Car stopped.")
            # after this block, the started value is False.
    elif command == 'help':
        print("""
start - to start the car
stop - to stop the car
quit - to quit
        """)
        command = ''
    elif command == "quit":
        break
    else:
        print("Sorry, I don't understand that.")

