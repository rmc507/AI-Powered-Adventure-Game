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

    # Ollama API endpoint
    url = "http://localhost:11434/api/generate"
    headers = {
        "Content-Type": "application/json"
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
    
    # Prepare the data for Ollama - here we'll send the entire conversation history
    data = {
        "model": "llama3.1:latest",  
        "prompt": "\n".join([f"{msg['role']}: {msg['content']}" for msg in conversation_history]) + "\nassistant:",
        "stream": False  # For simplicity, we'll use non-streaming mode
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        response_json = response.json()
        message_content = response_json.get("response", "Go away!")
        
        # Append assistant's reply to the conversation history
        conversation_history.append({"role": "assistant", "content": message_content})

        # Clear the system message after every request
        conversation_history[:] = [msg for msg in conversation_history if msg['role'] != 'system']

        # Save the updated conversation history to the file
        save_conversation_history()

        return f"{charname}: {message_content}" 
    else:
        return f"Error: {response.status_code}", response.text