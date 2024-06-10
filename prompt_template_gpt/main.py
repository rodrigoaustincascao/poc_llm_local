from langchain_openai import OpenAI
from langchain_core.prompts import PromptTemplate
from langchain.chains.llm import LLMChain
from dotenv import load_dotenv

load_dotenv()

def generate_cat_name(animal_type):
    llm = OpenAI(temperature=0.6)

    template= """Você tem um {animal_type} filhote novo e gostaria de dar um nome para ele. 
        Ajude-me com uma lista de 5 possíveis nomes."""
    prompt = PromptTemplate.from_template(template)

    llm_chain = LLMChain(prompt=prompt, llm=llm, )
    response = llm_chain.invoke(animal_type)
    return response

if __name__ == "__main__":
    print(generate_cat_name("Arara"))
