from openai import OpenAI
from dotenv import load_dotenv, dotenv_values

load_dotenv()
client = OpenAI(api_key=dotenv_values(".env")["OPENAI_API_KEY"])


def generate_code_documentation(code_base, language):
    # Define an initial message from the user
    messages = [
        {
            "role": "user",
            "content": "Say this is a test",
        }
    ]  # Define messages as a list with a single initial message dictionary

    code_base = code_base
    language = language
    # If user input exists

    if code_base:
        # Append the user's new message to the messages list
        messages.append({'role': 'user', 'content': f"Please generate documentation and comments for the following {language.upper()} function/code. The goal is to clarify each line's purpose and functionality for future developers working on this codebase: {code_base}"})

        # Create a chat completion using the AI model (assuming 'client' is initialized elsewhere)
        chat_completion = client.chat.completions.create(
            messages=messages,  # Pass the list of messages
            model="gpt-4"  # Use the GPT-4 model for generating a response
        )

        # Retrieve the response content from the chat completion
        # Note: Make sure 'chat_completion' contains the response object with 'choices' available
        reply = chat_completion.choices[0].message.content

        # Print the response from the AI model
        # Add the assistant's response to the messages list
        messages.append({"role": "assistant", "content": reply})
    return reply
