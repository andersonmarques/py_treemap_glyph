from abc import ABC, abstractmethod

class File_Selection_Observer(ABC):
    @abstractmethod
    def update_file_selection(self, file_path):
        pass

    @abstractmethod
    def update_closing(self):
        pass