# for access to arguments Command Line
import sys
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton

from random import choice

window_titles = [
    'My App',
    'My App',
    'Still My App',
    'Still My App',
    'What on earth',
    'What on earth',
    'This is surprising',
    'This is surprising',
    'Something went wrong'
]


# child class QMainWindow for set main window of app
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.n_times_clicked = 0

        self.setWindowTitle("Guess the song")

        self.button = QPushButton("Confirm!")
        self.button.clicked.connect(self.the_button_was_clicked)

        # self.setFixedSize(QSize(400, 300))

        # signal
        self.windowTitleChanged.connect(self.the_window_title_changed)

        self.setCentralWidget(self.button)

        # self.setMinimumSize(600, 500)
        # self.setMaximumSize(1200, 1200)


    def the_button_was_clicked(self):
        print("clicked!")
        new_window_title = choice(window_titles)
        print("Setting_title: %s" % new_window_title)
        self.setWindowTitle(new_window_title)

    # slot-method
    def the_window_title_changed(self, window_title):
        print("Window title changed: %s" % window_title)

        if window_title == 'Something went wrong':
            self.button.setDisabled(True)


# transfer sys.argv to args,to access args of CL to app
app = QApplication(sys.argv)

# creating a widget; Qt - window
window = MainWindow()
window.show()

# starting event to no close window
app.exec()
