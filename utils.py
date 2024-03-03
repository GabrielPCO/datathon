import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.preprocessing import MinMaxScaler, OneHotEncoder, OrdinalEncoder

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
            print('Uma ou mais features não estão no DataFrame')
            return df

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
            print('Uma ou mais features não estão no DataFrame')
            return df