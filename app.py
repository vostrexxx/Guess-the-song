from PyQt6.QtWidgets import QApplication, QWidget

import sys  # for access to arguments Command Line

# transfer sys.argv to args,to access args of CL to app
app = QApplication([])

# creating a widget; Qt - window
window = QWidget()
window.show()

# starting event to no close
app.exec()
