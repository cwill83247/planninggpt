from llama_index import SimpleDirectoryReader, GPTListIndex, readers, GPTSimpleVectorIndex, LLMPredictor, PromptHelper, ServiceContext
from langchain import OpenAI
import sys
import os
from IPython.display import Markdown, display

# html related imports
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def search_form():
  return render_template('search_form.html')

@app.route('/search')
def search():
    # Get the search query from the URL query string
    query = request.args.get('query')  

#def ask_ai():
    index = GPTSimpleVectorIndex.load_from_disk('index.json')   ## reads in the index.json 
    while True: 
        #query = input("What do you want to ask? ")
        query = query
        response = index.query(query)
        print(response)
        #display(Markdown(f"Response: <b>{response.response}</b>"))

#ask_ai()        
        return render_template('search_results.html', query=query, results=response)

if __name__ == '__main__':
  app.run()