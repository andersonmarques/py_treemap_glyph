from abc import ABC, abstractmethod

class File_Observer(ABC):
    @abstractmethod
    def update_file_selection(self, file_path):
        '''Notifies all observers that a file was selected'''
        pass

    @abstractmethod
    def update_closing(self):
        '''Notifies all observers that the application is closing'''
        pass