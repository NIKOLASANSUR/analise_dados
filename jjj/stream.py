import streamlit as st
import pandas as pd

st.title("Meu primeiro DashBoard")
st.header("Turma 3C2")
st.subheader("Turma bagunceira ano!")

aluno = "Pedro VAR"
st.write("Olá, ", aluno)

notas = pd.DataFrame({"Disciplina": ["PTBR", "MAT", "PY"], "NOTAS": [1, 5, 10]})
notas

st.write("___________________________________________________________")
materia = st.selectbox ("Selecione su matéria", ["PTBR", "MAT", "PY"])
st.write ("Você selecionou", materia)

st.write("___________________________________________________________")

aluno = st.text_input("Qual o seu nome")

st.write("Olá, ", aluno)




st.write("___________________________________________________________")


notificacoes = st.multiselect("Escolha os alunos:", ["Miguel Seleme", "Sofia Braga", "Cícero", "Matheus Fleming"])

st.write("Vocês foram notificados,", notificacoes)

st.write("___________________________________________________________")

num1, num2 = st.columns([1,2])

num1.title("Soma")

with st.form('addition'):
    a = st.number_input("a")
    b = st.number_input("b")
    submit = st.form_submit_button('add')

if submit:
    num2.title(f'{a+b:.2f}')
    
st.write("___________________________________________________________")
atv = st.button('Aperte aqui')


st.write("Faça a atividade", atv)
