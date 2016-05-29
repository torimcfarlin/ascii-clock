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


def validate_time(time):
    try:
        datetime.datetime.strptime(time, '%H:%M')
    except ValueError:
        raise TimeValidationError('Time not in correct format (hh:mm). Try Again!')


def parse_time(time):
    return int(time[0:2]), int(time[3:])


def render_clock_face(clock_values):
    clock_face = deepcopy(CLOCK_FACE)
    return clock_face.format(*clock_values)


def convert_time(hour, minutes):
    clock_values = deepcopy(DEFAULT_CLOCK_VALUES)
    h_position = get_hours_position(hour)
    m_position = get_minutes_position(minutes)
    if h_position == m_position:
        clock_values[h_position] = 'x'
    else:
        clock_values[h_position] = 'h'
        clock_values[m_position] = 'm'
    return clock_values


def get_minutes_position(minutes):
    return (minutes - (minutes % 5)) / 5


def get_hours_position(hours):
    return hours % 12


def time_to_clock(time):
    hour, minutes = parse_time(time)
    clock_values = convert_time(hour, minutes)
    return render_clock_face(clock_values)
