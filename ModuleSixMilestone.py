# Name: Tristan Smith
# ModuleSixMilestone.py
# This program runs a simplified text-based game where the player can move between rooms or exit the game.
# It uses a dictionary to define valid movements between rooms and validates player input.

# Color codes for terminal output, as it gets too unreadable/unplayable without them
RESET = "\033[0m"
RED = "\033[91m"
GREEN = "\033[92m"

# A dictionary for the simplified dragon text game featured in IT140
# The dictionary links a room to other rooms.
rooms = {
    'Great Hall': {'South': 'Bedroom'},
    'Bedroom': {'North': 'Great Hall', 'East': 'Cellar'},
    'Cellar': {'West': 'Bedroom'}
}

def main():
    current_room = 'Great Hall'   # The player starts in the Great Hall
    while current_room != 'exit':
        # Display the current room
        print(f"You are currently in the {current_room}.")

        # Display available directions in this room
        available_directions = list(rooms[current_room].keys())
        print("Available directions from here:", ", ".join(available_directions))

        # Prompt the player for a command
        command = input("Enter a direction (North, South, East, West) or 'exit' to quit: ").strip()

        # Check if the player wants to exit
        if command.lower() == 'exit':
            current_room = 'exit'
            print("You have chosen to exit the game. Goodbye!")
        else:
            # Convert first letter of direction to uppercase to match dictionary keys (e.g. 'north' -> 'North')
            direction = command.capitalize()

            # Check if the direction is valid in the current room
            if direction in rooms[current_room]:
                # Move the player to the next room
                next_room = rooms[current_room][direction]
                current_room = next_room
                print(GREEN + f"You move {direction} and arrive at {current_room}.\n" + RESET)
            else:
                # Invalid direction - RED seems to be a good attention grabber
                print(RED + "You cannot go that way! Please try another direction.\n" + RESET)

    # The loop ends once current_room == 'exit'

if __name__ == "__main__":
    main()
