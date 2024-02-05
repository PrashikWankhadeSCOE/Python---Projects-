'''
Create a PyQt window with a progress bar. Implement a function that simulates a task
(e.g., file download) and updates the progress bar accordingly.
'''

import sys
from PyQt5.QtWidgets import *
import urllib.request

class ProgressBar(QWidget):
    def __init__(self):
        super().__init__()

        self.init_UI()

    def init_UI(self):
        self.progressBar = QProgressBar(self)

        self.progressBar.setGeometry(25,45,210,30)

        self.button = QPushButton('Start',self)

        self.button.move(50,100)

        self.button.clicked.connect(self.Download)

        self.setGeometry(310,310,400,200)

        self.setWindowTitle('ProgressBar')

    def Handle_Progress(self,blocknum,blocksize,totalsize):
        readed_data = blocknum*blocksize

        if totalsize>0:
            download_percentage = readed_data*100/totalsize
            self.progressBar.setValue(int(download_percentage))
            QApplication.processEvents()

    def Download(self):
        down_url = 'https://img.indiaforums.com/person/640x480/1/2525-prabhas.jpg?c=4bM0D6'
        save_loc = "C:/Users/User-pc/Downloads/prabhas.jpg"
        urllib.request.urlretrieve(down_url,save_loc,self.Handle_Progress)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ProgressBar()
    window.show()
    sys.exit(app.exec_())