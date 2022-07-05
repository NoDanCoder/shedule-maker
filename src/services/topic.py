from typing import List

from src.constants.topic_id import TopicId
from src.services.stuff import Stuff


class Topic:

    def __init__(self, topic_id: TopicId, fixed: List[Stuff], monitory: List[Stuff] = None, laboratory: List[Stuff] = None):
        self.topic_id = topic_id
        self.fixed = fixed
        self.monitory = monitory
        self.laboratory = laboratory
