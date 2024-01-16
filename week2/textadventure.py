# text adventure game 

# first of all what is this startgame() = it's a function call

name = input('Please enter you name:')
print('\nHello ' + name + '!!!')

#"def" is a keyword that indicates the beginning of a function definition.
def startgame():
    print("\nWelcome to the Text Adventure Game " + name + '!!')
    print("You find yourself in a dark room. There are two doors in front of you.")

# "\n" is an escape sequence representing a newline to seperate from the top line. for better formattin
#  while True: creates an infinite loop.
    while True:
        print("\nOptions:")
        print("1. Go through the left door")
        print("2. Go through the right door")
        print("3. Quit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            print("\nYou enter a magical garden. You win!")
            break
        #break - break the loop
        # if else 
        elif choice == "2":
            print("\nYou enter a dragon's lair.")
            print("You lose. Game Over.")
            restart = input("Would you like to restart try again?")
            # added .lower() to make it case-insensitive.
            if restart.lower() == "yes":
                print("\nRestarting the game...")
            else: 
                print("BYE BYE.")
            continue
        #continue - the true program
        elif choice == "3":
            print("\nQuitting the game...")
            print("Goodbye!")
            break
        else:
            print("BYE BYE.")

if __name__ == "__main__":
    startgame()

# The if __name__ == "__main__": block checks if the script is being run as the main program (not imported as a module).
#If it is the main program, it calls the startgame() function.