import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from PyQt6.QtWidgets import QApplication, QSystemTrayIcon, QMenu
from PyQt6.QtGui import QIcon, QPixmap

import pandas as pd

from view.main import Main
from observer.file_selection_observer import File_Selection_Observer

class Visualization_Controller (File_Selection_Observer):
    def __init__(self):
        self.init_gui()
        # self.selected_file = None

    def update_file_selection(self, file_path):
        self.selected_file = file_path
        self.handle_file_selection()

    def update_closing(self):
        pass

    def init_gui(self):
        app = QApplication(sys.argv)
        self.__main_view = Main()
        self.__main_view.attach_observer(self)
        self.__main_view.show()
        sys.exit(app.exec())

    def handle_file_selection(self):
        data = pd.read_csv(f'{self.__main_view.selected_file}', sep='\t', encoding='utf-8')

        print(data.head(6))

    

if __name__ == "__main__":
    # app = QtWidgets.QApplication(sys.argv)
    controller = Visualization_Controller()
   