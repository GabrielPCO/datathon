# Streamlit

import streamlit as st

st.set_page_config(layout="centered",page_icon="📖")

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
## Referências

1. GOMES, Pedro César Tebaldi. Conheça as Etapas do Pré-Processamento de dados. DATAGEEKS, 2019. Disponível em: https://www.datageeks.com.br/pre-processamento-de-dados/. Acessado em: 03, março de 2024.

2. WAWERU, Bernice. How to Build a Machine Learning Pipeline With Scikit-Learn in Python. TURING, 2024. Disponível em: https://www.turing.com/kb/building-ml-pipeline-in-python-with-scikit-learn. Acessado em: 03, março de 2024.

3. GOBBO, Debora. Desenvolvimento de um aplicativo Web utilizando Python e Streamlit. DATA HACKERS, 2021. Disponível em: https://medium.com/data-hackers/desenvolvimento-de-um-aplicativo-web-utilizando-python-e-streamlit-b929888456a5. Acessado em: 03, março de 2024.

4. Modelos de machine learning. Databricks, 2023. Disponível em: https://www.databricks.com/br/glossary/machine-learning-models. Acessado em: 03, março de 2024.

5. MAKHIJANI, Charu. Machine Learning Model Deployment as a Web App using Streamlit. Medium, 2023. Disponível em: https://charumakhijani.medium.com/machine-learning-model-deployment-as-a-web-app-using-streamlit-4e542d0adf15. Acessado em: 03, março de 2024.

6. PŁOŃSKI, Piotr. How to save and load Xgboost in Python?. Mljar, 2021. Disponível em: https://mljar.com/blog/xgboost-save-load-python/. Acessado em: 03, março de 2024.

7. ASHRAF, Abdallah. Oversampling — Handling Imbalanced Data. Medium, 2023. Disponível em: https://medium.com/@abdallahashraf90x/oversampling-for-better-machine-learning-with-imbalanced-data-68f9b5ac2696. Acessado em: 03, março de 2024.
'''