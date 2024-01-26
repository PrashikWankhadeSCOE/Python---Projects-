'''
Design a PyQt window that includes a QSlider and a QLabel. Update the label text
dynamically to reflect the current value of the slider.
'''

import sys
from PyQt5.QtWidgets import QApplication,QWidget,QVBoxLayout,QSlider,QLabel
from PyQt5.QtCore import Qt

class SlideBar(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Slider App')
        self.setGeometry(100,100,400,200)

        layout = QVBoxLayout()

        self.slider = QSlider(Qt.Horizontal,self)
        layout.addWidget(self.slider)

        self.label = QLabel('Slider Value : 0',self)
        layout.addWidget(self.label)

        self.slider.valueChanged.connect(self.update_label)

        self.setLayout(layout)

    def update_label(self):
        value = self.slider.value()
        self.label.setText(f"Slider VAlue : {value}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SlideBar()
    window.show()
    sys.exit(app.exec_())