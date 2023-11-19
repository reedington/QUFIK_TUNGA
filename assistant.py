import openai
import time
from dotenv import load_dotenv, dotenv_values

# Initialize the OpenAI client
load_dotenv()
client = openai.Client(api_key=dotenv_values(".env")["OPENAI_API_KEY"])


def run_openai_assistant(uploaded_file, prompt_text):
    """
    Executes an OpenAI assistant using a given file and prompt text, returning the user and assistant messages.

    Parameters:
    - file_path (str): The path to the file to be uploaded for assistant use.
    - prompt_text (str): The text prompt to initiate the conversation with the assistant.

    Returns:
    - user_messages (list): A list of messages from the user in the conversation.
    - assistant_messages (list): A list of messages from the assistant in the conversation.
    """

    file_path = uploaded_file.read()
    # Upload files to OpenAI
    file = client.files.create(
        file=file_path,
        purpose="assistants"
    )

    # Step 1: Create an Assistant
    assistant = client.beta.assistants.create(
        name='ML & Computer Science Researcher',
        instructions=' You are an Expert in ML & Computer Science Research. Provided easy to understand answers to the most complicated questions in the best way possible',
        tools=[{'type': 'retrieval'}],
        model="gpt-4-1106-preview",
        file_ids=[file.id]
    )

    # Step 2: Create a Thread
    thread = client.beta.threads.create()

    # Step 3: Add a Message to a Thread
    message = client.beta.threads.messages.create(
        thread_id=thread.id,
        role="user",
        content=prompt_text
    )

    # Step 4: Run the Assistant
    run = client.beta.threads.runs.create(
        thread_id=thread.id,
        assistant_id=assistant.id,
        instructions="Please address the user as Jane Doe. The user has a premium account."
    )

    while True:
        # Wait for 5 seconds
        time.sleep(5)

        # Retrieve the run status
        run_status = client.beta.threads.runs.retrieve(
            thread_id=thread.id,
            run_id=run.id
        )

        # If run is completed, get messages
        if run_status.status == 'completed':
            messages = client.beta.threads.messages.list(
                thread_id=thread.id
            )

            # Initialize empty lists for user and assistant messages
            user_messages = []
            assistant_messages = []

            # Loop through messages and append content based on role
            for msg in reversed(messages.data):
                role = msg.role
                content = msg.content[0].text.value

                if role == "user":
                    user_messages.append(content)
                elif role == "assistant":
                    assistant_messages.append(content)

            return user_messages, assistant_messages
