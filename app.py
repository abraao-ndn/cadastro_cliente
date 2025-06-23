import streamlit as st

st.title("Cadastro de clientes")

nome = st.text_input("Digite o nome do cliente")
endereco = st.text_input("Digite o endereço")
dt_nascimento = st.date_input("Escolha a data de nascimento")
tipo_cliente = st.selectbox("Tipo de cliente",
                            ["Pessoa física", "Pessoa jurídico"])

cadastrar = st.button("Cadastrar Cliente")

if cadastrar:
    with open("cliente.csv", "a", encoding="utf8") as arquivo:
        arquivo.write(f"{nome},{endereco},{dt_nascimento},{tipo_cliente}\n")
        st.success("Cliente cadastrado com sucesso!")
