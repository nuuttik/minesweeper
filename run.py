from PyQt5.QtWidgets import QApplication
from src import MainWindow

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow(app)
    window.show()
    app.exec_()
