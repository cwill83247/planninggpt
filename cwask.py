from llama_index import SimpleDirectoryReader, GPTListIndex, readers, GPTSimpleVectorIndex, LLMPredictor, PromptHelper, ServiceContext
from langchain import OpenAI
import sys
import os
from IPython.display import Markdown, display


def ask_ai():
    index = GPTSimpleVectorIndex.load_from_disk('index.json')   ## reads in the index.json 
    while True: 
        query = input("What do you want to ask? ")
        response = index.query(query)
        print(response)
        display(Markdown(f"Response: <b>{response.response}</b>"))

ask_ai()        