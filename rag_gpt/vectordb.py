from langchain_community.document_loaders import WebBaseLoader
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_text_splitters import RecursiveCharacterTextSplitter


def urt_to_vector(url):
    loader = WebBaseLoader(url)
    docs = loader.load()

    embeddings = OpenAIEmbeddings()

    text_splitter = RecursiveCharacterTextSplitter()

    documents = text_splitter.split_documents(docs)

    vector = FAISS.from_documents(documents, embeddings)
    retriver = vector.as_retriever()

    return retriver
