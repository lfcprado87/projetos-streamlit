import streamlit as st
import pandas as pd
from datetime import date

def gravar_dados(nome, data_nasc, tipo):
    if nome and data_nasc < date.today():
        with open("clientes.csv", "a", encoding ="utf-8") as file:
            file.write(f"{nome},{data_nasc},{tipo}")
        st.session_state["sucesso"] = True 
    else:    
        st.session_state["sucesso"] = False


 

st.set_page_config(page_title="Cadastro de Clientes", 
                   page_icon="📗",)

st.title("Cadastro de Clientes") 
st.divider()

nome = st.text_input("Digite o nome do cliente",
                     key="nome_clente") 
dt_nasc = st.date_input("Data Nascimento", format="DD/MM/YYYY")

tipo = st.selectbox("Tipo de Cliente",
                    options=["Pessoa Física", "Pessoa Jurídica"])

btn_cad = st.button("Cadastrar",
                    on_click=gravar_dados,
                    args=[nome, dt_nasc, tipo])

if btn_cad:
    if st.session_state["sucesso"]:
        st.success("Cliente cadastrado com sucesso!", icon="✅")
    else:
        st.error("Erro no cadastro. Verifique os dados e tente novamente.", icon="❌" )