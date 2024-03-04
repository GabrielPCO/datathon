#Importação das bibliotecas
import streamlit as st 
import pandas as pd
from sklearn.model_selection import train_test_split
from utils import DropFeatures, OneHotEncodingNames, OrdinalFeature, MinMaxWithFeatNames
from sklearn.pipeline import Pipeline
import joblib

st.set_page_config(layout="centered",page_icon="📝")

# Função para a leitura da base de dados
@st.cache_data
def read_csv_file(file):
    return pd.read_csv(file)

# Função para a carregar o medelo de ml
@st.cache_data
def load_model(file_model):
    return joblib.load(file_model)

#carregando os dados 
dados = read_csv_file('Dataset/df_passos_target.csv')


############################# Streamlit ############################
st.markdown('<style>div[role="listbox"] ul{background-color: #6e42ad}; </style>', unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; '> Formulário de Análise do Ponto de Virada Passos Mágicos </h1>", unsafe_allow_html = True)

st.warning('Preencha o formulário com todos os dados do aluno e clique no botão **ENVIAR** no final da página.')

# Bolsa de Estudos
st.write('### Bolsa de Estudos')
input_bolsista = st.radio('O aluno é bolsista?',['Sim','Não'], index=0)
input_bolsista_dict = {'Sim': 1, 'Não':0}
input_bolsista = input_bolsista_dict.get(input_bolsista)

# Ingressantes na Passos Mágicos
st.write('### Ingressantes')
input_ingressante = st.radio('O aluno é ingressante?',['Sim','Não'], index=0)
input_ingressante_dict = {'Sim': 1, 'Não':0}
input_ingressante = input_ingressante_dict.get(input_ingressante)

# Anos na Passos Mágicos
st.write('### Quantidade de Anos na Passos Mágicos')
input_anos_pm = int(st.slider('Tempo que o aluno está na Passos Mágicos', 0, 4))

# INDE
st.write('### INDE')
input_inde = float(st.slider(label='Qual o INDE do aluno?', step=0.001, min_value = 0.0, max_value = 10.0))

# IAA
st.write('### IAA')
input_iaa = float(st.slider(label='Qual o IAA do aluno?', step=0.001, min_value = 0.0, max_value = 10.0))

# IEG
st.write('### IEG')
input_ieg = float(st.slider(label='Qual o IEG do aluno?', step=0.001, min_value = 0.0, max_value = 10.0))

# IPS
st.write('### IPS')
input_ips = float(st.slider(label='Qual o IPS do aluno?', step=0.001, min_value = 0.0, max_value = 10.0))

# IDA
st.write('### IDA')
input_ida = float(st.slider(label='Qual o IDA do aluno?', step=0.001, min_value = 0.0, max_value = 10.0))

# IPP
st.write('### IPP')
input_ipp = float(st.slider(label='Qual o IPP do aluno?', step=0.001, min_value = 0.0, max_value = 10.0))

# IPV
st.write('### IPV')
input_ipv = float(st.slider(label='Qual o IPV do aluno?', step=0.001, min_value = 0.0, max_value = 10.0))

# IAN
st.write('### IAN')
input_ian = float(st.slider(label='Qual o IAN do aluno?', step=0.001, min_value = 0.0, max_value = 10.0))

# Instituição de Ensino do Aluno
st.write('### Instituição')
input_instituicao_aluno = st.selectbox('Qual a instituição de ensino do aluno?', dados['INSTITUICAO_ENSINO_ALUNO'].sort_values().unique())

# FASE
st.write('### FASE')
input_fase = st.selectbox('Em que fase de ensino o aluno está?', dados['FASE'].sort_values().unique())

# PEDRA
st.write('### PEDRA')
input_pedra = st.selectbox('Qual a classificação (Pedra) do aluno?', dados['PEDRA'].sort_values().unique())

# Lista de todas as variáveis: 
if st.button('Enviar'):
    novo_aluno = [0, # ID
                        input_bolsista, # Bolsa de Estudos
                        input_ingressante, # Ingressantes na Passos Mágicos
                        input_anos_pm, # Anos na Passos Mágicos
                        2020, # Ano Pesquisa
                        input_inde, # INDE
                        input_iaa, # IAA
                        input_ieg, # IEG
                        input_ips, # IPS	
                        input_ida, # IDA
                        input_ipp, # IPP
                        input_ipv, # IPV
                        input_ian, # IAN
                        input_instituicao_aluno, # Instituição de Ensino do Aluno	
                        input_fase, # FASE
                        'A', # Turma
                        input_pedra, # PEDRA
                        0 # target (Ponto de Virada)
                        ]


    # Separando os dados em treino e teste
    def data_split(df, test_size):
        SEED = 1561656
        treino_df, teste_df = train_test_split(df, test_size=test_size, random_state=SEED)
        return treino_df.reset_index(drop=True), teste_df.reset_index(drop=True)

    treino_df, teste_df = data_split(dados, 0.2)

    #Criando novo aluno
    aluno_predict_df = pd.DataFrame([novo_aluno],columns=teste_df.columns)

    #Concatenando novo cliente ao dataframe dos dados de teste
    teste_novo_aluno  = pd.concat([teste_df,aluno_predict_df], ignore_index=True)

    #Pipeline
    def pipeline_teste(df):

        pipeline = Pipeline([
            ('feature_dropper', DropFeatures()),
            ('OneHotEncoding', OneHotEncodingNames()),
            ('ordinal_feature', OrdinalFeature()),
            ('min_max_scaler', MinMaxWithFeatNames()),
        ])
        df_pipeline = pipeline.fit_transform(df)
        return df_pipeline

    #Aplicando a pipeline
    teste_novo_aluno = pipeline_teste(teste_novo_aluno)

    #retirando a coluna target
    aluno_pred = teste_novo_aluno.drop(['PONTO_VIRADA'], axis=1)

    #Predições
    model = load_model('modelo/xgb.joblib')
    final_pred = model.predict(aluno_pred)
    if final_pred[-1] == 1:
        st.success('### O aluno em questão está apto para alcançar seu ponto de virada!')
        st.balloons()
    else:
        st.error('### O aluno em questão precisa de mais atenção para conseguir alcançar seu ponto de virada')