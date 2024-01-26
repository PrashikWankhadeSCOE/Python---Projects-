'''
Build a PyQt application with a QRadioButton group for selecting a programming
language (e.g., Python, Java, C++). Display a message indicating the selected language
when a radio button is clicked.
'''

import sys
from PyQt5.QtWidgets import QApplication,QWidget,QVBoxLayout,QRadioButton,QLabel


class RadioButtonApp(QWidget):
    def __init__(self):
        super().__init__()

        self.radioUi()

    def radioUi(self):
        self.setWindowTitle('Radio Button App')
        self.setGeometry(300,300,400,200)

        layout = QVBoxLayout()
        self.option1_radio = QRadioButton('Python',self)
        self.option2_radio = QRadioButton('Java',self)
        self.option3_radio = QRadioButton('C++',self)

        layout.addWidget(self.option1_radio)
        layout.addWidget(self.option2_radio)
        layout.addWidget(self.option3_radio)

        self.selected_option_lable = QLabel('Selected Option : None ',self)
        layout.addWidget(self.selected_option_lable)

        self.option1_radio.toggled.connect(lambda : self.update_slected_option('Pyhton'))
        self.option2_radio.toggled.connect(lambda : self.update_slected_option('Java'))
        self.option3_radio.toggled.connect(lambda : self.update_slected_option('C++'))
        self.setStyleSheet(f"background-color:Pink;")

        self.setLayout(layout)

    def update_slected_option(self,option):
        if option:
            self.selected_option_lable.setText(f"Selected Option:{option}")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = RadioButtonApp()
    window.show()
    sys.exit(app.exec_()) 