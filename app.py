# to run this code command is: streamlit run app.py

import streamlit as st
from pydantic import BaseModel
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure Gemini AI
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
if not GOOGLE_API_KEY:
    st.error("GOOGLE_API_KEY not found in environment variables")
    st.stop()

genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-pro')

# Streamlit app
st.title("AI Python Code Generator by Wrick")

# Create a form for input
with st.form(key='code_generator_form'):
    # Input box for getting the specification
    prompt = st.text_area("Enter your code specification:", height=150)
    
    # Generate button
    generate_button = st.form_submit_button("Generate Code")

if generate_button and prompt:
    try:
        # Show loading spinner while generating
        with st.spinner('Generating code...'):
            # Generate code using Gemini AI
            response = model.generate_content(prompt)
        
        if not response.text:
            st.error("Failed to generate code")
        else:
            # Success message
            st.success("Code generated successfully!")
            
            # Display the generated code in a neat format
            st.code(response.text.strip(), language='python')
            
            # Add a copy button (Streamlit automatically adds this for code blocks)

    except Exception as e:
        st.error(f"Error: {str(e)}")