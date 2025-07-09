import streamlit as st

# Configuração da página

st.set_page_config(page_title="Calculadora TMB", page_icon="logo_saude_TMB.jpg", layout="centered")

# Cabeçalho da página

col1, col2 = st.columns([5,1])

with col1:

    st.title("Calculadora TMB")
    
    
with col2:

    st.image(image="medicina_simbolo.png")

st.markdown("## Olá,seja bem vindo!\n\n")

nome = "calculadora TMB (Taxa Metabólica Basal)"

st.write(f"Esta é uma **{nome}**, uma ferramenta utilizada por médicos e nutricionistas para avaliar" 
" as necessidades calóricas de uma pessoa por dia, ou seja, a quantidade necessária de calorias que devem ser ingeridas" 
" para que as funções vitais do organismo sejam mantidas.")

st.write("Existem várias fórmulas para calcular a TMB, para nossa calculadora utilizaremos a equação de Mifflin-St Jeor.")

#Entradas

#Altura
st.markdown("## Digite sua altura: ")
altura = st.number_input("Altura(em cm):",format="%0.2f",min_value=56.4, max_value= 272.0, placeholder="Ex: Se você tem 1,70, digite 170")


#Peso
st.markdown("## Digite seu peso: ")
peso = st.number_input("Peso(em Kg)", format="%0.2f", min_value=2.1, max_value= 635.0, placeholder= "Ex: Se você pesa 80Kg, digite 80")

#Idade
st.markdown("## Digite sua idade: ")
idade = st.number_input("Idade:", format="%0.2f" , min_value= 0.0,max_value=122.0, placeholder="Digite sua idade: ")

#Sexo
st.markdown("## Escolha seu sexo: ")
sexo = st.selectbox("Sexo:",("Masculino","Feminino"))

#Cálculo da TMB

#Homens: TMB = (10 x peso em kg) + (6,25 x altura em cm) - (5 x idade em anos) + 5 
#Mulheres: TMB = (10 x peso em kg) + (6,25 x altura em cm) - (5 x idade em anos) - 161

if sexo =="Masculino":

    tmb = (10 * peso) + (6.25 * altura) - (5 * idade) + 5

if sexo =="Feminino":

    tmb = (10 * peso) + (6.25 * altura) - (5 * idade ) - 161

#Exibindo o resultado:

if st.button("# Calcular TMB ", icon="⚕"):
    st.markdown(f"#### Sua taxa metabólica basal é: {tmb} kcal/dia")


