import streamlit as st
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

st.set_page_config(page_title="Consultas Modelo deepseek")

st.title("Consultas a Modelo deepseek")

# Modelo Ollama local
model = OllamaLLM(model="deepseek-r1:7b")

# Prompt para consultas sencillas
prompt_template = """
Eres un asistente en español. Responde de forma clara y concisa.

Pregunta: {question}
Respuesta:
"""

prompt = ChatPromptTemplate.from_template(prompt_template)

# Interfaz
question = st.text_input("Escribe aquí tu pregunta:")

if st.button("Obtener respuesta") and question:
    with st.spinner('Consultando al modelo...'):
        chain = prompt | model
        response = chain.invoke({"question": question})

        respuesta_final = response.strip().split("<|im_end|>")[0].split("<|im_end|>")[0].split("<|assistant|>")[-1].strip()
        
        st.success("Respuesta del modelo:")
        st.write(response)