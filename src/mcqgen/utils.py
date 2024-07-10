import os
import PyPDF2
import json
import traceback
import pandas as pd
import re

def read_file(file):
    if file is None or file.size == 0:
        raise Exception("File is empty or not uploaded")
    
    if file.name.endswith(".pdf"):
        try:
            pdf_reader = PyPDF2.PdfReader(file)
            text = ""
            for page in pdf_reader.pages:
                text += page.extract_text()
            return text
            
        except Exception as e:
            raise Exception("Error reading the PDF file: " + str(e))
        
    elif file.name.endswith(".txt"):
        try:
            return file.read().decode("utf-8")
        except Exception as e:
            raise Exception("Error reading the text file: " + str(e))
    
    else:
        raise Exception("Unsupported file format. Only PDF and text files are supported.")

def get_table_data(text):
    try:
        # convert the quiz from a str to dict
        pattern = r"(?<=###Identifier).*"
        match = re.search(pattern, text, re.DOTALL)
        if not match:
            raise Exception("Pattern not found in the text")
        
        result = match.group(0).strip()  # Remove leading and trailing whitespace
        json_data = json.loads(result)
        quiz_table_data = []
        
        # iterate over the quiz dictionary and extract the required information
        for key, value in json_data.items():
            mcq = value["mcq"]
            options = " || ".join([f"{option} -> {option_value}" for option, option_value in value["options"].items()])
            correct = value["correct"]
            quiz_table_data.append({"MCQ": mcq, "Choices": options, "Correct": correct})
        
        return quiz_table_data
        
    except Exception as e:
        traceback.print_exception(type(e), e, e.__traceback__)
        return False

def preprocess(text):
    try:
        pattern = r"(?<=###Identifier).*"
        match = re.search(pattern, text, re.DOTALL)
        if not match:
            raise Exception("Pattern not found in the text")
        
        result = match.group(0).strip()  # Remove leading and trailing whitespace
        json_data = json.loads(result)
        rows = []
        for key, value in json_data.items():
            mcq = value.get('mcq', '')
            options = value.get('options', {})
            correct = value.get('correct', '')
            row = {
                'Question ID': key,
                'Question': mcq,
                'Option A': options.get('a', ''),
                'Option B': options.get('b', ''),
                'Option C': options.get('c', ''),
                'Option D': options.get('d', ''),
                'Correct Answer': correct
            }
            rows.append(row)
                
        # Convert to DataFrame
        df = pd.DataFrame(rows)
        return df
    
    except Exception as e:
        traceback.print_exception(type(e), e, e.__traceback__)
        return False
