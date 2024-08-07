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
    response = client.messages.create(
        model="claude-3-5-sonnet-20240620",
        max_tokens=1024,
        messages=messages
    )
    # The response is a Message object, so access the content attribute
    full_message = response.content[0].text.strip()
    usage = response.usage  # Assuming usage is available in the response

    # Extract token counts from usage
    input_tokens = getattr(usage, 'input_tokens', 0)
    output_tokens = getattr(usage, 'output_tokens', 0)
    
    return full_message, input_tokens, output_tokens

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
        
        print(f"Assistant: {response}")
        print(f"\nTotal Input Tokens: {total_input_tokens}, Total Output Tokens: {total_output_tokens}")

if __name__ == "__main__":
    main()