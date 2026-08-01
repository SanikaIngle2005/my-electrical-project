from langchain_community.llms import Ollma
import streamlit as st
from langchain_core.promts import ChatpromptTemplate
from langchain_core.output_parsers import Stroutputparser

#creating my prompts
prompt =ChatpromptTemplate.from_messages(

    ("system",'You are helpful assistant.please respond to the que')
    ("user ","Question:{question}")

    #streamlit framework
    st.title('MY GPT')
    input_text = st.text_input('what question do you have in mind')
)
     #Let's create LLM chain systems
     # ollama LAAMA2 model
llm = Ollama(model ="gemma2:2b")
output_parsers = Stroutputparser()
chain = prompt | llm | output_parser

if input_text:
    st.write(chain.invoke())






