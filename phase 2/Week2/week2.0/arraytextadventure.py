# version 2 of text game 
import sys 
import numpy as np
name = input('Welcome to the game! Enter your name?')
print("\nGame starting...")
print('\nWell Hello ' +name+ '!!!.')
print("You find yourself in a dark room. There are two doors in front of you.")
print('\nPlease pick a room:')

# Text Adventure Game with Map

# Define the rooms and their descriptions
rooms = {
    "Start":  "There is a door to the east and south.",
    "Blue Door": "You are in the Blue room. You dead. Gameover",
    "Red Door": "You are in the Red room. There are doors to the east and south.",
    "Gold Door": "You are in the Gold room. There are doors to the west, east and south.",
    "Ice Door": "You are in the Ice room. There are doors to the west and east.",
    "Fire Door": "You are in the Fire room. You dead.",
    "EXIT": "Congratulations! You have reached freedom.",
    "EXIT1": "Congratulations! You have reached freedom."
}
# Define the game world as a 2D array
game_map = [
    ["Start", "Red Door" ,"Brass Door"],
    ["Blue Door","Gold Door" , "EXIT1"],
    ["EXIT", "Ice Door", "Fire Door"]
]

# Set up the initial room and player's position
current_room = (0, 0)

# Main game loop
while True:
    # Print the current room description
    print(rooms[game_map[current_room[0]][current_room[1]]])

    # Print the map
    for row in game_map:
        for cell in row:
            if cell == game_map[current_room[0]][current_room[1]]:
                print("[P]", end="")  # Player's current position
            else:
                print("[ ]", end="")  # Explored cell
        print()

    # Get user input for the next move
    move = input("Enter a direction: ").lower()

    # Check user input and update the current room
    if game_map[current_room[0]][current_room[1]] == "Red Door":
        print("You entered the Red Door!")
        break
    if game_map[current_room[1]][current_room[0]] == "Blue Door":
        print("You entered the Blue Door!")
        break
        sys.exit(0)
 


    elif move in ["south", "east", "north", "west"]:
        # Update the current room based on the user's move
        if current_room[1] < len(game_map[current_room[0]]) - 1 and move == "east":
            current_room = (current_room[0], current_room[1] + 1)
        elif current_room[0] < len(game_map) - 1 and move == "south":
            current_room = (current_room[0] + 1, current_room[1])
        else:
            print("You can't move further in this direction.")  


    if move == "quit":
        print("Thanks for playing. Goodbye!")
        break
    else:
        print("Invalid input. Please enter 'north', 'south', 'east', 'west' or 'quit'.")

#import numpy as np
#map_array = np.array([['Room1' ,'Room2]'],['Room 3','Room 4']], dtype:='str') # Use dtype='str' for string elements
#print(map_array)












