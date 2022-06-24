from typing import List

from src.constants.teacher import Teacher
from src.services.time import Time


class Stuff:

    def __init__(self, teacher: Teacher, time_list: List[Time]):
        self.teacher = teacher
        self.time_list = time_list