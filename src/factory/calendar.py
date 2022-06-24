
from src.constants.day import Day
from src.constants.teacher import Teacher
from src.constants.topic_id import TopicId
from src.services.stuff import Stuff
from src.services.time import Time
from src.services.topic import Topic


class Calendar:

    @staticmethod
    def available_topics():
        return [
                Topic(
                        topic_id=TopicId.CALCULUS,
                        fixed=[
                                Stuff(Teacher.CARMEN_SALAS, [
                                    Time(Day.MONDAY, 9, 10.5),
                                    Time(Day.WEDNESDAY, 9, 10.5)
                                ]),
                                Stuff(Teacher.CARMEN_SALAS, [
                                    Time(Day.MONDAY, 10.5, 12),
                                    Time(Day.WEDNESDAY, 10.5, 12)
                                ]),
                                Stuff(Teacher.NORMA_SARMIENTO, [
                                    Time(Day.MONDAY, 9, 10.5),
                                    Time(Day.WEDNESDAY, 9, 10.5)
                                ])
                        ],
                        monitory=[
                                Stuff(Teacher.MONITOR, [
                                    Time(Day.SATURDAY, 8, 10)
                                ]),
                                Stuff(Teacher.MONITOR, [
                                    Time(Day.SATURDAY, 8, 10)
                                ]),
                                Stuff(Teacher.MONITOR, [
                                    Time(Day.SATURDAY, 8, 10)
                                ])
                        ]
                ),
                Topic(
                        topic_id=TopicId.DIGITAL_SYSTEMS,
                        fixed=[
                                Stuff(Teacher.GERMAN_OBANDO, [
                                    Time(Day.TUESDAY, 14, 15.5),
                                    Time(Day.THURSDAY, 14, 15.5)
                                ])
                        ],
                        laboratory=[
                                Stuff(Teacher.GERMAN_OBANDO, [
                                    Time(Day.WEDNESDAY, 14, 16),
                                ]),
                                Stuff(Teacher.GERMAN_OBANDO, [
                                    Time(Day.FRIDAY, 11, 13),
                                ]),
                                Stuff(Teacher.UNKNOWN, [
                                    Time(Day.FRIDAY, 11, 13),
                                ])
                        ]
                ),
                Topic(
                        topic_id=TopicId.ALGORITHMS,
                        fixed=[
                                Stuff(Teacher.CARLOS_ALVAREZ, [
                                    Time(Day.MONDAY, 7, 8.5),
                                    Time(Day.WEDNESDAY, 7, 8.5),
                                    Time(Day.FRIDAY, 7, 9)
                                ]),
                                Stuff(Teacher.CARLOS_ALVAREZ, [
                                    Time(Day.MONDAY, 11, 12.5),
                                    Time(Day.TUESDAY, 11, 12.5),
                                    Time(Day.THURSDAY, 11, 13)
                                ]),
                                Stuff(Teacher.PEDRO_WIGHTMAN, [
                                    Time(Day.MONDAY, 7.5, 9),
                                    Time(Day.WEDNESDAY, 7.5, 9),
                                    Time(Day.FRIDAY, 7, 9)
                                ])
                        ],
                        monitory=[
                                Stuff(Teacher.MONITOR, [
                                    Time(Day.TUESDAY, 7, 9)
                                ])
                        ]
                ),
                Topic(
                        topic_id=TopicId.LOGIC,
                        fixed=[
                            Stuff(Teacher.UNKNOWN, [
                                Time(Day.TUESDAY, 11, 13),
                                Time(Day.THURSDAY, 11, 13)
                            ]),
                            Stuff(Teacher.DANIEL_BOJACA, [
                                Time(Day.TUESDAY, 11, 13),
                                Time(Day.THURSDAY, 11, 13)
                            ]),
                            Stuff(Teacher.DANIEL_BOJACA, [
                                Time(Day.TUESDAY, 9, 11),
                                Time(Day.THURSDAY, 9, 11)
                            ])
                        ]
                ),
                Topic(
                        topic_id=TopicId.ANALYSIS,
                        fixed=[
                            Stuff(Teacher.GLORIA_GALLO, [
                                Time(Day.TUESDAY, 7, 9)
                            ]),
                            Stuff(Teacher.ADRYAN_PINEDA, [
                                Time(Day.THURSDAY, 7, 9)
                            ]),
                            Stuff(Teacher.TIRSO_BUENO, [
                                Time(Day.THURSDAY, 7, 9)
                            ])
                        ]
                ),
                Topic(
                        topic_id=TopicId.CONSTITUTION,
                        fixed=[
                            Stuff(Teacher.JESSICA_MURILLO, [
                                Time(Day.FRIDAY, 14, 16)
                            ]),
                            Stuff(Teacher.HAROLD_VILLAMIL, [
                                Time(Day.FRIDAY, 14, 16)
                            ]),
                            Stuff(Teacher.MARIA_LOPEZ, [
                                Time(Day.THURSDAY, 9 , 11)
                            ])
                        ]
                ),
                Topic(
                        topic_id=TopicId.MUTIS,
                        fixed=[
                            Stuff(Teacher.JHONATAN_DIAZ, [
                                Time(Day.MONDAY, 14, 17)
                            ]),
                            Stuff(Teacher.JHONATAN_DIAZ, [
                                Time(Day.TUESDAY, 17, 18.5),
                                Time(Day.THURSDAY, 17, 18.5)
                            ]),
                            Stuff(Teacher.MARIA_BATISTA, [
                                Time(Day.MONDAY, 13, 16)
                            ]),
                            Stuff(Teacher.MARIA_BATISTA, [
                                Time(Day.THURSDAY, 13, 16)
                            ])
                        ]
                )
        ]
