from PyQt5 import QtWidgets

class MessageBox(QtWidgets.QMessageBox):
    def error(self, title: str, message: str):
        self._show_messagebox(title, message, self.Warning)

    def information(self, title: str, message: str):
        self._show_messagebox(title, message, self.Information)

    def _show_messagebox(self, title: str, message: str, icon: QtWidgets.QMessageBox.Icon):
        self.setIcon(icon)
        self.setText(message)
        self.setWindowTitle(title)
        self.setStandardButtons(self.Ok)
        self.exec_()
