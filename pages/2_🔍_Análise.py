# libs gráficas

import matplotlib.pyplot as plt

# Streamlit

import streamlit as st

st.set_page_config(layout="wide",page_icon="🔍")

# Carregamento de imagens por cach
@st.cache_data
def load_img(img):
    return plt.imread(img)

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
## 🔍 Impacto Socioeducacional
'''

col1, col2 = st.columns([0.035,0.965])
with col2:
    '''
    O dashboard a seguir representa uma ferramenta de análise de dados, separado em dois painéis ou abas. 
    O objetivo é dar visibilidade a indicadores socioeducacionais relacionados à atuação da Associação, os quais são relevantes para compreender de que maneira a Passos Mágicos pode ser um agente de transformação na vida da população que ela atende.

    Para melhor entender o impacto da Passos Mágicos, é necessário contextualizar o cenário socioecônomico e educacional da região em que ela atua.
    Desta forma, o primeiro painel busca caracterizar o município de Embu-Guaçu (SP), quanto a sua demografia (sexo, cor/raça, pirâmide etária, etc.), infraestruturas básicas e sistema educacional.

    Já no segundo painel, o objetivo é destrinchar os dados diponibilizados pela Passos Mágicos no âmbito dos projetos de Pesquisa Extensiva do Desenvolvimento Educacional, dos anos de 2020, 2021 e 2022. São apresentados indicadores relacionados
    ao desempenho dos alunos, ao impacto da atuação da Associação no sistema educacional do município e outras análises diversas com objetivo de salientar a importância da oferta de bolsas de estudos em instituições de ensino privadas.

    Um dos principais resultados deste projeto é exatamente esse, poder evidenciar com dados aos interessados da Associação Passos Mágicos que **expandir** parcerias com instituições privadas pode ser um caminho de sucesso para aumentar o impacto da Associação.

    '''
    st.warning(':bulb: Acesse o dashboard em Tela Cheia e explore análises com o espaço exploratório de indicadores no segundo painel!')

    Dashboard_Power_BI = '<p align="center"><iframe title="datathon_alura_pos_tech" style="width:94.1%; height:1700px" src="https://app.powerbi.com/view?r=eyJrIjoiNGYwMjk2NmQtNjIyMi00MjNkLTk1MzYtYmMyYjc5NDUyYjU4IiwidCI6IjExZGJiZmUyLTg5YjgtNDU0OS1iZTEwLWNlYzM2NGU1OTU1MSIsImMiOjR9" frameborder="0" allowFullScreen="true"></iframe></p>'

    st.divider()

    with st.container():
        st.markdown(Dashboard_Power_BI, unsafe_allow_html=True)