from setuptools import find_packages,setup

setup(
    name='mcqgenrator',
    version='0.0.1',
    author='ujjwal tiwari',
    author_email='ujjwaltiwari2004razor@gmail.com',
    install_requires=["openai","langchain","streamlit","python-dotenv","PyPDF2","transformers","sentence-transformers"],
    packages=find_packages()
)