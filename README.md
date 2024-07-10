# MCQ Generator

## Overview

MCQ Generator is a Python application that utilizes the Hugging Face API and the Mixtral model to generate multiple-choice questions (MCQs) based on text input. The application is designed to simplify the process of creating quizzes or assessments by automatically generating questions of varying difficulty levels.

## Features

- Generates MCQs based on text input (TXT or PDF files)
- Allows selection of question difficulty levels: Simple, Medium, or Tough
- Utilizes the Hugging Face API for natural language processing
- Powered by the Mixtral model for advanced language understanding and generation

## About Mixtral

Mixtral is a state-of-the-art language model developed by Mistral AI. It's known for its:

- High performance across a wide range of tasks
- Efficient processing of long contexts
- Ability to generate coherent and contextually relevant content

By leveraging Mixtral, our MCQ Generator can create high-quality, diverse, and contextually accurate questions.

## Setup Instructions

### Prerequisites

- Python 3.6+
- pip (Python package installer)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/mcq-generator.git
   cd mcq-generator
   ```

2. Set up a virtual environment (optional but recommended):
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run setup:
   ```bash
   python setup.py install
   ```

### Running the Application

1. Start the Streamlit application:
   ```bash
   streamlit run streamlitapp.py
   ```

2. Open your web browser and go to the provided local host URL.

### Usage

1. Upload a text file (TXT) or a PDF document containing the content for which MCQs need to be generated.
2. Select the desired number of questions and their difficulty level (Simple, Medium, or Tough).
3. Click on the "Generate Questions" button to 

https://github.com/UjjTiw/mcqgen/assets/99402799/0e246e57-78f3-4edc-b0db-9de3a19bff90

obtain the generated MCQs.


## Contributing

Contributions are welcome! Please fork the repository and submit pull requests.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
