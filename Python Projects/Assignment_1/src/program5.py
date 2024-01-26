
'''
Create a PyQt window with a QComboBox containing a list of colors. Upon selecting a
color, change the background color of the window accordingly.
'''

import sys
from PyQt5.QtWidgets import QWidget,QApplication,QVBoxLayout,QComboBox
from PyQt5.QtGui import QColor

class ColorChangeApp(QWidget):
    def __init__(self):
        super().__init__()
        self.__init__ui()

    def __init__ui(self):
        layout = QVBoxLayout()

        color_combo = QComboBox(self)
        colors = ['Red','Green','Blue','Yellow','Cyan','Magenta']
        color_combo.addItems(colors)

        color_combo.currentIndexChanged.connect(self.change_color)

        layout.addWidget(color_combo)
        self.setLayout(layout)
        self.change_color(0)

        self.setGeometry(500,300,500,300)
        self.setWindowTitle('Color changer App')

    def change_color(self,index):
        color_name = self.sender().currentText() if self.sender() else 'Red'

        color = QColor(color_name)
        self.setStyleSheet(f"background-color: {color.name()};")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ColorChangeApp()
    ex.show()
    sys.exit(app.exec_())
