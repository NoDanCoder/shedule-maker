from __future__ import annotations


class Time:

    def __init__(self, day: Day, start: float, end: float):
        self.day = day
        self.start = start * 2
        self.end = end * 2

    @property
    def start(self):
        return self._start / 2

    @start.setter
    def start(self, value: float):
        self._start = value * 2

    @property
    def end(self):
        return self._end / 2

    @end.setter
    def end(self, value: float):
        self._end = value * 2

    @property
    def distance(self):
        return abs(self._start - self._end)

    @staticmethod
    def are_in_conflict(time_a: Time, time_b: Time):
        return abs(time_a.start - time_b.start) + abs(time_a.end - time_b.end) <= time_a.distance + time_b.distance
