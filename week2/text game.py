# version 3 of text game 

name = input('Welcome to the game! Enter your name?')
print("\nGame starting...")
print('\nWell Hello ' +name+ '!!!.')
print("You find yourself in a dark room. There is a door on the south and the east, select one:")
print('\nPlease pick a room:')

# Text Adventure Game with Map

# Define the rooms and their descriptions
rooms = {
    "Blue Door": "You are in the Blue room. You dead. Gameover",
    "Red Door": "You are in the Red room. There are doors to the east and south.",
    "Gold Door": "You are in the Gold room. There are doors to the west, east and south.",
    "Ice Door": "You are in the Ice room. There are doors to the west and east.",
    "Fire Door": "You are in the Fire room. You dead.",
    "EXIT": "Congratulations! You have reached freedom."
}
# Define the game world as a 2D array
game_map = [
    ["Start", "Red Door" ,"Brass Door"],
    ["Blue Door","Gold Door" , "EXIT"],
    ["EXIT", "Ice Door", "Fire Door"]
]

# Set up the initial room and player's position
current_room = (0, 0)

if current_room == 1:
    location = "Red Door"
    action = "discover"
elif current_room == 2:
    location = "Blue door"
    action = "explore"
else:
    location = "Mysterious Caves"
    action = "enter"
    
for row in game_map:
        for cell in row:
            if cell is None:
                print("   ", end="")  # Empty cell
            elif (game_map.index(row), row.index(cell)) == current_room:
                print("[P]", end="")  # Player's current position
            else:
                print("[ ]", end="")  # Explored cell
        print()
# Main game loop
while True:
    # Get user input for the next move
    move = input("Enter a direction (south/east/north/west/quit): ").lower()
    if move == "quit":
        print("Thanks for playing. Goodbye!")
    