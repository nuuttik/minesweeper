from typing import Union
from PyQt5 import QtWidgets, QtCore

class SettingsWindow(QtWidgets.QDialog):
    def __init__(self, parent: QtWidgets.QWidget):
        super().__init__(parent, QtCore.Qt.Window | QtCore.Qt.WindowCloseButtonHint)

        self.setWindowTitle('Settings')

        self.grid = QtWidgets.QGridLayout()
        self.setLayout(self.grid)

        self.create_gridlayout()

    def create_gridlayout(self):
        self.widgets = [
            {
                'type': 'lineedit',
                'label': QtWidgets.QLabel('Rows'),
                'box': QtWidgets.QLineEdit(),
                'pos': (0, 0)
            },
            {
                'type': 'lineedit',
                'label': QtWidgets.QLabel('Columns'),
                'box': QtWidgets.QLineEdit(),
                'pos': (0, 1)
            },
            {
                'type': 'lineedit',
                'label': QtWidgets.QLabel('Mines'),
                'box': QtWidgets.QLineEdit(),
                'pos': (1, 0)
            },
            {
                'type': 'button',
                'btn': QtWidgets.QPushButton('Start the game'),
                'pos': (2, 0),
                'action': self.accept
            },
            {
                'type': 'button',
                'btn': QtWidgets.QPushButton('Cancel'),
                'pos': (2, 1),
                'action': self.reject
            }
        ]

        for widget in self.widgets:
            sublayout = QtWidgets.QVBoxLayout()

            if widget['type'] == 'lineedit':
                sublayout.addWidget(widget['label'], alignment=QtCore.Qt.AlignCenter)
                sublayout.addWidget(widget['box'], alignment=QtCore.Qt.AlignCenter)

            elif widget['type'] == 'button':
                widget['btn'].clicked.connect(widget['action'])
                sublayout.addWidget(widget['btn'], alignment=QtCore.Qt.AlignCenter)

            self.grid.addLayout(sublayout, *widget['pos'])

    def get_selected(self) -> dict[str, int]:
        try:
            rows = int(self.widgets[0]['box'].text())
            columns = int(self.widgets[1]['box'].text())
            bombs = int(self.widgets[2]['box'].text())
        except ValueError as err:
            raise RuntimeError('Rows, columns and mines must be numbers.') from err

        if rows <= 0 or columns <= 0 or bombs <= 0:
            raise RuntimeError('The amount of rows, columns and mines must be '
                                'greater than zero.')

        return {
            'rows': rows,
            'columns': columns,
            'bombs': bombs
        }

    def clear_lineedits(self):
        for widget in self.widgets:
            if widget['type'] == 'lineedit':
                widget['box'].clear()

    def get_settings(self) -> Union[dict[str, int], bool]:
        self.clear_lineedits()
        if self.exec_():
            return self.get_selected()
        return False
