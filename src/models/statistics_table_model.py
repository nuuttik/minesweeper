from PyQt5 import QtCore
from src.models import StatisticsModel

class StatisticsTableModel(QtCore.QAbstractTableModel):
    def __init__(self, data: list[StatisticsModel]):
        super().__init__()
        self._data = data
        self.labels = ['Date', 'Duration (s)', 'Turns', 'Outcome',
                        'Rows', 'Columns', 'Mines']

    def data(self, index, role):
        if role == QtCore.Qt.DisplayRole:
            column = index.column()
            item = self._data[index.row()][column]
            if column == 0:
                return item.strftime('%d.%m.%Y %H:%M:%S')
            if column == 1:
                return f"{item:.2f}"
            if column == 3:
                return 'Win' if item else 'Loss'
            return item
        return QtCore.QVariant()

    def rowCount(self, index):
        return len(self._data)

    def columnCount(self, index):
        return len(self._data[0].__dict__)

    def headerData(self, section, orientation, role):
        """Asetetaan sarakkeille otsikot."""
        if orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return self.labels[section]
        return super().headerData(section, orientation, role)
