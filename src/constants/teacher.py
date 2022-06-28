from enum import Enum

from src.constants.score import Score


class Teacher(Enum):
    CARMEN_SALAS = ("CARMEN AMALIA SALAS BROWN", Score.GOOD)
    NORMA_SARMIENTO = ("NORMA CONSTANZA SARMIENTO BENAVIDES", Score.GOOD)
    GERMAN_OBANDO = ("GERMAN DARIO OBANDO BRAVO", Score.EXCELLENT)
    CARLOS_ALVAREZ = ("CARLOS EDUARDO ALVAREZ CABRERA", Score.EXCELLENT)
    PEDRO_WIGHTMAN = ("PEDRO MARIO WIGHTMAN ROJAS", Score.REGULAR)
    DANIEL_BOJACA = ("DANIEL ALFONSO BOJACA TORRES", Score.EXCELLENT)
    GLORIA_GALLO = ("GLORIA AYDEE GALLO CUBILLOS", Score.REGULAR)
    ADRYAN_PINEDA = ("ADRYAN FABRIZIO PINEDA REPIZZO", Score.EXCELLENT)
    TIRSO_BUENO = ("TIRSO HERNAN BUENO CASTANEDA", Score.REGULAR)
    JESSICA_MURILLO = ("JESSICA MURILLO MENA", Score.EXCELLENT)
    HAROLD_VILLAMIL = ("HAROLD ALEXANDER VILLAMIL CASTILLO", Score.REGULAR)
    MARIA_LOPEZ = ("MARIA PAULA LOPEZ VELASQUEZ", Score.REGULAR)
    JHONATAN_DIAZ = ("JHONATAN JULIAN DIAZ TIMOTE", Score.REGULAR)
    MARIA_BATISTA = ("MARIA FERNANDA BATISTA MORALES", Score.EXCELLENT)

    MONITOR = ("MONITOR", Score.UNKNOWN)
    UNKNOWN = ("N/N", Score.UNKNOWN)

    def __init__(self, user_name: str, score: Score):
        self.user_name = user_name
        self.score = score
