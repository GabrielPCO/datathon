# Libs

import pandas as pd

# libs gráficas

import matplotlib.pyplot as plt

# Streamlit

import streamlit as st

# Função para a leitura da base de dados
@st.cache_data
def read_csv_file(file):
    return pd.read_csv(file)

# Função do botão de Download para converter o DataFrame em .csv
@st.cache_data
def convert_df(df):
    return df.to_csv().encode('utf-8')

# Carregamento de imagens por cach
@st.cache_data
def load_img(img):
    return plt.imread(img)

st.set_page_config(layout="centered",page_icon="🗃️")

# Código para alinhar imagens expandidas no centro da tela e justificar textos
st.markdown(
    """
    <style>
        body {text-align: justify}
        button[title^=Exit]+div [data-testid=stImage]{
            text-align: center;
            display: block;
            margin-left: auto;
            margin-right: auto;
            width: 100%;
        }
    </style>
    """, unsafe_allow_html=True
)

# Alterando cor dos hyperlinks
st.markdown(
   """
    <style>
     a:link {
       color: #F63366;
       background-color: transparent;
       text-decoration: none;
     }

     a:visited {
        color: #98072d;
        background-color: transparent;
        text-decoration: none;
    }

     a:hover {
        color: #F63366;
        background-color: transparent;
        text-decoration: none;
    }

    a:active {
        color: #F63366;
        background-color: transparent;
        text-decoration: none;
    }
    </style>
    """ , unsafe_allow_html=True
)

'''
## 🗃️ Dataset
'''
st.image(load_img('Imagens/dataframe.png'))
'''

Os dados visualizados abaixo foram produzidos originalmente pela Associação Passos Mágicos, relacionados aos projetos de Pesquisa Extensiva do Desenvolvimento Educacional realizados na institruição, e estão anonimizados para uso técnico. Técnicas de limpeza e processamento de dados foram aplicadas para atender aos objetivos da análise de dados
e construção do modelo de Machine Learning.

Em resumo, a tabela apresenta dados cadastrais e de desempenho acadêmico, estes relacionados ao Índice de Desenvolvimento Educacional (INDE), de 1348 alunos entre os anos de 2020 e 2022. Para viabilizar um dataset consistente em toda a série temporal, apenas colunas presentes nos 3 anos foram considerados para as análises.
Ao final, foi obtida uma tabela composta por 18 colunas e 2275 linhas, sendo 727 alunos em 2020, 686 alunos em 2021 e 862 alunos em 2022.

A última coluna, de nome Ponto de Virada, é a coluna target do modelo desenvolvido, que visa prever o atingimento do Ponto de Virada através do desempenho e características do aluno analisado.

Por vim, é importante ressaltar que cada linha da tabela é compreendida como um aluno independente, mesmo para alunos que estiveram mais de um ano com a Passos Mágicos.
Isso ocorre, pois o modelo busca avaliar a trajetória do aluno ano a ano e verificar a possibilidade do mesmo atingir seu ponto de virada naquele momento.

'''
df = read_csv_file('Dataset/df_passos_target.csv')
df = df.rename(columns={"ID":"Nº Aluno","BOLSISTA":"Bolsista","SINALIZADOR_INGRESSANTE":"Ingressante","ANOS_PM":"Anos na PM","ANO_PESQUISA":"Ano da Pesquisa","INSTITUICAO_ENSINO_ALUNO":"Instituição do Aluno","FASE":"Fase","TURMA":"Turma","PEDRA":"Classificação","PONTO_VIRADA":"Ponto de Virada (Target)"})
df["Bolsista"] = df["Bolsista"].map({1:"Sim",0:"Não"})
df["Ingressante"] = df["Ingressante"].map({1:"Sim",0:"Não"})
df['Ano da Pesquisa'] = df['Ano da Pesquisa'].apply(str).replace(',','',regex=True).astype(int)
df["INDE"] = df["INDE"].astype(float).round(2)
df["IAA"] = df["IAA"].astype(float).round(2)
df["IEG"] = df["IEG"].astype(float).round(2)
df["IPS"] = df["IPS"].astype(float).round(2)
df["IDA"] = df["IDA"].astype(float).round(2)
df["IPP"] = df["IPP"].astype(float).round(2)
df["IPV"] = df["IPV"].astype(float).round(2)
df["IAN"] = df["IAN"].astype(float).round(2)
df["Ponto de Virada (Target)"] = df["Ponto de Virada (Target)"].map({1:"Alcançado",0:"Não alcançado"})
df = df.sort_values(['Nº Aluno', 'Ano da Pesquisa'])

# Convertendo o DataFrame em .csv
csv = convert_df(df)

st.dataframe(df.style.format(thousands="", precision=2), hide_index=True)

# Botão de Download do DataFrame
st.download_button(
    label="Download do CSV",
    data=csv,
    file_name='passos_mágicos.csv',
    mime='text/csv',
)