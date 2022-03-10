from enum import Enum
import pkg_resources

class TileState(Enum):
    def __new__(cls, value: int, picture: str):
        """https://docs.python.org/3/library/enum.html#using-a-custom-new
        __new__ pitää määritellä että constructorilla voi olla picture parametri,
        joka ei kuitenkaan ole osa enumin arvoa.
        Esimerkiksi TileState(0) kutsulla saadaan TileState.EMPTY jonka picture
        attribuutilla on arvo 'ruutu_tyhja.png'."""
        obj = object.__new__(cls)
        obj._value_ = value
        obj.picture = picture
        return obj

    EMPTY = (0, 'ruutu_tyhja.png')
    CHECKED_1 = (1, 'ruutu_1.png')
    CHECKED_2 = (2, 'ruutu_2.png')
    CHECKED_3 = (3, 'ruutu_3.png')
    CHECKED_4 = (4, 'ruutu_4.png')
    CHECKED_5 = (5, 'ruutu_5.png')
    CHECKED_6 = (6, 'ruutu_6.png')
    CHECKED_7 = (7, 'ruutu_7.png')
    CHECKED_8 = (8, 'ruutu_8.png')
    NOT_CHECKED = (9, 'ruutu_selka.png')
    BOMB = (10, 'ruutu_miina.png')
    FLAG = (11, 'ruutu_lippu.png')

    def get_picture_path(self) -> str:
        """Palauttaa absoluuttisen polun ruudun tilaa vastaavaan kuvaan."""
        return pkg_resources.resource_filename('resources.images', self.picture)
