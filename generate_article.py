from openai import OpenAI
import os
import requests
import uuid
import json
from pathlib import Path
import streamlit as st
from dotenv import load_dotenv, dotenv_values

load_dotenv()
client = OpenAI(api_key=dotenv_values(".env")["OPENAI_API_KEY"])


def format_translated_article(translated_article):
    translated_article = translated_article.replace('\\n', '\n')
    paragraphs = translated_article.split('\n\n')

    formatted_article = ""
    for paragraph in paragraphs:
        if paragraph.startswith('**'):
            formatted_article += f"\n• {paragraph.replace('**', '')}\n"
        else:
            formatted_article += f"\n{paragraph}\n"

    return formatted_article


def article_generator(user_input, language):
    # Define an initial message from the user
    messages = [
        {
            "role": "user",
            "content": "Say this is a test",
        }
    ]  # Define messages as a list with a single initial message dictionary

    # Receive input from the user
    message = user_input
    language = language.lower()
    languages = []
    if language == 'english':
        languages = ['en']
    elif language == 'yoruba':
        languages.append('yo')
    elif language == 'igbo':
        languages.append('ig')
    elif language == 'hausa':
        languages.append('ha')
    else:
        languages.append('en')
    print(languages)

    # If user input exists
    if message:
        # Append the user's new message to the messages list
        messages.append({'role': 'user', 'content': message})

        # Create a chat completion using the AI model (assuming 'client' is initialized elsewhere)
        chat_completion = client.chat.completions.create(
            messages=messages,  # Pass the list of messages
            model="gpt-4"  # Use the GPT-4 model for generating a response
        )

        # Retrieve the response content from the chat completion
        # Note: Make sure 'chat_completion' contains the response object with 'choices' available
        reply = chat_completion.choices[0].message.content
        # Add your key and endpoint
        key = dotenv_values('.env')['AZURE_KEY']

        endpoint = dotenv_values('.env')['AZURE_ENDPOINT']

        # location, also known as region.
        # required if you're using a multi-service or regional (not global) resource. It can be found in the Azure portal on the Keys and Endpoint page.
        location = dotenv_values('.env')['AZURE_REGION']
        path = '/translate'
        constructed_url = endpoint + path

        params = {
            'api-version': '3.0',
            'from': 'en',
            'to': languages
        }

        headers = {
            'Ocp-Apim-Subscription-Key': key,
            # location required if you're using a multi-service or regional (not global) resource.
            'Ocp-Apim-Subscription-Region': location,
            'Content-type': 'application/json',
            'X-ClientTraceId': str(uuid.uuid4())
        }

        # You can pass more than one object in body.
        body = [{
            'text': reply
        }]

        request = requests.post(
            constructed_url, params=params, headers=headers, json=body)
        response = request.json()
        final_reply = format_translated_article(json.dumps(
            response[0]['translations'][0]['text'], sort_keys=True, ensure_ascii=False, indent=4, separators=(',', ': ')))
        # Print the response from the AI model
        # print(f"ChatGPT: {final_reply}")

        # Add the assistant's response to the messages list
        messages.append({"role": "assistant", "content": final_reply})
    return final_reply


def speech_synthesis_to_audio_stream(article):
    """performs speech synthesis and returns the audio stream"""

    speech_file_path = Path('ttr').parent / "speech.mp3"
    response = client.audio.speech.create(
        model="tts-1",
        voice="alloy",
        input=article
    )
    response.stream_to_file(speech_file_path)

    # Read the contents of the audio file
    audio_data = speech_file_path.read_bytes()

    # Display the audio file in Streamlit
    st.audio(audio_data, format='audio/mp3')
