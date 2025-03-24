# Importing the necessary modules from the Streamlit and OpenAI packages
import streamlit as st
from openai import OpenAI

# Setting the title of the Streamlit application
st.title('Simple LLM-App 🤖')

# Creating a sidebar input widget for the OpenAI API key, input type is password for security
openai_api_key = st.sidebar.text_input('OpenAI API Key', type='password')

# Defining a function to generate a response using the OpenAI model
def generate_response(input_text):
    # Initializing the OpenAI model with the API key
    client = OpenAI(api_key=openai_api_key)

    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        store=True,
        messages=[
            {"role": "user", "content": input_text}
            ]
        )
    # Displaying the generated response as an informational message in the Streamlit app
    st.info(completion.choices[0].message.content)

# Creating a form in the Streamlit app for user input
with st.form('my_form'):
    # Adding a text area for user input with a default prompt
    text = st.text_area('Enter text:', '')
    # Adding a submit button for the form
    submitted = st.form_submit_button('Submit')
    # Displaying a warning if the entered API key does not start with 'sk-'
    if not openai_api_key.startswith('sk-'):
        st.warning('Please enter your OpenAI API key!', icon='⚠')
    # If the form is submitted and the API key is valid, generate a response
    if submitted and openai_api_key.startswith('sk-'):
        generate_response(text) ####

 