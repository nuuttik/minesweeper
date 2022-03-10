from datetime import datetime
from PyQt5 import QtWidgets, QtCore, QtGui
import numpy as np
from src.models import GameModel, TileState, StatisticsModel
from src.widgets import PictureButton
from src import StatisticsHandler

class GameWindow(QtWidgets.QWidget):
    def __init__(self, parent: QtWidgets.QWidget, rows: int, columns: int,
                bombs: int, stats: StatisticsHandler):
        super().__init__(parent)
        self.parent = parent
        self.stats = stats
        self._game_ended = False
        self.actions = 0

        self.game = GameModel(rows, columns, bombs)

        self.grid = QtWidgets.QGridLayout()
        self.setLayout(self.grid)

        self.create_gridlayot()
        self.game_start_timestamp = datetime.now()

    def create_gridlayot(self):
        self.buttons = np.array([[PictureButton(tile, self) for tile in row]
                                for row in self.game.tiles])
        for button in self.buttons.flatten():
            button.clicked.connect(self.picture_clicked)
            self.grid.addWidget(button, button.tile.row, button.tile.column)

    def picture_clicked(self, event: QtGui.QMouseEvent, button: QtWidgets.QWidget):
        if self._game_ended:
            return

        mouse_button = event.button()
        if mouse_button == QtCore.Qt.RightButton:
            if button.tile.state is TileState.NOT_CHECKED:
                button.tile.state = TileState.FLAG
                if self.game.has_player_won():
                    self.game_ended(True)
            elif button.tile.state is TileState.FLAG:
                button.tile.state = TileState.NOT_CHECKED

        elif mouse_button == QtCore.Qt.LeftButton:
            if button.tile.state is not TileState.NOT_CHECKED:
                return
            self.actions += 1
            tiles = self.game.open(button.tile)
            if not tiles:
                self.game_ended(False)
            elif self.game.has_player_won():
                self.game_ended(True)

    def game_ended(self, win: bool):
        if not win:
            self.game.reveal_all_bombs()
        self._game_ended = True
        timestamp = datetime.now()
        duration = (timestamp - self.game_start_timestamp).total_seconds()
        stats_mdl = StatisticsModel(timestamp, duration, self.actions,
                    win, self.game.rows, self.game.columns, self.game.bombs)
        self.stats.write(stats_mdl)
        self.parent.msg.information('The game ended', 'You won the game!' if win else 'You lost the game!')
