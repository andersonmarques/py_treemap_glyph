
from view.main_screen import Ui_MainWindow
from observer.file_selection_observable import File_Selection_Observable
# from controller.business.treemap import Treemap

from PyQt6.QtCore import Qt, QRect, QSize
from PyQt6.QtGui import QResizeEvent,QPixmap, QIcon, QImage
from PyQt6.QtWidgets import QMainWindow, QProgressBar, QFileDialog, QVBoxLayout
from PyQt6.QtGui import QPainter, QBrush, QColor

from PIL import Image, ImageDraw

import pandas as pd

class Main (QMainWindow, Ui_MainWindow, File_Selection_Observable):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.resizeEvent = self.on_resize #override the method resizeEvent to resize the splitter
        self.showMaximized()       
        
        # layout.addWidget(self.label_visualization_area)
        ########## Hide the treemap tab ##########
        #tab 0: treemap
        #tab 1: grid
        #tab 3: categorical glyphs
        #tab 4: continuous glyphs
        #tab 5: details
        #tab 6: filters
        self.tab_widget_abas.setTabVisible(0, False)

        # self.progressBar = QProgressBar()
        # self.progressBar.setMaximum(100)
        # self.progressBar.setValue(0)
        # self.statusBar().addWidget(self.progressBar)
        self.statusbar.hide()
        self.load_icons()
        self.actionOpen_file.triggered.connect(self.on_open_file)
        self.selected_file = None
        File_Selection_Observable.__init__(self)
        # self.label_visualization_area.setPixmap(
        #     self.createSquarePixmap(
        #         self.label_visualization_area.size(), 
        #         QColor(105, 0, 50)
        #     )
        # )
        ####### Actions of the buttons ########
        self.push_button_view_grid.clicked.connect(lambda : self.create_grid_image(10, 10, 
                                                                                   self.label_visualization_area.height(),
                                                                                   self.label_visualization_area.height()))

        ####### Actions of the QActions (Menu Itens) ########
        self.action_treemap.triggered.connect(lambda: self.show_treemap_or_grid_tab(0))
        self.action_grid.triggered.connect(lambda: self.show_treemap_or_grid_tab(1))

        # layout = QVBoxLayout(self.label_visualization_area)

    def show_treemap_or_grid_tab(self, index_to_show):
        '''
        This method shows the treemap tab or the grid tab.
        :param index_to_show: use 0 to show the treemap tab and 1 to show the grid tab
        '''
        if index_to_show == 0:
            self.tab_widget_abas.setTabVisible(0, True)
            self.tab_widget_abas.setTabVisible(1, False)
            self.tab_widget_abas.setCurrentIndex(0)
        else:
            self.tab_widget_abas.setTabVisible(0, False)
            self.tab_widget_abas.setTabVisible(1, True)
            self.tab_widget_abas.setCurrentIndex(1)

    def create_grid_image(self, rows, cols, width, height):
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
        left = int(size.width() * 0.75)
        right = int(size.width() * 0.25)
        self.splitter_esq_dir.setGeometry(0, 0, size.width(), size.height())
        self.splitter_esq_dir.setSizes([left, right])
        self.label_visualization_area.setGeometry(self.splitter_esq_dir.geometry())
        super().resizeEvent(a0)

    def load_icons(self):
        img_up = QPixmap(r'img/setaUp.png').scaled(self.push_button_cima_treemap.width(),
                                 self.push_button_cima_treemap.height(),
                                    Qt.AspectRatioMode.KeepAspectRatio)
        self.push_button_cima_treemap.setIcon(QIcon(img_up))
        img_down = QPixmap(r'img/setaDown.png').scaled(self.push_button_baixo_treemap.width(),
                                    self.push_button_baixo_treemap.height(),
                                    Qt.AspectRatioMode.KeepAspectRatio)
        self.push_button_baixo_treemap.setIcon(QIcon(img_down))
        img_left = QPixmap(r'img/setaEsq.png').scaled(self.push_button_esquerda_treemap.width(),
                                    self.push_button_esquerda_treemap.height(),
                                    Qt.AspectRatioMode.KeepAspectRatio)
        self.push_button_esquerda_treemap.setIcon(QIcon(img_left))
        img_right = QPixmap(r'img/setaDir.png').scaled(self.push_button_direita_treemap.width(),
                                    self.push_button_direita_treemap.height(),
                                    Qt.AspectRatioMode.KeepAspectRatio)
        self.push_button_direita_treemap.setIcon(QIcon(img_right))
        self.setWindowIcon(QIcon(QPixmap(r'img\treemap_glyph_logo.png').scaled(32, 32)))

        icon = QIcon()
        icon.addPixmap(QPixmap(r"\img\folder.png"), QIcon.Mode.Normal, QIcon.State.Off)
        self.actionOpen_file.setIcon(icon)
    
    def on_open_file(self):        
        dialog = QFileDialog()
        dialog.fileSelected.connect(self.handle_file_selection)
        dialog.exec()

    def handle_file_selection(self, file_path):
        print(f'File selected: {file_path}')
        self.selected_file = file_path
        self.notify_file_selected(file_path)

    def closeEvent(self, event):
        self.notify_closing()


    @property
    def selected_file(self):
        return self.__selected_file
    
    @selected_file.setter
    def selected_file(self, selected_file):
        self.__selected_file = selected_file

       
    
