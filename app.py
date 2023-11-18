# app.py
import streamlit as st
from assistant import run_openai_assistant
from generate_article import article_generator, format_translated_article, speech_synthesis_to_audio_stream
from generate_code_documentation import generate_code_documentation
from detect_and_fix_bugs import detect_and_fix_bugs


def article():
    st.title("Article Generation and Speech Synthesis")

    # User input for article generation
    user_input = st.text_input(
        "Enter text for article generation:", "Write an article about ")

    # Language selection for translation
    language = st.selectbox("Select translation language:", [
                            "English", "Yoruba", "Igbo", "Hausa"])
    Generate = st.button("Generate and Translate")
    if 'generate_state' not in st.session_state:
        st.session_state.generate_state = False

    if Generate or st.session_state.generate_state:
        st.session_state.generate_state = True
        # Generate and translate the article
        generated_article = article_generator(user_input, language)
        translated_article = format_translated_article(generated_article)

        # Display the translated article
        st.subheader("Translated Article:")
        st.code(translated_article, 'markdown')
        if language.lower() == 'english':
            # Synthesize the translated article
            synthesize = st.button("Synthesize Speech")
            if 'synthesize_state' not in st.session_state:
                st.session_state.synthesize_state = False
            if synthesize or st.session_state.synthesize_state:
                st.session_state.synthesize_state = True
                if translated_article:
                    speech_synthesis_to_audio_stream(translated_article)
                else:
                    st.warning(
                        "Please enter some text before synthesizing speech.")


def documentation():
    st.title("Code Documentation Generation")

    # Get user input for code base and language
    code_base = st.text_area("Enter your code:", "")
    language_options = ["Python", "Java", "C++",
                        "JavaScript", "TypeScript", "PHP", "C#", "Bash"]
    language = st.selectbox(
        "Select the programming language:", language_options)
    # Check if the user has provided code and language
    if st.button("Generate Documentation"):
        if code_base and language:
            # Generate documentation using the provided function
            documentation = generate_code_documentation(code_base, language)
            st.code(documentation, language)
        else:
            st.warning("Please enter both code and language.")


def bugs():
    st.title("Bug Detection and Fixing")

    # Get user input for code base and language
    code_base = st.text_area("Enter your code:", "")
    language_options = ["Python", "Java", "C++",
                        "JavaScript", "TypeScript", "PHP", "C#", "Bash"]
    language = st.selectbox(
        "Select the programming language:", language_options)
    # Check if the user has provided code and language
    if st.button("Detect and Fix Bugs"):
        if code_base and language:
            # Detect and fix bugs using the provided function
            bug_detection_result = detect_and_fix_bugs(code_base, language)
            st.code(bug_detection_result, language)
        else:
            st.warning("Please enter both code and language.")


def darth():
    st.title("D.A.R.T.H Assistant")

    # File upload
    uploaded_file = st.file_uploader("Upload a file", type=["pdf"])

    if uploaded_file is not None:
        st.success("File uploaded successfully!")

        # Get user prompt
        prompt_text = st.text_area("Enter your prompt:", "")

        if st.button("Run Assistant"):
            st.info("Running OpenAI Assistant... Please wait.")

            # Run the OpenAI Assistant
            user_msgs, assistant_msgs = run_openai_assistant(
                uploaded_file, prompt_text)

            # Display user messages
            st.subheader("User Messages:")
            for msg in user_msgs:
                st.text(f"User: {msg}")

            # Display assistant messages
            st.subheader("Assistant Messages:")
            for msg in assistant_msgs:
                st.text(f"Assistant: {msg}")
                speech_synthesis_to_audio_stream(msg)


# Define the main navigation sidebar
st.sidebar.title("D.A.R.T.H")
page_names_to_funcs = {
    "Generate article": article,
    "Generate code documentation": documentation,
    "Detect and fix bugs": bugs,
    "D.A.R.T.H Assistant": darth
}
demo_name = st.sidebar.selectbox(
    "What would you like to do?", list(page_names_to_funcs.keys()))
page_names_to_funcs[demo_name]()
