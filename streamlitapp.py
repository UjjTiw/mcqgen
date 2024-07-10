import os
import re
import json
import traceback
import pandas as pd
from dotenv import load_dotenv
import streamlit as st
from src.mcqgen.utils import read_file, get_table_data, preprocess
from src.mcqgen.mcqgen import generate_evaluate_chain
from src.mcqgen.logger import logging

# Load environment variables
load_dotenv()

# Load the response.json file
with open('response.json', 'r') as file:
    RESPONSE_JSON = json.load(file)

# Creating a title for the app
st.title("MCQs Creator Application with LangChain 🦜⛓️")

# Create a form using st.form
with st.form("user_inputs"):
    # File Upload
    uploaded_file = st.file_uploader("Upload a PDF or txt file")

    # Input Fields
    mcq_count = st.number_input("No. of MCQs", min_value=3, max_value=50)

    # Subject
    subject = st.text_input("Insert Subject", max_chars=20)

    # Quiz Tone
    tone = st.text_input("Complexity Level Of Questions", max_chars=20, placeholder="Simple")

    # Add Button
    button = st.form_submit_button("Create MCQs")

    # Check if the button is clicked and all fields have input
    if button and uploaded_file is not None and mcq_count and subject and tone:
        with st.spinner("Loading..."):
            try:
                text = read_file(uploaded_file)
                # Count tokens and the cost of API call
                response = generate_evaluate_chain(
                    {
                        "text": text,
                        "number": mcq_count,
                        "subject": subject,
                        "tone": tone,
                        "response_json": json.dumps(RESPONSE_JSON)
                    }
                )

            except Exception as e:
                logging.error("Error occurred", exc_info=True)
                st.error(f"Error: {str(e)}")
            
            else:
                if isinstance(response, dict):
                    # Extract the quiz data from the response
                    quiz = response.get("quiz", None)
                    if quiz is not None:
                        table_data = get_table_data(quiz)
                        if table_data is not None:
                            df = pd.DataFrame(table_data)
                            df.index = df.index + 1
                            st.table(df)
                            # Display the review in a text box as well
                            st.text_area(label="Review", value=response.get("review", ""))
                        else:
                            st.error("Error in the table data")
                    else:
                        st.error("Quiz data not found in the response")
                else:
                    st.write(response)
