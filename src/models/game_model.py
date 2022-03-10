import random
import numpy as np
from src.models import TileState, GameTile

class GameModel:
    def __init__(self, rows: int, columns: int, bombs: int):
        self.rows = rows
        self.columns = columns
        self.bombs = bombs

        if bombs > rows * columns:
            raise ValueError('There can\'t be more mines than tiles!')

        self.tiles = np.array([[GameTile(row, column, TileState.NOT_CHECKED) for column
                                in range(self.columns)] for row in range(self.rows)])

        available_tiles = self.tiles.flatten().tolist()

        # Etsitään satunnaiset paikat pommeille.
        # Pop metodi poistaa ruudun available_tiles listasta,
        # joten samaa ruutua ei voida valita monta kertaa.
        for _ in range(bombs):
            idx = random.randrange(len(available_tiles))
            tile = available_tiles.pop(idx)
            tile.bomb = True

    def open(self, tile: GameTile) -> list[GameTile]:
        """Avaa ruudun jos se ei ole pommi.
        Myös viereiset ruudut avataan tulvatäyttöalgoritmilla jos niissä ei ole pommeja."""
        if tile.bomb:
            return False

        tiles = []
        tiles.append(tile)

        while tiles:
            tile = tiles.pop(0)
            neighbour_tiles = self.get_neighbour_tiles(tile)
            bombs_count = sum(t.bomb for t in neighbour_tiles)
            tile.state = TileState(bombs_count)

            if tile.state == TileState.EMPTY:
                for tile2 in neighbour_tiles:
                    if tile2.state == TileState.NOT_CHECKED and not tile2.bomb:
                        if tile2 not in tiles:
                            tiles.append(tile2)

        return True

    def reveal_all_bombs(self) -> list[GameTile]:
        bombs = []
        for tile in self.tiles.flatten():
            if tile.bomb:
                tile.state = TileState.BOMB
                bombs.append(tile)
        return bombs

    def get_neighbour_tiles(self, tile: GameTile) -> list[GameTile]:
        tiles = []
        for row in range(tile.row - 1, tile.row + 2):
            for column in range(tile.column - 1, tile.column + 2):
                if self.is_valid_tile(row, column) and self.tiles[row][column] != tile:
                    tiles.append(self.tiles[row][column])
        return tiles

    def has_player_won(self) -> bool:
        for tile in self.tiles.flatten():
            if tile.state is TileState.NOT_CHECKED:
                return False
            if tile.state is TileState.FLAG and not tile.bomb:
                return False
        return True

    def is_valid_tile(self, row: int, column: int) -> bool:
        return 0 <= row < self.rows and 0 <= column < self.columns
