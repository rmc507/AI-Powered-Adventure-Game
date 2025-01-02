import json
import requests
import subprocess
# Function to load the conversation history (JSON file)
def load_conversation_history():
    try:
        with open("conversation_history.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []  # Return an empty list if the file doesn't exist

# Function to load the content of the patterns.txt file
def load_patterns_file():
    try:
        with open("pattern.txt", "r") as f:
            return f.read()
    except FileNotFoundError:
        print("Text file 'pattern.txt' not found.")
        return None

# Function to save the updated conversation history back to the JSON file
def save_conversation_history(conversation_history):
    with open("conversation_history.json", "w") as f:
        json.dump(conversation_history, f, indent=4)

# Function to send the conversation history, text file content, and user input to Grok API
def send_to_grok(conversation_history, text_content):
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer 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"  # Replace with your actual API key
    }

    # Combine conversation history with the new text content
    data = {
        "model": "llama-3.3-70b-versatile",  # Make sure to choose the correct model for your use case
        "messages": conversation_history + [{"role": "user", "content": text_content}]
    }

    response = requests.post(url, headers=headers, json=data)
    
    if response.status_code == 200:
        response_json = response.json()
        message_content = response_json.get("choices", [])[0].get("message", {}).get("content", "No response.")
        return message_content
    else:
        return f"Error: {response.status_code}", response.text

# Main function to read the files, send to Grok, and update the conversation history
def main():
    # Load the current conversation history (empty if file doesn't exist)
    conversation_history = load_conversation_history()

    # Load the content from the patterns.txt file
    text_content = load_patterns_file()

    if text_content is not None:
        # Send the current conversation history and the patterns.txt content to Grok
        summary = send_to_grok(conversation_history, text_content)

        # Prepend a note to the summary indicating it is a summary of past events
        summary_with_note = f"This is a summary of what has already happened:\n{summary}"

        # Create a new conversation history with the Grok summary as user input
        conversation_history = [{"role": "user", "content": summary_with_note}]

        # Print the final summary response from Grok
        print("Grok Response (Summary):", summary_with_note)

        # Save the updated conversation history (which now only contains the summary) to the JSON file
        save_conversation_history(conversation_history)

if __name__ == "__main__":
    main()
