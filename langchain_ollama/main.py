from langchain_community.chat_models import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

# Local Llama2 
llm = ChatOllama(
    base_url="http://ollama:11434",
    model="llama3",
    keep_alive=-1, # keep the model loaded indefinitely
    temperature=0,
    max_new_tokens=512)

prompt = ChatPromptTemplate.from_template("Escreva, em português, um artigo de 500 palavras sobre {topic} a partir da pespectiva de um {profession}. ")

# using LangChain Expressive Language chain syntax
chain = prompt | llm | StrOutputParser()


for chunk in chain.stream({"topic": "LLMs", "profession": "Desenvolvedor"}):
    print(chunk, end="", flush=True)