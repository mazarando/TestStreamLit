import streamlit as st
import time

def main():
    st.title("Olá, eu sou a Millenna!")
    st.write("Sou estudante de Análise e Desenvolvimento de Sistemas e, como uma apaixonada por tecnologia, estou sempre em busca de aprender e crescer na área de programação. Minha linguagem de programação favorita é Python. Estou explorando o Streamlit, uma ferramenta incrível para criar aplicações web interativas de maneira rápida e simples usando Python. O que me atraiu no Streamlit é a sua capacidade de transformar códigos Python em aplicações funcionais e atraentes com facilidade. É uma ferramenta ideal para quem, como eu, está iniciando no desenvolvimento de aplicações e busca uma forma prática de compartilhar e visualizar dados.")

    st.header("Input de texto")
    input_text = st.text_input("Comente aqui")
    if input_text:
        st.write("Você digitou: ", input_text)

    st.header("Seleção")
    selected_option = st.selectbox("Selecione uma opção", ['Contratada', 'Sou criativa','Aprendo rápido'])

    if selected_option:
        st.write("Opção selecionada: ", selected_option)

    st.header("Slider")
    slider_value = st.slider("Escolha um valor", 0, 100, 50)
    st.write("Valor escolhido: ", slider_value)

    st.header("Checkbox")
    checkbox_state = st.checkbox("Marque para ativar")
    st.write("Checkbox ativado: ", checkbox_state)

    st.header("Botão")
    if st.button("Clique aqui"):
        st.write("Você clicou no botão!")

    st.header("Loading...")
    with st.spinner("Aguarde..."):
        time.sleep(3)
    st.success("Carregado com sucesso!")
main()