from PyQt5 import QtWidgets, QtGui
from src.widgets import GameWindow, SettingsWindow, MessageBox, StatisticsWindow
from src import StatisticsHandler

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, app: QtWidgets.QApplication):
        super().__init__()
        self.app = app

        self.setWindowTitle('Minesweeper')

        self.settings = SettingsWindow(self)
        self.msg = MessageBox(self)
        self.stats = StatisticsHandler('stats.data')

        # Asetetaan jonkinlaiset järkevät rajat ruutujen määrälle
        # Ohjelma tukee toki suurempaakin määrää, mutta ikkunan koko on yleensä silloin liian suuri
        self.max_rows = 30
        self.max_columns = 50
        self.in_main_menu = True

        self.main_menu()

    def main_menu(self):
        self.in_main_menu = True

        layout = QtWidgets.QVBoxLayout()

        buttons = {
            'New Game': self.new_game,
            'Statistics': self.statistics,
            'Exit program': self.app.quit
        }

        for title, action in buttons.items():
            button = QtWidgets.QPushButton(title)
            button.clicked.connect(action)
            layout.addWidget(button)

        main_widget = QtWidgets.QWidget()
        self.setCentralWidget(main_widget)
        main_widget.setLayout(layout)
        main_widget.setMinimumSize(250, 200)
        self.adjustSize()

    def new_game(self):
        try:
            settings = self.settings.get_settings()
        except RuntimeError as err:
            self.msg.error('Error', str(err))
            return
        if not settings:
            return

        if not self.is_valid_settings(settings):
            self.msg.error('Error',
            f"There can be at most {self.max_rows} rows and {self.max_columns} columns")
            return

        try:
            game_window = GameWindow(self,
            settings['rows'], settings['columns'], settings['bombs'], self.stats)
        except ValueError as err:
            self.msg.error('Error', str(err))
            return

        self.in_main_menu = False
        self.setCentralWidget(game_window)
        self.adjustSize()

    def is_valid_settings(self, settings):
        return settings['rows'] <= self.max_rows and settings['columns'] <= self.max_columns

    def statistics(self):
        data = self.stats.read()
        if not data:
            self.msg.error('Error', 'You haven\'t played any games')
            return
        stats_window = StatisticsWindow(self, data)
        self.in_main_menu = False
        self.setCentralWidget(stats_window)
        self.adjustSize()

    def closeEvent(self, event: QtGui.QCloseEvent):
        if not self.in_main_menu:
            self.main_menu()
            event.ignore()
        else:
            event.accept()
