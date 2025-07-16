import streamlit as st
import pandas as pd

# Configuração da página

st.set_page_config(page_title="Calculadora TMB", page_icon="logo_saude_TMB.jpg", layout="centered")


# Seletor de colunas

with st.sidebar:
    caixa_de_seleção = st.selectbox("Selecione uma das ferramentas abaixo: ",("Página inicial","Calculadora TMB","Calculadora IMC"))


if  caixa_de_seleção == "Página inicial":

    # Cabeçalho da página
    col1,col2 = st.columns([5,1])

    with col1:
        
        st.title("Página inicial")

    with col2:

        st.image("medicina_simbolo.png")
        
        
    st.markdown("## Olá, seja bem vindo!\n\n")

    st.write("Este é um mini site feito com a biblioteca streamlit, visando explorar as funcionalidades desta biblioteca.")

    st.write("Duas ferramentas estão disponíveis: Uma calculadora IMC e uma calculadora TMB que podem ser acessadas pela barra lateral. "
             "Caso ela não esteja sendo exibida, clique nas duas setas (>>) localizadas no canto superior direito da página.")
             
    st.markdown("## Divirta-se!!!")

    st.video("cinema.mp4", loop=True, autoplay=True)


#Calculadora TMB
elif caixa_de_seleção == "Calculadora TMB":

    # Cabeçalho da página
    col1, col2 = st.columns([5,1])


    with col1:

        st.title("Calculadora TMB")
    
    
    with col2:

        st.image(image="calorias_logo.png")

    
    st.markdown("## De quantas calorias você necessita?\n\n")

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

#Calculadora IMC

elif caixa_de_seleção == "Calculadora IMC":
    
    # Cabeçalho da página

    col1, col2 = st.columns([5,1])

    with col1:

         st.title("Calculadora IMC")

    with col2:

        st.image(image="peso_icone.png")

    st.markdown("## Seu peso é o ideal?\n\n")

    st.write("O Índice de massa corpórea (IMC) é uma ferramenta utilizada pela OMS para determinar se "
             "o peso atual de um indivíduo é adequado, com base na sua altura e peso.")
    
    st.write("O calculo do IMC baseia-se na divisão do peso do indivíduo (em quilos) pelo quadrado da altura (em metros).")

    #Entradas

    #Altura
    st.markdown("## Digite sua altura: ")
    altura = st.number_input("Altura(em m):",format="%0.2f",min_value=0.564, max_value= 2.72, placeholder="Ex: Se você tem 1,70, digite 1.7")


    #Peso
    st.markdown("## Digite seu peso: ")
    peso = st.number_input("Peso(em Kg)", format="%0.2f", min_value=2.1, max_value= 635.0, placeholder= "Ex: Se você pesa 80Kg, digite 80")

    #Cálculo do IMC

    # IMC = peso/(altura**2)

    imc = peso/(altura**2)

    #Exibindo o resultado:

    if st.button("# Calcular IMC ", icon="⚕"):
        st.markdown("#### Seu índice de massa corpórea é: %.2f" %(imc))

    # Tabela qualitativa IMC

    st.write("Os valores obtidos devem ser comparados com os valores de uma tabela de referência, para fins qualitativos")

    st.markdown("## Tabela de valores de referência")

    # Criando a tabela

    df = pd.DataFrame({
        "Valores de IMC":["menor que 18,5","18,5 - 24,9","25 - 29,9","30,0 - 34,9","35 - 39,9","maior ou igual a 40"],
        "Classificação":["Abaixo do peso","Peso normal","Excesso de peso","Obesidade classe I","Obesidade classe II","Obesidade classe III"]
    })

    # Exibindo a tabela

    st.dataframe(df)

    # Qualificando o IMC do usuário

    st.markdown("### Com base nos resultados ...")

    if imc <= 18.5:

        texto = "abaixo do peso"

        st.write(f"Você está **{texto}**")

    elif imc > 18.5 and imc <= 24.9:

        texto = "peso ideal"

        st.write(f"Você está no **{texto}**")

    elif imc > 24.9 and imc <= 29.9:

        texto = "excesso de peso"

        st.write(f"Você está com **{texto}**")

    elif imc > 29.9 and imc <= 34.9:

        texto = "Obesidade grau I"

        st.write(f"Você está com **{texto}**")

    elif imc > 34.9 and imc <= 39.9:

        texto = "Obesidade grau II"

        st.write(f"Você está com **{texto}**")
    
    else:

        texto = "Obesidade grau III"

        st.write(f"Você está com **{texto}**")

    

    





 