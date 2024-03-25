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
## Análise exploratória
'''
#st.image(load_img('Imagens/processamento_analise.png'))

Dashboard_Power_BI = '<iframe title="datathon_alura_pos_tech" style="width:90.3%; height:1700px" src="https://app.powerbi.com/view?r=eyJrIjoiNGYwMjk2NmQtNjIyMi00MjNkLTk1MzYtYmMyYjc5NDUyYjU4IiwidCI6IjExZGJiZmUyLTg5YjgtNDU0OS1iZTEwLWNlYzM2NGU1OTU1MSIsImMiOjR9" frameborder="0" allowFullScreen="true"></iframe>'

with st.container(border=False):
    st.markdown(Dashboard_Power_BI, unsafe_allow_html=True)