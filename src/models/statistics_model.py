from dataclasses import dataclass
from datetime import datetime

@dataclass
class StatisticsModel:
    timestamp: datetime
    duration: float
    actions: int
    win: bool
    rows: int
    columns: int
    bombs: int

    def __getitem__(self, key: int):
        return list(self.__dict__.values())[key]
