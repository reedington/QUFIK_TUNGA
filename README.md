# D.A.R.T.H - Digital Assistant for Resourceful Technical Help

D.A.R.T.H is a powerful streamlit application designed to assist developers in enhancing their coding experience. With a focus on providing valuable resources and aiding in various aspects of coding, D.A.R.T.H offers four key functions to make developers' lives easier.

## Features

1. **Article Generation:**
   - D.A.R.T.H can generate articles in English, Yoruba, Igbo, and Hausa. The English version is also synthesized into speech, providing an accessible way to consume information.

2. **Code Documentation Generator:**
   - Simplify the process of creating code documentation. Insert your code, and D.A.R.T.H will generate comprehensive documentation for you.

3. **Code Bug Detection and Correction:**
   - Identify and fix bugs in your code effortlessly. By submitting your code to D.A.R.T.H, it analyzes the content, pinpoints errors, and provides automated fixes.

4. **Document Assistant:**
   - Upload a document, and D.A.R.T.H becomes your knowledgeable assistant. Ask questions about the document, and receive detailed answers in English. The responses are also synthesized into speech for a convenient listening experience.

## Getting Started

Follow the instructions below to get started with D.A.R.T.H:

### Prerequisites

- Python installed
- Streamlit library installed (you can install it using `pip install streamlit`)
- Additional prerequisites for specific functions (mention them if any)

### Installation

1. Clone the repository.
2. Navigate to the project directory.
3. Install the required dependencies.

```bash
pip install -r requirements.txt 
```

## D.A.R.T.H Streamlit App

The `app.py` file contains a Streamlit app for interacting with various functions of the D.A.R.T.H system. Here's how you can use the Streamlit app:

### Usage

1. **Generate Article and Synthesize Speech:**
   - Enter text for article generation.
   - Select the translation language (English, Yoruba, Igbo, Hausa).
   - Click "Generate and Translate" to generate and translate the article.
   - Optionally, click "Synthesize Speech" to listen to the synthesized speech.

2. **Generate Code Documentation:**
   - Enter your code in the provided text area.
   - Select the programming language from the dropdown.
   - Click "Generate Documentation" to generate code documentation.

3. **Detect and Fix Bugs:**
   - Enter your code in the provided text area.
   - Select the programming language from the dropdown.
   - Click "Detect and Fix Bugs" to identify and fix bugs in the code.

4. **D.A.R.T.H Assistant:**
   - Upload a PDF file.
   - Enter your prompt text in the text area.
   - Click "Run Assistant" to interact with the OpenAI Assistant.
   - View the user and assistant messages, and optionally listen to the synthesized speech.

### Dependencies

- [`streamlit`](https://streamlit.io/) for creating the interactive web app.
- [`openai`](https://github.com/openai/openai) library for OpenAI interactions.
- [`dotenv`](https://github.com/theskumar/python-dotenv) for managing environment variables.

### How to Run

1. Install the required dependencies using `pip install streamlit openai python-dotenv`.

2. Create a `.env` file with your OpenAI API key.

3. Run the Streamlit app using `streamlit run app.py`.

### Example

Here's an example demonstrating how to use the Streamlit app:

```bash
# Install dependencies
pip install streamlit openai python-dotenv
```

### Create a .env file with your OpenAI API key

### Run the Streamlit app

streamlit run app.py

## Article Generator

The `article_generator` function in D.A.R.T.H allows you to generate articles in various languages using OpenAI's GPT-4 model. Here's a breakdown of how it works:

### Usage

```python
from DARTH import article_generator

# Provide user input and target language
user_input = "Say this is a test"
language = "English"

# Generate the translated article
translated_article = article_generator(user_input, language)
```

# Display the formatted article

print(translated_article)

## Description

1. **User Input:**
   - The function takes a user input message as the starting point for generating an article.

2. **Language Selection:**
   - Specify the target language for the article. Supported languages include English, Yoruba, Igbo, and Hausa.

3. **Translation:**
   - Utilizes OpenAI's GPT-4 model to generate a response in the specified language.

4. **Translation to Speech:**
   - Translates the English version into the chosen language and formats the translated article for readability.

## Dependencies

- [`openai`](https://github.com/openai/openai) library for GPT-4 model interactions.
- [`requests`](https://docs.python-requests.org/en/latest/) library for making HTTP requests.
- [`streamlit`](https://streamlit.io/) for creating the user interface.
- [`dotenv`](https://github.com/theskumar/python-dotenv) for managing environment variables.

## Code Documentation Generator

The `generate_code_documentation` function in D.A.R.T.H simplifies the process of generating documentation and comments for your codebase. Here's how you can use it:

### Usage

```python
from DARTH import generate_code_documentation
```

# Provide your code and specify the language

code_base = """

### Your code goes here

"""
language = "python"

## Generate code documentation

documentation = generate_code_documentation(code_base, language)

# Display the generated documentation

print(documentation)

### Description

1. **Code Input:**
   - Provide your codebase or function for which you want to generate documentation.

2. **Language Specification:**
   - Specify the programming language of your code (e.g., Python, JavaScript).

3. **Documentation Generation:**
   - The function uses OpenAI's GPT-4 model to generate comprehensive documentation and comments for the provided code.

### Dependencies

- [`openai`](https://github.com/openai/openai) library for GPT-4 model interactions.
- [`dotenv`](https://github.com/theskumar/python-dotenv) for managing environment variables.

## Code Bug Detection and Fixer

The `detect_and_fix_bugs` function in D.A.R.T.H simplifies the process of identifying and fixing bugs or potential issues in your codebase. Here's how you can use it:

### Usage

```python
from DARTH import detect_and_fix_bugs
```

# Provide your code and specify the language

code_base = """

# Your code goes here

"""
language = "python"

# Detect and fix bugs

bug_detection_result = detect_and_fix_bugs(code_base, language)

# Display the bug detection result

print(bug_detection_result)

### Description

1. **Code Input:**
   - Provide your codebase or function for which you want to detect and fix bugs.

2. **Language Specification:**
   - Specify the programming language of your code (e.g., Python, JavaScript).

3. **Bug Detection and Fixing:**
   - The function uses OpenAI's GPT-4 model to analyze the provided code, identify bugs or potential issues, and suggest fixes or improvements.

### Dependencies

- [`openai`](https://github.com/openai/openai) library for GPT-4 model interactions.
- [`dotenv`](https://github.com/theskumar/python-dotenv) for managing environment variables.

## OpenAI Assistant

The `run_openai_assistant` function in D.A.R.T.H allows you to interact with an OpenAI assistant using a file and prompt text. Here's how you can use it:

### Usage

```python
from DARTH import run_openai_assistant
```

## Provide the file and prompt text

uploaded_file = open("path/to/your/file.txt", "rb")
prompt_text = "Ask a question or provide instructions."

### Run the OpenAI assistant

user_messages, assistant_messages = run_openai_assistant(uploaded_file, prompt_text)

### Display the conversation messages

print("User Messages:", user_messages)
print("Assistant Messages:", assistant_messages)

### Description

1. **File Upload:**
   - The function uploads a file to OpenAI, which will be used during the interaction with the OpenAI assistant.

2. **Assistant Initialization:**
   - An OpenAI assistant is created with specific instructions, tools, and a model (gpt-4-1106-preview).

3. **Conversation Initiation:**
   - A conversation thread is established, and an initial message is sent to the assistant with the provided prompt text.

4. **Assistant Execution:**
   - The assistant is run within the context of the conversation thread, and the function periodically checks for completion.

5. **Message Retrieval:**
   - Once the assistant completes the run, the function retrieves and organizes the user and assistant messages from the conversation.

### Dependencies

- [`openai`](https://github.com/openai/openai) library for OpenAI interactions.
- [`dotenv`](https://github.com/theskumar/python-dotenv) for managing environment variables.

## DeepSeeker: An Open-Source Model

### Summary

DeepSeeker is an open-source model implemented in the *** notebook. However, the initial implementation demonstrated a sluggish performance. To overcome this limitation, we incorporated OpenAI GPT-4 into the system, enhancing the model's speed and responsiveness.

### OpenAI GPT-4 Integration

To address the speed constraints, we seamlessly integrated OpenAI GPT-4 into DeepSeeker. This not only accelerates the model's processing but also leverages the advanced capabilities of GPT-4, providing improved efficiency and more accurate outcomes.

### Functions in the Notebook

While the functions in the notebook are not directly connected to the D.A.R.T.H app, they play a crucial role in specific tasks. Operating through user input, these functions enable dynamic interaction with the model. Users can input queries or data, triggering the model's processes and obtaining valuable insights and outputs.
