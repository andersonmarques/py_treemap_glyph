from observer.file_observable import FileObservable

import pandas as pd

class DataLoaderModel (FileObservable):

    def __init__(self, file = None) -> None:
        super().__init__()
        self.data_frame = pd.DataFrame()
        # self.__df_same_size: pd.DataFrame = pd.DataFrame()
        self.file = file
        self.categorical_columns = []

    def load_file(self, file_path):
        if file_path is None:
            raise Exception("Erro: File not found")
        else:
            self.file = file_path
            self.data_frame = pd.read_csv(f'{self.file}', sep='\t', encoding='utf-8')
            # print(f'Passou aqui para carregar o arquivo {self.file}.')
            self.categorical_columns = self.get_categorical_columns()
            return self.data_frame
    
    def is_empty_columns(self):
        '''Retorna True se o dataframe não tiver colunas
        
        ### Returns:
        Retorna True se o DataFrame não tiver colunas, caso contrário, retorna False
        '''
        return self.data_frame.columns.empty
    
    def get_columns(self):
        '''Retorna uma lista com os nomes das colunas do dataframe

        ### Returns:
        - list: Lista com os nomes das colunas do dataframe
        '''
        return self.data_frame.columns.tolist()
    
    def get_column_values(self, column):
        '''Retorna uma lista com os valores da coluna do dataframe
        ### Args:
        - column: str - Nome da coluna do dataframe

        ### Returns:
        - list: Lista com os valores da coluna do dataframe
        '''
        return self.data_frame[column].tolist()
    
    def get_column_unique_values(self, column):
        '''Retorna uma lista com os valores únicos da coluna do dataframe
        ### Args:
        - column: str - Nome da coluna do dataframe

        ### Returns:
        - list: Lista com os valores únicos da coluna do dataframe
        '''
        return self.data_frame[column].unique().tolist()
    
    def get_column_unique_values_count(self, column):
        '''Retorna a contagem de valores únicos da coluna do dataframe
        ### Args:
        - column: str - Nome da coluna do dataframe

        ### Returns:
        - pandas.core.series.Series: Contagem de valores únicos da coluna do dataframe
        '''
        # print(f'TIPO: {type(self.data_frame[column].value_counts())}')
        return self.data_frame[column].value_counts()
    
    def get_column_unique_values_count_dict(self, column):
        '''Retorna uma lista com os valores únicos da coluna do dataframe
        ### Args:
        - column: str - Nome da coluna do dataframe

        ### Returns:
        - dict: Dicionário com os valores únicos da coluna e a quantidade de ocorrencia
        '''
        return self.data_frame[column].value_counts().to_dict()
    
    def get_column_unique_values_count_dict_with_percentage(self, column):
        '''Retorna uma lista com os valores únicos da coluna do dataframe
        ### Args:
        - column: str - Nome da coluna do dataframe

        ### Returns:
        - dict: Dicionário com os valores únicos da coluna e a porcentagem de ocorrencia
        '''
        return self.data_frame[column].value_counts(normalize=True).to_dict()
    
    def check_categorical_column(self, column):
        '''Method to check if the column is categorical
        ### Args:
        - column: str - Column name

        ### Returns:
        - bool: Return True if the column is categorical, otherwise False
        '''
        is_categorical = False
        quant_unique_values = len(self.get_column_unique_values(column))
        # print(f'QUANTIDADE DE VALORES ÚNICOS: \n{self.get_column_unique_values_count(column)}')
        if quant_unique_values <= 10:
            is_categorical = True  
        return is_categorical
    
    def get_categorical_columns(self) -> list:
        '''
        Methods to get all categorical columns from the dataframe

        ### Returns:
        - list: List with all categorical columns from the dataframe
        '''
        categorical_columns = []
        if not self.is_empty_columns():
            for column in self.get_columns():
                if self.check_categorical_column(column):
                    categorical_columns.append(column)
        return categorical_columns
    
    ################ Properties ########################

    @property
    def data_frame(self) -> pd.DataFrame:
        return self.__data_frame
    
    @data_frame.setter
    def data_frame(self, data_frame : pd.DataFrame):
        # Cria uma nova coluna no dataframe chamada SAME_SIZE com valor 1
        data_frame['SAME_SIZE'] = '1'
        self.__data_frame = data_frame

    @property
    def file(self):
        return self.__file
    
    @file.setter
    def file(self, file):
        self.__file = file

    @property
    def categorical_columns(self):
        return self.__categorical_columns
    
    @categorical_columns.setter
    def categorical_columns(self, columns):
        self.__categorical_columns = columns

    # @property
    # def df_same_size(self):
    #     '''
    #     Cria uma nova coluna no dataframe chamada SAME_SIZE com valor 1
    #     ### Returns:
    #     Retorna um dataframe com uma coluna a mais chamada SAME_SIZE com valor 1'''
    #     return self.__df_same_size
    
    # @df_same_size.setter
    # def df_same_size(self, df_same_size: pd.DataFrame):
    #     # Cria uma nova coluna no dataframe chamada SAME_SIZE com valor 1
    #     df_same_size['SAME_SIZE'] = '1'
    #     self.__df_same_size = df_same_size
    
