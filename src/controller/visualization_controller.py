import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from PyQt6.QtWidgets import QApplication, QSystemTrayIcon, QMenu
from PyQt6.QtGui import QIcon, QPixmap

import pandas as pd

from view.main_view import Main_View
from model.dao.file_model import File_Model

class Visualization_Controller:
    def __init__(self):
        self.file_model = File_Model()
        self.init_gui()        

    def init_gui(self):
        app = QApplication(sys.argv)
        self.main_view = Main_View(controller=self, file_model=self.file_model)
        self.main_view.show()
        sys.exit(app.exec())

    def handle_file_selection(self, file_path):
        if file_path != None:
            self.file_model.notify_file_selected(file_path)
            self.load_lists_widgets_grid()
            self.load_lists_widgets_treemap()

    def load_lists_widgets_grid(self):
        # verificar se a lista de colunas, que virá do model, está vazia
        if not self.file_model.is_empty_columns():
            self.main_view.load_lists_widgets_grid(self.file_model.get_columns())

    def load_lists_widgets_treemap(self):
        categorical_columns = []
        if not self.file_model.is_empty_columns():
            for column in self.file_model.get_columns():
                quant_unique_values = len(self.file_model.get_column_unique_values(column))
                # print(f'{column} : {quant_unique_values}')
                if quant_unique_values <= 10:
                    categorical_columns.append(column)
                
            self.main_view.load_lists_widgets_treemap(sorted(categorical_columns))

    # def set_attr_to_treemap_hierarchy(self, attr):
    #     self.main_view.list_widget_hierarchy_treemap.

if __name__ == "__main__":
    controller = Visualization_Controller()
   