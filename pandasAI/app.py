from pandasai.llm.local_llm import LocalLLM
import streamlit as st 
import pandas as pd 
from pandasai import SmartDataframe

model = LocalLLM(
    api_base="http://ollama:11434/v1",
    model="llama3"
)

st.title("Conversando com os dados!")

uploaded_file = st.file_uploader("Upload do CSV", type=['csv'])

if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    st.write(data.head(3))

    df = SmartDataframe(data, config={"llm": model})
    prompt = st.text_area("Pergunte para os Dados:")

    if st.button("Perguntar"):
        if prompt:
            with st.spinner("Pensando..."):
                st.write(df.chat(prompt))