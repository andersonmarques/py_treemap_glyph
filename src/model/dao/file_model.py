from observer.file_observable import File_Observable

import pandas as pd

class File_Model (File_Observable):

    def __init__(self, file = None) -> None:
        super().__init__()
        self.__data_frame: pd.DataFrame = pd.DataFrame()
        self.__df_same_size: pd.DataFrame = pd.DataFrame()
        self.__file = file

    def load_file(self, file_path):
        if file_path is None:
            raise Exception("Erro: File not found")
        else:
            self.file = file_path
            self.data_frame = pd.read_csv(f'{self.file}', sep='\t', encoding='utf-8')
            
            return self.data_frame
    
    def is_empty_columns(self):
        '''Retorna True se o dataframe não tiver colunas'''
        return self.data_frame.columns.empty
    
    def get_columns(self):
        '''Retorna uma lista com os nomes das colunas do dataframe'''
        return self.data_frame.columns.tolist()
    
    def get_column_values(self, column):
        '''Retorna uma lista com os valores da coluna do dataframe'''
        return self.data_frame[column].tolist()
    
    def get_column_unique_values(self, column):
        '''Retorna uma lista com os valores únicos da coluna do dataframe'''
        return self.data_frame[column].unique().tolist()
    
    def get_column_unique_values_count(self, column):
        '''Retorna a contagem de valores únicos da coluna do dataframe'''
        print(f'TIPO: {type(self.data_frame[column].value_counts())}')
        return self.data_frame[column].value_counts()
    
    def get_column_unique_values_count_dict(self, column):
        '''Retorna uma lista com os valores únicos da coluna do dataframe'''
        return self.data_frame[column].value_counts().to_dict()
    
    def get_column_unique_values_count_dict_with_percentage(self, column):
        '''Retorna uma lista com os valores únicos da coluna do dataframe'''
        return self.data_frame[column].value_counts(normalize=True).to_dict()
    
    @property
    def data_frame(self):
        return self.__data_frame
    
    @data_frame.setter
    def data_frame(self, data_frame):
        self.__data_frame = data_frame

    @property
    def file(self):
        return self.__file
    
    @file.setter
    def file(self, file):
        self.__file = file

    @property
    def df_same_size(self):
        '''Retorna um dataframe com uma coluna a mais chamada SAME_SIZE com valor 1'''
        return self.__df_same_size
    
    @df_same_size.setter
    def df_same_size(self, df_same_size: pd.DataFrame):
        #como criando uma nova coluna em um data frame
        df_same_size['SAME_SIZE'] = '1'
        self.__df_same_size = df_same_size
    
