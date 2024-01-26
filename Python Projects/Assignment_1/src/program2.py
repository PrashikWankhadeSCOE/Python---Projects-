

'''
2. Design a PyQt window with a QPushButton. Upon clicking the button, change the text of
a QLabel to "Button Clicked!"
'''

import sys
from PyQt5.QtWidgets import QWidget,QApplication,QVBoxLayout,QLabel,QPushButton
from PyQt5.QtCore import Qt

class MainWindow(QWidget):
    def __init__(self ):
        super().__init__()

        self.setWindowTitle('Main Window')
        self.setGeometry(500,300,500,300)

        self.mainLayout = QVBoxLayout(self)
        self.setLayout(self.mainLayout)
    
        self.label = QLabel("Hello Core2web")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label.setFixedSize(500,100)
        self.mainLayout.addWidget(self.label)

        self.addButton()

    def addButton(self):
        self.Button1 = QPushButton("Text Change !")

        self.Button1.setFixedSize(100,30)
        self.Button1.clicked.connect(lambda: self.label.setText('Hello Core2web' if self.label.text()=='I am here'else "I am here"))
        self.mainLayout.addWidget(self.Button1,alignment=Qt.AlignmentFlag.AlignCenter)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_Window = MainWindow()
    main_Window.show()
    sys.exit(app.exec_())