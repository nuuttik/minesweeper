from PyQt5 import QtCore
from src.models import TileState

class GameTile(QtCore.QObject):
    state_changed = QtCore.pyqtSignal()

    def __init__(self, row: int, column: int, state: TileState):
        super().__init__()
        self.row = row
        self.column = column
        self.state = state
        self.bomb = False

    def __setattr__(self, name, value):
        """Jos tila muuttuu niin annetaan siitä signaali,
        että PictureButton luokassa voimme vaihtaa napin kuvan vastaamaan uutta tilaa."""
        super().__setattr__(name, value)
        if name == 'state':
            self.state_changed.emit()
