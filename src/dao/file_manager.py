import pandas as pd

class File_Manager:

    def __init__(self, file = None) -> None:
        self.__data_frame: pd.DataFrame = pd.DataFrame()
        self.__df_same_size: pd.DataFrame = pd.DataFrame()
        self.__file = file

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
        
    def read_file(self):
        if self.__file is None:
            raise Exception("Erro: File not found")
        else:
            self.__data_frame = pd.read_csv(self.__file)
            return self.__data_frame
        
    def get_columns(self):
        '''Retorna uma lista com os nomes das colunas do dataframe'''
        return self.__data_frame.columns.tolist()
    
    def get_column_values(self, column):
        '''Retorna uma lista com os valores da coluna do dataframe'''
        return self.__data_frame[column].tolist()
    
    def get_column_unique_values(self, column):
        '''Retorna uma lista com os valores únicos da coluna do dataframe'''
        return self.__data_frame[column].unique().tolist()
    
    def get_column_unique_values_count(self, column):
        '''Retorna uma lista com os valores únicos da coluna do dataframe'''
        return self.__data_frame[column].value_counts().tolist()
    
    def get_column_unique_values_count_dict(self, column):
        '''Retorna uma lista com os valores únicos da coluna do dataframe'''
        return self.__data_frame[column].value_counts().to_dict()
    
    def get_column_unique_values_count_dict_with_percentage(self, column):
        '''Retorna uma lista com os valores únicos da coluna do dataframe'''
        return self.__data_frame[column].value_counts(normalize=True).to_dict()
    
    
    
