from langchain_openai import OpenAI
from langchain_core.prompts import PromptTemplate
from langchain.chains.llm import LLMChain
from dotenv import load_dotenv


load_dotenv()

def oscar(filme, ano, llm):
    

    template= """Quantos oscar o filme {filme} ganhou em {ano}"""
    prompt = PromptTemplate.from_template(template)

    llm_chain = LLMChain(prompt=prompt, llm=llm )
    response = llm_chain.invoke({'filme':filme, 'ano':ano})
    return response

llm = OpenAI(temperature=0.6, model="gpt-3.5-turbo-instruct")

if __name__ == "__main__":
    response = oscar('Oppenheimer', 2024, llm)
    print(response['text'])
