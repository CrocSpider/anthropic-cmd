from dotenv import load_dotenv
import anthropic
import os

# Load environment variables from the .env file
load_dotenv()

# Load your API key from an environment variable
API_KEY = os.getenv("ANTHROPIC_API_KEY")

# Initialize the Anthropic client
client = anthropic.Anthropic(api_key=API_KEY)

def chat_with_anthropic(messages):
    # Create a chat message with streaming enabled
    stream = client.messages.create(
        model="claude-3-5-sonnet-20240620",
        max_tokens=100,
        messages=messages,
        stream=True
    )
    
    # Initialize variables to hold the final message and token count
    full_message = ""
    total_input_tokens = 0
    total_output_tokens = 0

    # Iterate over the streamed response
    for event in stream:
        #print("Received event:", event)  # Debug: Print the entire event
        
        if hasattr(event, 'delta') and hasattr(event.delta, 'text'):
            # Extract and accumulate the text
            text = event.delta.text
            full_message += text
            print(text, end='', flush=True)  # Print the text continuously
        
        if hasattr(event, 'usage'):
            # Access input_tokens and output_tokens directly
            print("Usage details:", dir(event.usage))
            usage = event.usage
            total_input_tokens += getattr(usage, 'input_tokens', 0)
            total_output_tokens += getattr(usage, 'output_tokens', 0)
        
        if hasattr(event, 'type') and event.type == 'content_block_stop':
            print("\nContent block stopped.")
        
        if hasattr(event, 'type') and event.type == 'message_stop':
            print("\nMessage stream stopped.")
            break

    print()  # For a new line after streaming is complete
    return full_message, total_input_tokens, total_output_tokens

def main():
    print("Welcome to the Anthropic Assistant!")
    messages = []
    total_input_tokens = 0
    total_output_tokens = 0

    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit']:
            break

        # Append the user's message to the messages list
        messages.append({"role": "user", "content": user_input})

        # Get the response and token counts
        response, input_tokens, output_tokens = chat_with_anthropic(messages)

        # Append the assistant's response to the messages list
        messages.append({"role": "assistant", "content": response})

        # Update total tokens
        total_input_tokens += input_tokens
        total_output_tokens += output_tokens

        print(f"\nTotal Input Tokens: {total_input_tokens}, Total Output Tokens: {total_output_tokens}")

if __name__ == "__main__":
    main()
