from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton
from PyQt6.QtCore import QSize, Qt
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("my app")
        
        button = QPushButton("press me")
        button.setCheckable(True)
        button.clicked.connect(self.the_button_was_clicked)
        button.clicked.connect(self.the_button_was_toggled)

        self.setFixedSize(QSize(400,300))
        self.setCentralWidget(button)

    def the_button_was_clicked(self):
        print("button was clicked")
    
    def the_button_was_toggled(self, checked):
        print("this is the status: ", checked )

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()