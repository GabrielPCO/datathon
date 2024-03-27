# libs gráficas

import matplotlib.pyplot as plt

# Streamlit

import streamlit as st

st.set_page_config(layout="centered",page_icon="📊")

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

'''
## :bar_chart: Modelo de análise do Ponto de Virada &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(APV)
'''
st.image(load_img('Imagens/ml.png'))
'''

Nesta seção, será descrito o método utilizado no desenvolvimento da aplicação de Machine Learning utilizando os dados disponibilizados pela Associação Passos Mágicos.

O Formulário APV consiste em uma aplicação web que analisa os dados de um aluno específico e, a partir do modelo de Machine Learning, infere se ele está apto a atingir o Ponto de Virada. 

A utilização é muito simples, o usuário da Passos Mágicos precisa apenas inserir os dados do aluno (Instituição, fase, classificação, notas etc.). Em seguida, o modelo compara estas informações com os padrões encontrados na base de dados da Associação e avalia se aquele aluno está apto a alcançar seu Ponto de Virada naquele momento específico de sua jornada escolar. 

O intuito da ferramenta não é classificar alunos que podem chegar ao ponto de virada, mas indicar quais deles precisam de maior atenção do corpo docente.
'''
st.divider()
'''
## Construção do modelo

O método de desenvolvimento do modelo consistiu em 7 etapas, descritas nas seções a seguir:
'''
# Layout das etapas
tab0, tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["Limpeza",
                                                    "Mesclagem",
                                                    "Correlação",
                                                    "Divisão",
                                                    "Pipeline",
                                                    "Avaliação",
                                                    "Seleção"])

with tab0:
    '''
    ## Limpeza dos dados

    Decidiu-se por separar os dados fornecidos pela Associação Passos Mágicos por ano da pesquisa (2020, 2021 e 2022). Desse modo, foi possível trabalhar com uma estruturação de dados mais simples e mais bem ajustada.
    
    Inicialmente, os valores nulos foram verificados e tratados de acordo com o seu contexto, sendo ora excluídos ora alterados por valores mais adequados, de acordo com o contexto. 
    
    Em seguida, os valores de cada coluna foram associados com seus tipos de dados mais adequados e, por fim,
    as colunas dos dataframes foram reorganizados de forma mais coerente possível.
    
    O resultado para cada dataframe foi o seguinte:

    ## DataFrame Passos 2020

    ```python
    df_passos_2020.info()
    ```
    ```
    <class 'pandas.core.frame.DataFrame'>
    Index: 727 entries, 1 to 1348
    Data columns (total 19 columns):
    #   Column                         Non-Null Count  Dtype   
    ---  ------                         --------------  -----   
    0   INSTITUICAO_ENSINO_ALUNO_2020  727 non-null    category
    1   IDADE_ALUNO_2020               727 non-null    Int16   
    2   ANOS_PM_2020                   727 non-null    Int16   
    3   FASE_2020                      727 non-null    category
    4   TURMA_2020                     727 non-null    category
    5   PONTO_VIRADA_2020              727 non-null    bool    
    6   INDE_2020                      727 non-null    Float64 
    7   INDE_CONCEITO_2020             727 non-null    category
    8   PEDRA_2020                     727 non-null    category
    9   DESTAQUE_IEG_2020              727 non-null    category
    10  DESTAQUE_IDA_2020              727 non-null    category
    11  DESTAQUE_IPV_2020              727 non-null    category
    12  IAA_2020                       727 non-null    Float64 
    13  IEG_2020                       727 non-null    Float64 
    14  IPS_2020                       727 non-null    Float64 
    15  IDA_2020                       727 non-null    Float64 
    16  IPP_2020                       727 non-null    Float64 
    17  IPV_2020                       727 non-null    Float64 
    18  IAN_2020                       727 non-null    Float64 
    dtypes: Float64(8), Int16(2), bool(1), category(8)
    memory usage: 65.5 KB
    ```
    '''
    st.divider()
    '''
    ## DataFrame Passos 2021

    ```python
    df_passos_2021.info()
    ```
    ```
    <class 'pandas.core.frame.DataFrame'>
    Index: 686 entries, 1 to 1348
    Data columns (total 20 columns):
    #   Column                         Non-Null Count  Dtype   
    ---  ------                         --------------  -----   
    0   INSTITUICAO_ENSINO_ALUNO_2021  686 non-null    category
    1   FASE_2021                      686 non-null    category
    2   TURMA_2021                     686 non-null    category
    3   PONTO_VIRADA_2021              686 non-null    bool    
    4   SINALIZADOR_INGRESSANTE_2021   686 non-null    bool    
    5   INDE_2021                      686 non-null    Float64 
    6   PEDRA_2021                     686 non-null    category
    7   IAA_2021                       686 non-null    Float64 
    8   IEG_2021                       686 non-null    Float64 
    9   IPS_2021                       686 non-null    Float64 
    10  IDA_2021                       686 non-null    Float64 
    11  IPP_2021                       686 non-null    Float64 
    12  IPV_2021                       686 non-null    Float64 
    13  IAN_2021                       686 non-null    Float64 
    14  REC_EQUIPE_1_2021              686 non-null    category
    15  REC_EQUIPE_2_2021              686 non-null    category
    16  REC_EQUIPE_3_2021              686 non-null    category
    17  REC_EQUIPE_4_2021              686 non-null    category
    18  NIVEL_IDEAL_2021               686 non-null    category
    19  DEFASAGEM_2021                 686 non-null    Int16   
    dtypes: Float64(8), Int16(1), bool(2), category(9)
    memory usage: 61.6 KB
    ```
    '''
    st.divider()
    '''
    ## DataFrame Passos 2022

    ```python
    df_passos_2022.info()
    ```
    ```
    <class 'pandas.core.frame.DataFrame'>
    Index: 862 entries, 2 to 1349
    Data columns (total 30 columns):
    #   Column               Non-Null Count  Dtype   
    ---  ------               --------------  -----   
    0   ANO_INGRESSO_2022    862 non-null    Int16   
    1   BOLSISTA_2022        862 non-null    bool    
    2   FASE_2022            862 non-null    category
    3   TURMA_2022           862 non-null    category
    4   PONTO_VIRADA_2022    862 non-null    bool    
    5   INDE_2022            862 non-null    Float64 
    6   PEDRA_2022           862 non-null    category
    7   CG_2022              862 non-null    Int16   
    8   CF_2022              862 non-null    Int16   
    9   CT_2022              862 non-null    Int16   
    10  DESTAQUE_IEG_2022    862 non-null    category
    11  DESTAQUE_IDA_2022    862 non-null    category
    12  DESTAQUE_IPV_2022    862 non-null    category
    13  IAA_2022             862 non-null    Float64 
    14  IEG_2022             862 non-null    Float64 
    15  IPS_2022             862 non-null    Float64 
    16  IDA_2022             862 non-null    Float64 
    17  IPP_2022             862 non-null    Float64 
    18  IPV_2022             862 non-null    Float64 
    19  IAN_2022             862 non-null    Float64 
    ...
    28  NIVEL_IDEAL_2022     862 non-null    category
    29  INDICADO_BOLSA_2022  862 non-null    bool    
    dtypes: Float64(11), Int16(5), bool(3), category(11)
    memory usage: 112.3 KB
    ```
    '''
with tab1:
    '''
    ## Concatenação dos dados

    Após a limpeza dos dados e separação em tabelas por ano de pesquisa, os três DataFrames processados foram concatenados em uma tabela única.

    Foram escolhidas as colunas de mais interesse para o projeto e, então, aplicada a concatenação dos dados dos três anos.

    ```python
    def generate_df_to_merge(df):
        common_cols = ['ID','NOME','ANO_PESQUISA','INSTITUICAO_ENSINO_ALUNO','BOLSISTA','ANOS_PM','SINALIZADOR_INGRESSANTE','FASE','TURMA','PONTO_VIRADA','INDE',
                    'PEDRA', 'IAA','IEG','IPS','IDA','IPP','IPV','IAN','NIVEL_IDEAL', 'DEFASAGEM']
        
        ano = df['ANO_PESQUISA'].values[0]

        col_names = [col.split(f'_{ano}')[0] for col in df.columns]
        df.columns = col_names

        df_to_merge = df[common_cols]

        return df_to_merge

    df_2020_to_merge = generate_df_to_merge(df_2020)
    df_2021_to_merge = generate_df_to_merge(df_2021)
    df_2022_to_merge = generate_df_to_merge(df_2022)

    list_dfs = [df_2020_to_merge, df_2021_to_merge, df_2022_to_merge]

    dfs_passos_magicos_merged = pd.DataFrame()

    for df in list_dfs:
        if len(dfs_passos_magicos_merged) == 0:
            dfs_passos_magicos_merged = df.copy()
        else:
            dfs_passos_magicos_merged = pd.concat([dfs_passos_magicos_merged, df], axis=0)
            
    dfs_passos_magicos_merged['NIVEL_IDEAL'] = dfs_passos_magicos_merged['NIVEL_IDEAL'].astype(float)
    dfs_passos_magicos_merged['DEFASAGEM'] = dfs_passos_magicos_merged['DEFASAGEM'].astype(float)
    dfs_passos_magicos_merged['ANOS_PM'] = dfs_passos_magicos_merged['ANOS_PM'].astype(int)
    dfs_passos_magicos_merged.sort_values(by=['ANO_PESQUISA','ID'], inplace=True)
    dfs_passos_magicos_merged.reset_index(drop=True, inplace=True)

    dfs_passos_magicos_merged.to_csv('df_passos_2020_2021_2022.csv', index=False)
    ```
    '''
with tab2:
    '''
    ## Correlação dos atributos

    Com o conjunto de dados devidamente processado e concatenado, decidiu-se por realizar a verificação da correlação entre os atributos presentes no dataset.

    Avaliar a correlação entre atributos é de extrema importância na análise de dados, uma vez que evita a multicolinearidade entre eles. 
    
    Atributos fortemente correlacionadas podem representam a mesma informação e, portanto, não necessitam ser utilizadas em conjunto.    
    ```python
    corr = df_passos_corr.corr()
    plt.figure(figsize=(20,10))
    sns.heatmap(corr, cmap='Blues', annot=True)
    ```
    '''
    st.image(load_img('Imagens/corr.png'))
    '''

    Percebe-se pela imagem que no geral as colunas do dataframe não possuem uma correlação forte e, portanto, podemos utilizá-las para a criação do nosso modelo em aprendizado de máquina.
    '''
with tab3:
    '''
    ## Criação dos conjuntos de treino e teste

    Em modelos de Machine Learning, outra etapa básica e essencial é a separação do conjunto de dados em subconjuntos de treino e teste. O primeiro é utilizado no treinamento do algoritmo, enquanto o conjunto de teste é empregado exclusivamente
    na validação dos resultados do modelo treinado.
    
    O tamanho de teste escolhido foi de 0,2, ou seja, 80% dos registros compõem o conjunt de treino e 20% entram no conjunto de teste.
    
    ```python
    from sklearn.model_selection import train_test_split

    SEED = 1561656
    df_treino, df_teste = train_test_split(df_passos_target, test_size=0.2, random_state=SEED)

    df_treino.shape
    (1816, 18)

    df_teste.shape
    (455, 18)
    ```
    '''
with tab4:
    '''
    ## Pipeline do modelo

    É interessante que seja construído um pipeline do modelo para que novos dados possam ser processados de forma eficaz e a ocorrência de erros durante o processo de geração do modelo seja reduzida.

    O pipeline é uma forma de automatizar o fluxo de trabalho necessário para produzir um modelo de aprendizado de máquina. Os pipelines de aprendizado de máquina consistem em várias etapas sequenciais que atuam desde a extração e pré-processamento de dados até treinamento e implantação de modelo.
    
    Para esse projeto, foi criado um pipeline que consiste das seguintes características:
    
    ## Drop Features

    Remoção de atributos que não serão utilizadas pelo modelo
    
    ```python
    class DropFeatures(BaseEstimator, TransformerMixin):
        def __init__(self, feature_to_drop=['ID', 'ANO_PESQUISA', 'TURMA']):
            self.feature_to_drop = feature_to_drop
        
        def fit(self, df):
            return self
        
        def transform(self, df):
            if set(self.feature_to_drop).issubset(df.columns):
                df.drop(self.feature_to_drop, axis=1, inplace=True)
                return df
            else:
                print('Uma ou mais features não estão no DataFrame')
                return df
    ```
    '''
    st.divider()
    '''

    ## Min Max Scaler

    Aplicação de MinMaxScaler para a normalização dos dados antes do processo de fitting

    ```python
    class MinMaxWithFeatNames(BaseEstimator, TransformerMixin):
        def __init__(self, min_max_scaler = ['ANOS_PM', 'INDE', 'IAA', 'IEG', 'IPS', 'IDA', 'IPP', 'IPV', 'IAN']):
            self.min_max_scaler = min_max_scaler

        def fit(self, df):
            return self
        
        def transform(self, df):
            if set(self.min_max_scaler).issubset(df.columns):
                min_max_enc = MinMaxScaler()
                df[self.min_max_scaler] = min_max_enc.fit_transform(df[self.min_max_scaler])
                return df
            else:
                print('Um ou mais atributos não estão no DataFrame')
                return df
    ```
    '''
    st.divider()
    '''

    ## One Hot Encoder

    Utilização de OneHotEncoder para a binarização das variáveis de texto

    ```python
    class OneHotEncodingNames(BaseEstimator, TransformerMixin):
        def __init__(self, OneHotEncoding = ['INSTITUICAO_ENSINO_ALUNO', 'PEDRA']):
            self.OneHotEncoding = OneHotEncoding

        def fit(self, df):
            return self

        def transform(self, df):
            if set(self.OneHotEncoding).issubset(df.columns):
                def one_hot_enc(df, OneHotEncoding):
                    one_hot_enc = OneHotEncoder()
                    one_hot_enc.fit(df[OneHotEncoding])
                    feature_names = one_hot_enc.get_feature_names_out(OneHotEncoding)
                    df = pd.DataFrame(one_hot_enc.transform(df[self.OneHotEncoding]).toarray(),
                                    columns=feature_names, index=df.index)
                    return df
            
                def concat_with_rest(df, one_hot_enc_df, OneHotEncoding):
                    outras_features = [feature for feature in df.columns if feature not in OneHotEncoding]
                    df_concat = pd.concat([one_hot_enc_df, df[outras_features]], axis=1)
                    return df_concat
                
                df_OneHotEncoding = one_hot_enc(df, self.OneHotEncoding)

                df_full = concat_with_rest(df, df_OneHotEncoding, self.OneHotEncoding)

                return df_full
            else:
                print('Um ou mais atributos não estão no DataFrame')
                return df
    ```
    '''
    st.divider()
    '''

    ## Ordinal Feature

    Realizou-se a organização dos dados por Ordinal Feature em casos de atributos em formato de texto e que possuem ordem (por exemplo a fase do aluno)

    ```python
    class OrdinalFeature(BaseEstimator, TransformerMixin):
        def __init__(self, ordinal_feature = ['FASE']):
            self.ordinal_feature = ordinal_feature

        def fit(self, df):
            return self
        
        def transform(self, df):
            if 'FASE' in df.columns:
                ordinal_encoder = OrdinalEncoder()
                df[self.ordinal_feature] = ordinal_encoder.fit_transform(df[self.ordinal_feature])
                return df
            else:
                print('Fase não está no DataFrame')
                return df
    ```
    '''
    st.divider()
    '''

    ## Oversample

    Utilização de Oversampling para o aumento da representatividade de nossa base, visto que estamos trabalhando com uma base limitada nessa questão

    ```python
    class Oversample(BaseEstimator, TransformerMixin):
        def __init__(self):
            pass

        def fit(self, df):
                return self
        
        def transform(self, df):
            oversample = SMOTE(sampling_strategy='minority')
            X_bal, y_bal = oversample.fit_resample(df.loc[:, df.columns != 'PONTO_VIRADA'], df['PONTO_VIRADA'])
            df_bal = pd.concat([pd.DataFrame(X_bal), pd.DataFrame(y_bal)], axis=1)
            return df_bal
    ```
    '''
    st.divider()
    '''

    ## Rebalanceamento

    E finalmente, o rebalanceamento dos dados referentes a coluna target (Ponto de Virada)

    ```python
    df_passos_target['PONTO_VIRADA'].value_counts(normalize=True)*100

    PONTO_VIRADA
    0    86.129458
    1    13.870542
    Name: proportion, dtype: float64

    treino['PONTO_VIRADA'].value_counts(normalize=True)*100

    PONTO_VIRADA
    0    50.0
    1    50.0
    Name: proportion, dtype: float64
    ```
    '''
with tab5:
    '''
    ## Avaliação do modelo

    Para avaliar e selecionar o modelo mais preciso foram calculados a Matriz de Confusão, o Classification Report e a Curva ROC.

    ```python
    def roda_modelo(modelo):
        modelo.fit(X_treino, y_treino)

        print(f'------------------------ Resultados {modelo} ------------------------')

        print(f'Confusion Matrix')

        matiz_confusao = ConfusionMatrixDisplay.from_estimator(
            modelo,
            X_teste,
            y_teste,
            display_labels=['PV-Positivo', 'PV-Negativo'],
            cmap=plt.cm.Blues,
            normalize='true',
        )
        matiz_confusao.ax_.set_title('Matrix de Confuzão Normalizada', fontsize=16, fontweight='bold')
        matiz_confusao.ax_.set_xlabel('Label predita', fontsize=18)
        matiz_confusao.ax_.set_ylabel('Label verdadeira', fontsize=18)
        plt.grid(False)
        plt.show(matiz_confusao)

        prediction = modelo.predict(X_teste)
        print('Classification Report')
        print(classification_report(y_teste, prediction, zero_division=0))

        print('ROC curve')
        metrics.RocCurveDisplay.from_estimator(modelo, X_teste, y_teste)
    ```
    '''
    st.divider()
    '''
    ## Logistic Regression

    ```
    ------------------------ Resultados LogisticRegression() ------------------------
    Classification Report

              precision    recall  f1-score   support

           0       0.95      0.93      0.94       384
           1       0.93      0.95      0.94       384

    accuracy                           0.94       768
    macro avg      0.94      0.94      0.94       768
    weighted avg   0.94      0.94      0.94       768
    ```
    '''
    st.image(load_img('Imagens/mc_logistico.png'))
    st.image(load_img('Imagens/roc_logistico.png'))
    st.divider()
    '''
    ## Decision Tree Classifier

    ```
    ------------------------ Resultados DecisionTreeClassifier() ------------------------
    Classification Report

              precision    recall  f1-score   support

           0       0.96      0.99      0.98       384
           1       0.99      0.96      0.98       384

    accuracy                           0.98       768
    macro avg      0.98      0.98      0.98       768
    weighted avg   0.98      0.98      0.98       768
    ```
    '''
    st.image(load_img('Imagens/mc_tree.png'))
    st.image(load_img('Imagens/roc_tree.png'))
    st.divider()
    '''
    ## Gradient Boosting Classifier
    ```
    ------------------------ Resultados GradientBoostingClassifier() ------------------------
    Classification Report

              precision    recall  f1-score   support

           0       0.98      0.99      0.99       384
           1       0.99      0.98      0.99       384

    accuracy                           0.99       768
    macro avg      0.99      0.99      0.99       768
    weighted avg   0.99      0.99      0.99       768
    ```
    '''
    st.image(load_img('Imagens/mc_xgb.png'))
    st.image(load_img('Imagens/roc_xgb.png'))
    st.divider()
    '''
    ## Random Forest Classifier

    ```
    ------------------------ Resultados RandomForestClassifier() ------------------------
    Classification Report

              precision    recall  f1-score   support

           0       0.98      0.98      0.98       384
           1       0.98      0.98      0.98       384

    accuracy                           0.98       768
    macro avg      0.98      0.98      0.98       768
    weighted avg   0.98      0.98      0.98       768
    ```
    '''
    st.image(load_img('Imagens/mc_forest.png'))
    st.image(load_img('Imagens/roc_forest.png'))
with tab6:
    '''
    ## Seleção do modelo

    Ao final, o modelo selecionado foi o Gradient Boosting Classifier, pois a partir dele foram obtidos os melhores resultados, tanto de precisão quanto de f1-score.

    O aumento de gradiente (Gradient Boosting) refere-se a uma classe de algoritmos de aprendizado de máquina que pode ser usada para problemas de classificação ou de regressão. 
    
    No caso deste projeto, o Gradient Boosting Classifier se mostrou um algoritmo muito eficaz e precisa, principalmente neste contexto em que foi necessário trabalhar com dezenas de variáveis para classificar alunos que atingiram o Ponto de Virada.
    '''