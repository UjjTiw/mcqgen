import os
import re
import json
import PyPDF2
import pandas as pd
import traceback
from dotenv import load_dotenv
from src.mcqgen.logger import logging
from src.mcqgen.utils import read_file, get_table_data, preprocess

from langchain.llms import HuggingFaceHub
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain
from huggingface_hub import login

# Load environment variables
load_dotenv()

# Get Hugging Face API key
key = os.getenv("HUGGING_FACE_KEY")
if not key:
    raise ValueError("HUGGING_FACE_KEY environment variable is not set")

# Log in to Hugging Face Hub
login(token=key)
os.environ['HUGGINGFACEHUB_API_TOKEN'] = key

# Initialize Hugging Face Hub LLM
llm = HuggingFaceHub(
    repo_id='mistralai/Mixtral-8x7B-Instruct-v0.1',
    model_kwargs={"temperature": 0.5, "max_length": 64, "max_new_tokens": 512}
)

# Define the quiz generation prompt template
TEMPLATE = """
Text:{text}
You are an expert MCQ maker. Given the above text, it is your job to \
create a quiz of {number} multiple choice questions for {subject} students in {tone} tone.
Make sure the questions are not repeated and check all the questions to be conforming the text as well.
Make sure to format your response like RESPONSE_JSON below and use it as a guide. \
Ensure to make {number} MCQs
### RESPONSE_JSON
{response_json}
###Identifier
"""

quiz_generation_prompt = PromptTemplate(
    input_variables=['text', 'number', 'subject', 'tone', 'response_json'],
    template=TEMPLATE
)

# Define the quiz evaluation prompt template
TEMPLATE2 = """
You are an expert english grammarian and writer. Given a Multiple Choice Quiz for {subject} students.\
You need to evaluate the complexity of the question and give a complete analysis of the quiz. Only use at max 50 words for complexity analysis. 
if the quiz is not at par with the cognitive and analytical abilities of the students,\
update the quiz questions which need to be changed and change the tone such that it perfectly fits the student abilities.
Quiz_MCQs:
{quiz}

Check from an expert English Writer of the above quiz:
###Identifier
"""

quiz_evaluation_prompt = PromptTemplate(
    input_variables=["subject", "quiz"],
    template=TEMPLATE2
)

# Create the LLM chains
quiz_chain = LLMChain(
    llm=llm,
    prompt=quiz_generation_prompt,
    output_key='quiz',
    verbose=True
)

review_chain = LLMChain(
    llm=llm,
    prompt=quiz_evaluation_prompt,
    output_key="review",
    verbose=True
)

# Create the sequential chain
generate_evaluate_chain = SequentialChain(
    chains=[quiz_chain, review_chain],
    input_variables=['text', 'number', 'subject', 'tone', 'response_json'],
    output_variables=['quiz', 'review'],
    verbose=True
)

# Add appropriate error handling and logging as needed
try:
    # Your code to use the chains
    # Example:
    # response = generate_evaluate_chain({...})
    pass

except Exception as e:
    logging.error(f"An error occurred: {e}")
    traceback.print_exception(type(e), e, e.__traceback__)
