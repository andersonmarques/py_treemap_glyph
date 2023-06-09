from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt6.QtGui import QPainter, QColor, QBrush, QPixmap
from PyQt6.QtCore import Qt, QRect

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Quadrado em QLabel")
        self.setGeometry(100, 100, 400, 400)

        self.label = QLabel(self)
        self.label.setGeometry(50, 50, 200, 200)
        self.label.setPixmap(self.createSquarePixmap(self.label.size(), QColor(255, 0, 0)))
        self.label.mousePressEvent = self.squareClicked # type: ignore
        self.squareColor = QColor(255, 0, 0)

    def squareClicked(self, event):
        squareRect = self.label.rect()
        if squareRect.contains(event.pos()):
            if self.squareColor == QColor(255, 0, 0):
                self.squareColor = QColor(0, 255, 0)
            else:
                self.squareColor = QColor(255, 0, 0)
            self.label.setPixmap(self.createSquarePixmap(self.label.size(), self.squareColor))


    def createSquarePixmap(self, size, color):
        pixmap = QPixmap(size)
        pixmap.fill(Qt.GlobalColor.transparent)

        painter = QPainter(pixmap)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        brush = QBrush(color)
        painter.setBrush(brush)

        pen = painter.pen()
        pen.setWidth(2)
        painter.setPen(pen)

        squareSize = min(size.width(), size.height())
        squareRect = QRect(0, 0, squareSize, squareSize)
        squareRect.moveCenter(pixmap.rect().center())

        painter.drawRect(squareRect)
        painter.end()

        return pixmap

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
