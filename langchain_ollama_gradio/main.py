from langchain_community.chat_models import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
import gradio as gr

def chat(message, history):
    # Local Llama3
    llm = ChatOllama(
        base_url="http://ollama:11434",
        model="llama3",
        keep_alive=-1, # mantém o modelo carregado indefinidamente
        temperature=0,
        max_new_tokens=512)


    prompt = ChatPromptTemplate.from_template("Escreva em português, com sarcasmo sobre: {topic}")

    
    chain = prompt | llm | StrOutputParser()
    response = ""
    for chunk in chain.stream({"topic": message}):
        response += chunk
        yield response

iface = gr.ChatInterface(chat, 
                         title="Chatbox com Llama3", 
                         submit_btn="Enviar",
                         retry_btn="Repetir",
                         undo_btn="Desfazer",
                         clear_btn="Limpar",
                         autofocus=True).queue().launch()
