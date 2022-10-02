# for access to arguments Command Line
import sys
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton


# child class QMainWindow for set main window of app
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Guess the song")
        button = QPushButton("Confirm!")

        # set central widget window
        self.setCentralWidget(button)


# transfer sys.argv to args,to access args of CL to app
app = QApplication(sys.argv)

# creating a widget; Qt - window
window = MainWindow()
window.show()

# starting event to no close window
app.exec()

