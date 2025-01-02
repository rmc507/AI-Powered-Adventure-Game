"""
README

This module handles communication with the Groq API to generate responses from characters in the text-based adventure game.

Functions:
- save_conversation_history(): Saves the conversation history to a file.
- load_conversation_history(): Loads the conversation history from a file.
- get_response(charname, character_description, user_input): Sends a prompt to the Groq API and returns the response.

Usage:
- Import this module to get responses from characters based on user input.
- Use the get_response function to interact with characters in the game.

Example:
from get_response import get_response

response = get_response("Narrator", "You are the narrator...", "Describe the dungeon.")
print(response)
"""

import requests
import json

# Store previous messages for continuity
global conversation_history
conversation_history = []

# Function to save conversation history to a file
def save_conversation_history():
    with open("conversation_history.json", "w") as f:
        json.dump(conversation_history, f)

# Function to load conversation history from a file
def load_conversation_history():
    global conversation_history
    try:
        with open("conversation_history.json", "r") as f:
            conversation_history = json.load(f)
    except FileNotFoundError:
        conversation_history = []  # If no file exists, start with an empty history

# Initialize conversation history by loading from file
load_conversation_history()

def get_response(charname, character_description, user_input):
    global conversation_history  # Declare conversation_history as global

    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer 'You're gonna have to get your own'"  # Replace with your actual API key
    }

    # If the user types '-C', clear the conversation history
    if user_input.strip() == "-C":
        conversation_history.clear()
        save_conversation_history()  # Save the cleared history to the file
        return "Context cleared. Start a new conversation."

    # Add system message for character description
    conversation_history.append({"role": "system", "content": character_description})
    
    # Append user input to the conversation history
    conversation_history.append({"role": "user", "content": user_input})
    
    # Send the entire conversation history in the request
    data = {
        "model": "llama3-70b-8192",
        "messages": conversation_history
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        response_json = response.json()
        message_content = response_json.get("choices", [])[0].get("message", {}).get("content", "Go away!")
        
        # Append assistant's reply to the conversation history
        conversation_history.append({"role": "assistant", "content": message_content})

        # Clear the system message after every request
        conversation_history[:] = [msg for msg in conversation_history if msg['role'] != 'system']

        # Save the updated conversation history to the file
        save_conversation_history()

        return f"{charname}: {message_content}" 
    else:
        return f"Error: {response.status_code}", response.text
