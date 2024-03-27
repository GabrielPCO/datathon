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
st.title('🏫Impacto socioeducacional da &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Associação Passos Mágicos nas &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;crianças de Embu-Guaçu (SP)')

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

st.markdown('''<video controls width="700" height="400" autoplay="true" muted="true" loop="true" poster="https://cryptohub.com.br/DataFrame/passos.png" controlsList="nodownload">
            <source 
            src="https://tinyurl.com/datathon-video" 
            type="video/mp4"/>
            </video>''', unsafe_allow_html=True)

show_pages_from_config()

url = 'https://passosmagicos.org.br/'
link = 'Associação Passos Mágicos'
#st.image(load_img('Imagens/passos_magicos_home.jpg'))
#st.markdown(f'[{link}]({url})')

'''
A Associação Passos Mágicos tem uma trajetória de mais de 30 anos de atuação, trabalhando na transformação da vida de crianças e jovens de baixa renda, alçando crianças a melhores oportunidades através de pilares como educação, ações sociais
e acompanhamento psicopedagógico.

Idealizada por Michelle Flues e Dimitri Ivanoff, esta história de sucesso teve início principalmente nos orfanatos do município de Embu-Guaçu, desde sempre buscando tornar sua região de atuação um lugar em que jovens e crianças tenham igualdade de
oportunidades de crescimento pessoal e profissional.

Atualmente, a Passos Mágicos atende crianças desde os 6 anos até jovens do terceiro ano do Ensino Médio, com iniciativas de aceleração do conhecimento como aulas de português, matemática e inglês, bolsas em instituições de ensino particulares e intercâmbio.
Ainda, fornece acompanhamento psicológico para os alunos e promove atividades culturas e ações sociais, para formar também seres humanos com uma visão de mundo mais crítica e consciente do seu potencial.

Evidentemente, o sucesso da Passos Mágicos depende do esforço e competência de seus colaboradores, que dão seu máximo para cuidar destas crianças com carinho, e dos apoiadores e patrocinadores que enxergam o tamanho da importância da Associação Passos Mágicos
para toda a população de Embu-Guaçu (SP). Neste sentido, é de extrema relevância para a Passos Mágicos mensurar o impacto de suas iniciativas na vida das crianças atendidas, como forma de justificar a expansão de seus programas.

Neste projeto, que é parte do trabalho de conclusão de curso da Pós-Tech em Data Analytics da FIAP, será analisado o impacto da Associação Passos Mágicos com olhar direcionado para as crianças e jovens como indivíduo, para buscar compreender quão influente
o trabalho da Associação Passos Mágicos pode ser na vida de um aluno, levando em conta o contexto socioeconômico de Embu-Guaçu (SP). Para isso, serão analisados principalmente os dados do Índice de Desenvolvimento Educacional (INDE), o indicador de Ponto de Virada
e a relação destes com outras variáveis como a fase dos alunos e a concessão de bolsas em instituições particulares.

Além disso, disponibilizamos a Passos Mágicos uma aplicação web (Formulário APV) para predição do Ponto de Virada de alunos a partir de seus indicadores do INDE. A aplicação foi feita utilizando-se técnicas de Machine Learning que são detalhadas na aba 'Modelo' deste documento.
'''
st.divider()
'''

## Links importantes:

[passosmagicos.org.br](https://passosmagicos.org.br/) - Site oficial da Associação Passos Mágicos

[cidades.ibge.gov.br](https://cidades.ibge.gov.br/brasil/sp/embu-guacu/panorama) - Censo IBGE para o município de Embu-Guaçu

[servicodados.ibge.gov.br](https://servicodados.ibge.gov.br/api/docs/agregados?versao=3) - API de dados agregados do IBGE 
&ensp;
&ensp;
&ensp;
&ensp;
### Contatos dos integrantes do projeto:

[github.com/GabrielPCO](https://github.com/GabrielPCO) - Github Gabriel Oliveira

[github.com/jackson-simionato](https://github.com/jackson-simionato) - Github Jackson Simionato

gabrielpcoliveira@gmail.com - Email Gabriel Oliveira

simionato.jackson@gmail.com - Email Jackson Simionato

haendelf@hotmail.com - Email Haendel Oliveira

'''
st.divider()

'''

## Observação

Os demais dados, DataFrames e outras análises mais aprofundadas podem ser encontradas na página de Github dos integrantes do grupo referenciadas no início desse documento.
'''