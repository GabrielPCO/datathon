# libs gráficas

import matplotlib.pyplot as plt

# Streamlit

import streamlit as st
from st_pages import show_pages_from_config

# Configurando a página
st.set_page_config(
    page_title="Datathon",
    page_icon="🏫",
    layout="centered",
    initial_sidebar_state="auto",
    menu_items={
        'About': "Projeto criado para o *Datathon* do curso de pós-graduação da FIAP/Alura."
    }
)

# Carregamento de imagens por cach
@st.cache_data
def load_img(img):
    return plt.imread(img)

# Titulo de Página
st.title('Análise de dados: impacto da Associação Passos Mágicos no município de Embu-Guaçu')

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

st.markdown('''<video controls width="700" height="400" autoplay="true" muted="true" loop="true" poster="https://niverdobem.com.br/wp-content/uploads/2020/10/18A3D82B-2FDB-4355-A9D1-FBAA99E56F41.jpeg" controlsList="nodownload">
            <source 
            src="https://tinyurl.com/datathon-video" 
            type="video/mp4"/>
            </video>''', unsafe_allow_html=True)

show_pages_from_config()

url = 'https://passosmagicos.org.br/'
link = 'Associação Passos Mágicos'
#st.image(load_img('Imagens/passos_magicos_home.jpg'))
st.markdown(f'[{link}]({url})')

'''
## Explorando dados do impacto da Associação Passos Mágicos no município de Embu-Guaçu.


Links importantes:

[passosmagicos.org.br](https://passosmagicos.org.br/) - Site oficial da Associação Passos Mágicos

[cidades.ibge.gov.br](https://cidades.ibge.gov.br/brasil/sp/embu-guacu/panorama) - Censo IBGE para o município de Embu-Guaçu

Links dos integrantes do projeto:

[github.com/GabrielPCO](https://github.com/GabrielPCO) - Github Gabriel Oliveira

[github.com/jackson-simionato](https://github.com/jackson-simionato) - Github Jackson Simionato

gabrielpcoliveira@gmail.com - Email Gabriel Oliveira

simionato.jackson@gmail.com - Email Jackson Simionato

haendelf@hotmail.com - Email Haendel Oliveira

'''
st.divider()
'''
## Resumo

A Associação Passos Mágicos tem uma trajetória de 30 anos de atuação, trabalhando na transformação da vida de crianças e jovens de baixa renda os levando a melhores oportunidades de vida.

A transformação, idealizada por Michelle Flues e Dimetri Ivanoff, começou em 1992, atuando dentro de orfanatos, no município de Embu-Guaçu.

Em 2016, depois de anos de atuação, decidem ampliar o programa para que mais jovens tivessem acesso a essa fórmula mágica para transformação que inclui: educação de qualidade, auxílio psicológico/psicopedagógico, ampliação de sua visão de mundo e protagonismo. Passaram então a atuar como um projeto social e educacional, criando assim a Associação Passos Mágicos.

Nesse documento iremos analisar o impacto da associação em Embu-Guaçu e os aspectos mais significativos da influência do trabalho da Associação Passos Mágicos no município.

Além disso, disponibilizamos aos professores uma aplicação web (Formulário APV) para a análise do Ponto de Virada dos alunos. A aplicação foi feita utilizando-se técnicas de machine learning que são detalhadas na aba 'Modelo' deste documento.
'''
st.divider()
'''

## Observação

Os demais dados, DataFrames e outras análises mais aprofundadas podem ser encontradas na página de Github dos integrantes do grupo referenciadas no início desse documento.
'''