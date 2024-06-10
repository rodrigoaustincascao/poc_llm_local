from langchain_core.prompts import ChatPromptTemplate
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains.retrieval import create_retrieval_chain
from vectordb import urt_to_vector
from chatgpt import llm

prompt = ChatPromptTemplate.from_template(""" Responda a pergunta com base apenas no contexto:
{context}
Pergunta: {input}
""")

document_chain = create_stuff_documents_chain(llm, prompt)
retriver = urt_to_vector('https://pt.wikipedia.org/wiki/Oppenheimer_(filme)')
retriver_chain = create_retrieval_chain(retriver, document_chain)

response = retriver_chain.invoke({"input": "Quantos oscar o filme Oppenheimer ganhou em 2024"})

print(response['answer'])

