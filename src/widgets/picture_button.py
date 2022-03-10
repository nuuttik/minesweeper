from PyQt5 import QtWidgets, QtGui, QtCore
from src.models import GameTile

class PictureButton(QtWidgets.QLabel):
    clicked = QtCore.pyqtSignal(object, object)

    def __init__(self, tile: GameTile, parent: QtWidgets.QWidget):
        super().__init__(parent)
        self.tile = tile
        # state_changed on GameTile luokan signaali, jota käytetään kuvan päivittämiseen
        # kun GameTilen state attribuutti vaihtuu
        self.tile.state_changed.connect(self.update)
        self.update()

    def update(self):
        pixmap = QtGui.QPixmap(self.tile.state.get_picture_path())
        self.setPixmap(pixmap)
        self.resize(pixmap.width(), pixmap.height())

    def mouseReleaseEvent(self, event: QtGui.QMouseEvent):
        self.clicked.emit(event, self)
