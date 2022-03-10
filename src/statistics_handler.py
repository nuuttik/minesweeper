import os
import pickle
from src.models import StatisticsModel

class StatisticsHandler:
    def __init__(self, filename: str):
        self.filename = filename

    def write(self, stats: StatisticsModel):
        with open(self.filename, 'ab') as file:
            pickle.dump(stats, file)

    def read(self) -> list[StatisticsModel]:
        ret = []
        if not os.path.isfile(self.filename):
            return ret
        with open(self.filename, 'rb') as file:
            while True:
                try:
                    ret.append(pickle.load(file))
                except EOFError:
                    break
        return ret
