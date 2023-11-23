import random
import sys

from UI import Ui_MainWindow
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow


class YellowCircle(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.click = False
        self.pushButton.clicked.connect(self.draw)

    def draw(self):
        self.click = True
        self.repaint()

    def paintEvent(self, event):
        if self.click:
            d = random.randint(1, min(self.width(), self.height()) - 1)
            qp = QPainter()
            qp.begin(self)
            qp.setBrush(
                QColor(
                    random.randint(0, 255),
                    random.randint(0, 255),
                    random.randint(0, 255),
                )
            )
            qp.drawEllipse(
                (self.width() - d) // 2, (self.height() - d) // 2, d, d
            )
            self.click = False
            qp.end()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = YellowCircle()
    window.show()
    sys.exit(app.exec())
