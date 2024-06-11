
from view.qtdesigner_screen import Ui_MainWindow
from observer.file_observer import File_Observer
# from controller.visualization_controller import Visualization_Controller
# from model.dao.file_model import File_Model
import util.contants as const

from PyQt6.QtCore import Qt, QRect, QSize
from PyQt6.QtGui import QResizeEvent,QPixmap, QIcon, QImage
from PyQt6.QtWidgets import QMainWindow, QProgressBar, QFileDialog, QVBoxLayout, QListWidget
from PyQt6.QtGui import QPainter, QBrush, QColor
from PyQt6 import QtWidgets

from PIL import Image, ImageDraw

import pandas as pd

class MainView (QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None, controller=None, file_model=None):
        super().__init__(parent)
        self.setupUi(self)
        self.resizeEvent = self.on_resize #override the method resizeEvent to resize the splitter
        self.showMaximized()    
        ########## reference to the controller
        self.controller = controller

        ########## reference to the model and registering it to the observer ##########
        if file_model != None:
            self.data_loader_model = file_model
            self.data_loader_model.attach_observer(self)
        
        ########## Hide the a tab ##########
        #tab 0: treemap
        #tab 1: grid
        #tab 3: categorical glyphs
        #tab 4: continuous glyphs
        #tab 5: details
        #tab 6: filters
        self.tab_widget_abas.setTabVisible(1, False)

        # self.progressBar = QProgressBar()
        # self.progressBar.setMaximum(100)
        # self.progressBar.setValue(0)
        # self.statusBar().addWidget(self.progressBar)
        self.statusbar.hide()
        self.load_icons_on_gui()
        
        self.action_event_qaction()        
        self.action_event_push_buttons()

    def action_event_qaction(self):
        ''' Actions of the QActions (Menu Itens) '''
        self.action_open_file.triggered.connect(self.on_open_file)
        self.action_treemap.triggered.connect(lambda: self.switch_visualization_tab(0))
        self.action_grid.triggered.connect(lambda: self.switch_visualization_tab(1))

    def action_event_push_buttons(self):
        ''' Actions of the buttons '''
        self.push_button_view_grid.clicked.connect(lambda : self.create_grid_image(10, 10, 
                                                            self.label_visualization_area.height(),
                                                            self.label_visualization_area.height()))
        self.push_button_direita_treemap.clicked.connect(self.choose_attr_to_treemap_hierarchy)
        self.push_button_esquerda_treemap.clicked.connect(self.remove_attr_from_treemap_hierarchy)
        self.push_button_baixo_treemap.clicked.connect(lambda : self.change_list_widget_item_order(0, self.list_widget_hierarchy_treemap))
        self.push_button_cima_treemap.clicked.connect(lambda : self.change_list_widget_item_order(1, self.list_widget_hierarchy_treemap))
        self.push_button_direita_grid.clicked.connect(self.choose_attr_to_grid)
        self.push_button_esquerda_grid.clicked.connect(self.remove_attr_from_grid)
        self.push_button_baixo_grid.clicked.connect(lambda : self.change_list_widget_item_order(0, self.list_widget_selected_attr))
        self.push_button_cima_grid.clicked.connect(lambda : self.change_list_widget_item_order(1, self.list_widget_selected_attr))

    def change_list_widget_item_order(self, direction:int, list_widget:QListWidget):
        '''
        This method changes the order of the attributes in the treemap hierarchy.
        ### Args:   
            direction (int): 0 to down and 1 to up
            list_widget (QListWidget): the list widget to change the order
        '''
        current_index = list_widget.currentRow()
        
        if direction == 0:#down
            if current_index >= 0:
                if current_index < list_widget.count() - 1:
                    list_widget.insertItem(current_index + 1, list_widget.takeItem(current_index))
                    list_widget.setCurrentRow(current_index + 1)
        else:#direction == 1 #up
            if current_index >= 0:
                if current_index > 0:
                    list_widget.insertItem(current_index - 1, list_widget.takeItem(current_index))
                    list_widget.setCurrentRow(current_index - 1)            

    def switch_visualization_tab(self, visualization):
        '''
        This method shows the treemap tab or the grid tab.
        ### Args:
        visualization (int): use 0 to show the treemap tab and 1 to show the grid tab
        '''
        if visualization == const.TREEMAP:
            self.tab_widget_abas.setTabVisible(const.TREEMAP, True)
            self.tab_widget_abas.setTabVisible(const.GRID, False)
            self.tab_widget_abas.setCurrentIndex(const.TREEMAP)
        else:
            self.tab_widget_abas.setTabVisible(const.TREEMAP, False)
            self.tab_widget_abas.setTabVisible(const.GRID, True)
            self.tab_widget_abas.setCurrentIndex(const.GRID)

    def create_grid_image(self, rows, cols, width, height):
        '''Create a grid image with the specified number of rows and columns.
        ### Args:
        rows (int): number of rows
        cols (int): number of columns
        width (int): width of the image
        height (int): height of the image
        '''
        print(f'rows: {rows}, cols: {cols}, width: {width}, height: {height}')
        
        # Ajuste a largura e a altura para garantir divisão exata
        adjusted_width = (width // cols) * cols
        adjusted_height = (height // rows) * rows
        
        img = Image.new('RGB', (adjusted_width, adjusted_height), color='white')
        print(f'img.size: {img.size}')
        draw = ImageDraw.Draw(img)

        distance_h = adjusted_height//rows
        distance_w = adjusted_width//cols

        for y in range(rows):
            for x in range(cols):
                draw.rectangle((distance_w*x, distance_h*y, distance_w*(x+1), distance_h*(y+1)), fill= 'white' , outline='black')
                # draw.text((distance_w*x, distance_h*y), f'({x}, {y})', fill='black')

        q_image = QImage(img.tobytes(), img.width, img.height, QImage.Format.Format_RGB888)
        pixmap = QPixmap.fromImage(q_image)

        self.label_visualization_area.setPixmap(pixmap)

    def choose_attr_to_grid(self):
        '''
        This method get the selected attribute from the attribute list and add it to the selected attributes list.
        '''
        selected_attribute = self.list_widget_attribute_grid.currentItem()#get the selected attribute
        if selected_attribute:#if there is a selected attribute
            self.list_widget_selected_attr.addItem(selected_attribute.text()) #add the selected attribute to the selected attributes list
            self.list_widget_attribute_grid.takeItem(self.list_widget_attribute_grid.row(selected_attribute))#remove the selected attribute from the attribute list
   
    def remove_attr_from_grid(self):
        selected_attribute = self.list_widget_selected_attr.currentItem()
        if selected_attribute:
            self.list_widget_attribute_grid.addItem(selected_attribute.text())
            self.list_widget_selected_attr.takeItem(self.list_widget_selected_attr.row(selected_attribute)) 
            self.list_widget_attribute_grid.sortItems()       

    def choose_attr_to_treemap_hierarchy(self):
        selected_attribute = self.list_widget_attribute_treemap.currentItem()
        if selected_attribute:
            self.list_widget_hierarchy_treemap.addItem(selected_attribute.text())
            self.list_widget_attribute_treemap.takeItem(self.list_widget_attribute_treemap.row(selected_attribute))

    def remove_attr_from_treemap_hierarchy(self):
        selected_attribute = self.list_widget_hierarchy_treemap.currentItem()
        if selected_attribute:
            self.list_widget_attribute_treemap.addItem(selected_attribute.text())
            self.list_widget_hierarchy_treemap.takeItem(self.list_widget_hierarchy_treemap.row(selected_attribute))
            self.list_widget_attribute_treemap.sortItems()

    def createSquarePixmap(self, drawable_area: QSize, color):
        pixmap = QPixmap(drawable_area)
        pixmap.fill(Qt.GlobalColor.transparent)#torna o fundo transparente da imagem

        painter = QPainter(pixmap)#Esta classe fornece métodos para desenhar em um pixmap
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)# RenderHint.Antialiasing: renderiza o pixmap com antialiasing

        brush = QBrush(color)#QBrush: define a cor e o estilo de preenchimento de formas desenhadas
        painter.setBrush(brush)# atribuindo a cor e o estilo de preenchimento de formas desenhadas ao painter

        pen = painter.pen() # QPen: define a cor, largura e estilo da linha usada para desenhar formas
        pen.setWidth(2) #definindo a largura da linha da forma
        painter.setPen(pen) # atribuindo a largura da linha ao painter

        squareSize = min(drawable_area.width(), drawable_area.height())# retorna o menor valor entre a largura e a altura
        squareRect = QRect(2, 2, int(squareSize/2), int(squareSize/2)) # cria um retangulo com o tamanho da menor dimensão
        # squareRect.moveCenter(pixmap.rect().center())# move o retangulo para o centro do pixmap

        painter.drawRect(squareRect)# desenha o retangulo no pixmap
        painter.end()# finaliza o painter

        return pixmap

    # def load_treemap(self):
        # self.progressBar.setValue(0)
        # self.progressBar.show()
        # self.treemap = Treemap()
        # self.treemap.build()
        # # self.treemap.load_data(self.selected_file)
        # # self.treemap.calculate()
        # self.treemap.draw()
        # self.progressBar.hide()

    def on_resize(self, a0: QResizeEvent):
        size = a0.size()
        left = int(size.width() * 0.79)
        right = int(size.width() * 0.21)
        self.splitter_esq_dir.setGeometry(0, 0, size.width(), size.height())
        self.splitter_esq_dir.setSizes([left, right])
        self.label_visualization_area.setGeometry(self.splitter_esq_dir.geometry())
        super().resizeEvent(a0)

    def load_icon_buttons(self, button, path: str):
        img = QPixmap(path).scaled(button.width(), button.height(), Qt.AspectRatioMode.KeepAspectRatio)
        button.setIcon(QIcon(img))

    def load_icons_on_gui(self):
        self.push_button_cima_treemap.setIcon(self.style().standardIcon(QtWidgets.QStyle.StandardPixmap.SP_ArrowUp))
        self.push_button_baixo_treemap.setIcon(self.style().standardIcon(QtWidgets.QStyle.StandardPixmap.SP_ArrowDown))
        self.push_button_cima_grid.setIcon(self.style().standardIcon(QtWidgets.QStyle.StandardPixmap.SP_ArrowUp))
        self.push_button_baixo_grid.setIcon(self.style().standardIcon(QtWidgets.QStyle.StandardPixmap.SP_ArrowDown))
        self.push_button_esquerda_treemap.setIcon(self.style().standardIcon(QtWidgets.QStyle.StandardPixmap.SP_ArrowLeft))
        self.push_button_esquerda_grid.setIcon(self.style().standardIcon(QtWidgets.QStyle.StandardPixmap.SP_ArrowLeft))
        self.push_button_direita_treemap.setIcon(self.style().standardIcon(QtWidgets.QStyle.StandardPixmap.SP_ArrowRight))
        self.push_button_direita_grid.setIcon(self.style().standardIcon(QtWidgets.QStyle.StandardPixmap.SP_ArrowRight))
        self.push_button_dir_cat.setIcon(self.style().standardIcon(QtWidgets.QStyle.StandardPixmap.SP_ArrowRight))
        self.push_button_esq_cat.setIcon(self.style().standardIcon(QtWidgets.QStyle.StandardPixmap.SP_ArrowLeft))
        self.push_button_baixo_cat.setIcon(self.style().standardIcon(QtWidgets.QStyle.StandardPixmap.SP_ArrowDown))
        self.push_button_cima_cat.setIcon(self.style().standardIcon(QtWidgets.QStyle.StandardPixmap.SP_ArrowUp))
        self.setWindowIcon(QIcon(QPixmap(r'img\treemap_glyph_logo.png').scaled(32, 32)))
        
        self.action_open_file.setIcon(self.style().standardIcon(QtWidgets.QStyle.StandardPixmap.SP_DirOpenIcon))
    
    def on_open_file(self):        
        dialog = QFileDialog()
        if self.controller != None:
            # The user-selected file will be passed automatically to the method handle_file_selection
            dialog.fileSelected.connect(self.controller.handle_file_selection)
        dialog.exec()

    def load_attributes_on_gui(self):
        '''Load the attributes from the selected file in the list widgets'''
        if self.data_loader_model != None:
            attributes = self.data_loader_model.get_columns()
            # grid widgets
            self.load_lists_widgets_attribute_grid()
            # Treemap widgets
            self.load_lists_widgets_atttribute_treemap()
            self.load_combobox_label_treemap(attributes)
            self.load_combobox_size_treemap(sorted(self.data_loader_model.numerical_columns))
    
    def load_lists_widgets_attribute_grid(self):
        if not self.data_loader_model.is_empty_columns():
            self.load_lists_widgets_grid(sorted(self.data_loader_model.categorical_columns))
    
    def load_lists_widgets_atttribute_treemap(self):                
        self.load_lists_widgets_treemap(sorted(self.data_loader_model.categorical_columns))

    def load_lists_widgets_grid(self, collumns: list):
        self.list_widget_attribute_grid.clear()
        self.list_widget_attribute_grid.addItems(collumns)
        # self.list_widget_attribute_grid.removeItemWidget(self.list_widget_attribute_grid.count() - 1)

    def load_lists_widgets_treemap(self, collumns: list):
        self.list_widget_attribute_treemap.clear()
        self.list_widget_attribute_treemap.addItems(collumns)

    def load_combobox_label_treemap(self, collumns: list):
        self.combo_box_label_treemap.clear()
        self.combo_box_label_treemap.addItem('---')
        self.combo_box_label_treemap.addItems(collumns)
        self.combo_box_label_treemap.removeItem(self.combo_box_label_treemap.count() - 1)

    def load_combobox_size_treemap(self,collumns):
        self.combo_box_size_treemap.clear()
        self.combo_box_size_treemap.addItem('---')
        self.combo_box_size_treemap.addItems(collumns)
        # self.combo_box_size_treemap.removeItem(self.combo_box_size_treemap.count() - 1)


    ########## NOTIFICATION METHODS ##########
    def update_file_selection(self, file_path):
        '''Update the selected file and notify the model
        ### Args:
        file_path (str): the path of the selected file
        '''
        if file_path not in ('', None):
            self.selected_file = file_path
            self.data_loader_model.load_file(file_path)
            # self.file_model.notify_file_selected(file_path)

    def update_closing(self):
        '''Notify the model that the window is closing'''
        self.data_loader_model.notify_closing()


    @property
    def selected_file(self):
        return self.__selected_file
    
    @selected_file.setter
    def selected_file(self, selected_file):
        self.__selected_file = selected_file

       
    
