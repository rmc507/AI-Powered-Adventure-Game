import random
import summarize_game
#from get_response import get_response  # Import the get_response function
from get_response_ollama import get_response
from game_data import people, places  # Import the people and places
import subprocess
USER = "Robert"
player_location = "town"

# World map with coordinates and corresponding locations
world_map = [
    ["woods", "dungeon", "mountain"],
    ["cave", "town", "forest"],
    ["river", "lake", "bridge"]
]


# Player's initial position in the world map
player_x, player_y = 1, 1

def whereis(x, y):
    """Returns the name of the location at given coordinates."""
    location = world_map[y][x]
    if location == "blank":
        return "This place is inaccessible."
    return location

def describe_location():
    """Describes the current location using the get_response function."""
    location = whereis(player_x, player_y)
    if location != "blank":
        return get_response("Narrator", people["nar"], places[location]) 
    return "You can't see anything here."

def move(direction):
    """Moves the player based on direction."""
    global player_x, player_y
    if direction == "up" and player_y > 0 and world_map[player_y - 1][player_x] != "blank":
        player_y -= 1
        print("You moved up.")
    elif direction == "down" and player_y < len(world_map) - 1 and world_map[player_y + 1][player_x] != "blank":
        player_y += 1
        print("You moved down.")
    elif direction == "left" and player_x > 0 and world_map[player_y][player_x - 1] != "blank":
        player_x -= 1
        print("You moved left.")
    elif direction == "right" and player_x < len(world_map[0]) - 1 and world_map[player_y][player_x + 1] != "blank":
        player_x += 1
        print("You moved right.")
    else:
        print("You can't move that way.")

def run_summarize_game():
    try:
        # Run summarize_game.py from within this Python script
        result = subprocess.run(['python', 'summarize_game.py'], capture_output=False, text=False)
        
        
        

        # Check if there was an error
        if result.stderr:
            print("Error:", result.stderr)

    except Exception as e:
        print(f"An error occurred while running summarize_game.py: {e}")

    


def print_yellow(text):
    return f"\033[93m{text}\033[0m"

def print_green(text):
    return f"\033[92m{text}\033[0m"

print(print_green("Enter h for help"))
if __name__ == "__main__":
    print(print_green("Welcome to the adventure, " + USER + "!"))
    print(print_green("This is where the player is: " + whereis(player_x, player_y)))
    
    while True:
        user_input = input(print_yellow(">>> "))

        if user_input == "look":
            print(print_green(describe_location()))
        elif user_input in ["up", "down", "left", "right"]:
            move(user_input)
            print(print_green("You are now at the " + whereis(player_x, player_y)))
            print(print_green(describe_location()))
        elif user_input == "sum":
            run_summarize_game()
        elif user_input == "h":
            print(print_green("('look', 'up', 'down', 'left', 'right', 'sum' to summarize context window, '-' to talk to the blacksmith and '*' to talk to the narrator.)"))
        elif user_input and user_input[0] == '-':
            print(print_green(get_response("Blacksmith", people["blacksmith"], user_input)))
        elif user_input and user_input[0] == '*':
            print(print_green(get_response("Narrator", people["livenar"], user_input)))
        else:
            print(print_green(get_response("Dave", people["dave"], user_input)))
