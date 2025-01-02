# Text-Based Adventure Game

## Overview

This is a text-based adventure game where the player can explore different locations, interact with characters, and receive descriptions of their surroundings. The game uses various modules to handle different aspects such as summarizing the game context, generating responses from characters, and managing game data.

## How It Works

The game consists of several Python scripts:

- `game.py`: The main script that runs the game. It handles player movement, interactions, and commands.
- `summarize_game.py`: Summarizes the game context by sending conversation history and text content to the Grok API.
- `get_response_ollama.py`: Communicates with the Ollama API to generate responses from characters based on user input.
- `game_data.py`: Contains data about the characters and locations in the game.

## Usage

1. **Run the Game**: Execute the `game.py` script to start the game.
   ```sh
   python game.py
   ```

2. **Commands**:
   - `look`: Describe the current location.
   - `up`, `down`, `left`, `right`: Move the player in the specified direction.
   - `sum`: Summarize the game context by running the `summarize_game.py` script.
   - `h`: Display help message with available commands.
   - `-<message>`: Talk to the blacksmith.
   - `*<message>`: Talk to the narrator.
   - Any other input will be directed to Dave for a response.

3. **Example**:
   ```sh
   >>> look
   >>> up
   >>> sum
   >>> -Hello Blacksmith
   >>> *Tell me a story
   ```

## Modules

- **summarize_game.py**: Loads conversation history and patterns from files, sends them to the Grok API, and updates the conversation history with the summary.
- **get_response_ollama.py**: Manages conversation history and sends prompts to the Ollama API to get character responses.
- **game_data.py**: Defines character and location descriptions used in the game.

## Requirements

- Python 3.x
- `requests` library (install using `pip install requests`)

## Setup

1. Clone the repository or download the source code.
2. Ensure you have Python 3.x installed.
3. Install the required libraries:
   ```sh
   pip install requests
   ```
4. Run the game:
   ```sh
   python game.py
   ```

Enjoy your adventure!