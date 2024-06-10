from langchain_community.chat_models import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
import streamlit as st

# Local Llama2 
llm = ChatOllama(
    base_url="http://ollama:11434",
    model="llama3",
    keep_alive=-1, # keep the model loaded indefinitely
    temperature=0,
    max_new_tokens=512)

st.title("Chatbot com Llama3")

entrada = st.text_area("Qual a sua dúvida????")


prompt = ChatPromptTemplate.from_template("Escreva, em português e com sarcasmo sobre: {topic}")

# using LangChain Expressive Language chain syntax
chain = prompt | llm | StrOutputParser()

if st.button("Enviar"):
    if entrada:
        with st.spinner("Pensando....."):
            st.write_stream(chain.stream({"topic": entrada}))
                
    
