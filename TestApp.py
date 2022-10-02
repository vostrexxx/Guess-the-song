import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

    widget = QLabel("1")  # Создана метка с текстом 1.
    widget.setText("2")  # Создана метка с текстом 2.

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
