import datetime
from copy import deepcopy

CLOCK_FACE = """
     {0}
  {11}     {1}
 {10}       {2}
{9}         {3}
 {8}       {4}
  {7}     {5}
     {6}
"""
DEFAULT_CLOCK_VALUES = ['o'] * 12


class TimeValidationError(Exception):
    pass


class ClockHand(object):
    CLOCK_SYMBOL = 'x'

    def __init__(self, value):
        self.value = value


class HourHand(ClockHand):
    CLOCK_SYMBOL = 'h'

    def to_clock_position(self):
        return self.value % 12


class MinuteHand(ClockHand):
    CLOCK_SYMBOL = 'm'

    def to_clock_position(self):
        return (self.value - (self.value % 5)) / 5


class AsciiClock(object):
    CO_LOCATED_SYMBOL = 'x'

    def __init__(self, time):
        self.validate_time(time)
        self.hour_hand = HourHand(int(time[0:2]))
        self.minute_hand = MinuteHand(int(time[3:]))

    @staticmethod
    def validate_time(time):
        try:
            datetime.datetime.strptime(time, '%H:%M')
        except ValueError:
            raise TimeValidationError('Time not in correct format (hh:mm). Try Again!')

    def to_clock_face(self):
        clock_values = deepcopy(DEFAULT_CLOCK_VALUES)
        clock_face = deepcopy(CLOCK_FACE)
        hour_position = self.hour_hand.to_clock_position()
        minute_position = self.minute_hand.to_clock_position()
        if hour_position == minute_position:
            clock_values[hour_position] = ClockHand.CLOCK_SYMBOL
        else:
            clock_values[hour_position] = HourHand.CLOCK_SYMBOL
            clock_values[minute_position] = MinuteHand.CLOCK_SYMBOL
        return clock_face.format(*clock_values)
