import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from PyQt6.QtWidgets import QApplication

from view.main_view import MainView
from model.dao.dataloader_model import DataLoaderModel

class VisualizationController:
    def __init__(self):
        self.data_loader_model = DataLoaderModel()
        self.init_gui()        

    def init_gui(self):
        app = QApplication(sys.argv)
        self.main_view = MainView(controller=self, file_model=self.data_loader_model)
        self.main_view.show()
        self.load_style_file('../css/style.qss', app)
        sys.exit(app.exec())

    def load_style_file(self, file_path, aplicacao):
        current_directory = os.path.dirname(os.path.realpath(__file__))
        style_path = os.path.join(current_directory, file_path)
        with open(style_path, 'r') as style_file:
            style = style_file.read()
        aplicacao.setStyleSheet(style)

    def handle_file_selection(self, file_path):
        '''
        This methods is responsible for load the file selected by the user
        and notify the view to update the widgets
        '''
        # print(f'File selected: {file_path}')
        if file_path != None:
            self.data_loader_model.notify_file_selected(file_path)
            self.main_view.load_attributes_on_gui()
            # self.load_lists_widgets_grid()
            # self.load_lists_widgets_treemap()


    def load_lists_widgets_grid(self):
        if not self.data_loader_model.is_empty_columns():
            self.main_view.load_lists_widgets_grid(sorted(self.data_loader_model.get_columns()))

    # def load_lists_widgets_treemap(self):
    #     # categorical_columns = []
    #     # if not self.data_loader_model.is_empty_columns():
    #     #     for column in self.data_loader_model.get_columns():
    #     #         quant_unique_values = len(self.data_loader_model.get_column_unique_values(column))
    #     #         if quant_unique_values <= 10:
    #     #             categorical_columns.append(column)
                
    #     self.main_view.load_lists_widgets_treemap(sorted(self.data_loader_model.get_categorical_columns()))


if __name__ == "__main__":
    controller = VisualizationController()
   