'''
Implement a PyQt dialog box that prompts users to enter their names using a QLineEdit.
Upon clicking "OK," display a QMessageBox with a personalized greeting.
'''

import sys
from PyQt5.QtWidgets import QApplication,QWidget, QLineEdit,QMessageBox,QPushButton,QVBoxLayout,QLabel
from  PyQt5.QtCore import Qt

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Input Output')
        self.setGeometry(500,300,500,300)
    

        self.mainLayout = QVBoxLayout(self)
        self.setLayout(self.mainLayout)
        
        self.user_input = QLineEdit("Enter the data")
        self.user_input.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.user_input.setFixedSize(300,50)
        self.mainLayout.addWidget(self.user_input,Qt.AlignmentFlag.AlignHCenter)

        self.addbutton()

    def addbutton(self):
        self.button = QPushButton('Get output !')
        self.button.setFixedSize(100,30)
        self.button.clicked.connect(self.__show_message)
        self.mainLayout.addWidget(self.button,alignment = Qt.AlignmentFlag.AlignCenter)

    def __show_message(self):
        input = self.user_input.text()
        QMessageBox.information(self,'input from user is',input)
        self.close()

if __name__ =='__main__':
    app = QApplication(sys.argv)
    main_Window = MainWindow()
    main_Window.show()
    sys.exit(app.exec_())