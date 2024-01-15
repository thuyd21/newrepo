# text adventure game 


# first of all what is this startgame() 

name = input('Please enter you name:')
print('Hello ' + name + '!!!')

def startgame():
    print("Welcome to the Text Adventure Game " + name + '!!')
    print("You find yourself in a dark room. There are two doors in front of you.")

    while True:
        print("\nOptions:")
        print("1. Go through the left door")
        print("2. Go through the right door")
        print("3. Quit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            print("You enter a magical garden. You win!")
            break
        elif choice == "2":
            print("You enter a dragon's lair. Game over!")
            break
        elif choice == "3":
            print("Quitting the game. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    startgame()

# The if __name__ == "__main__": block checks if the script is being run as the main program (not imported as a module).
#If it is the main program, it calls the startgame() function.