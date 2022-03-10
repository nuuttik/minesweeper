from PyQt5 import QtWidgets, QtCore
from src.models import StatisticsModel, StatisticsTableModel

class StatisticsWindow(QtWidgets.QTableView):
    def __init__(self, parent: QtWidgets.QWidget, data: list[StatisticsModel]):
        super().__init__(parent)
        self.model = StatisticsTableModel(data)
        self.setModel(self.model)
        self.resizeColumnsToContents()
        self.setMinimumSize(QtCore.QSize(600, 300))
