from src.factory.calendar import Calendar
from src.utils.strings import Strings


class ScheduleMaker:

    def __init__(self, calendar: Calendar):
        self.calendar = calendar

    def to_json(self):
        return Strings.object_to_json(self.calendar)


if __name__ == "__main__":
    schedule_maker = ScheduleMaker(Calendar.available_topics())
    print(schedule_maker.to_json())
