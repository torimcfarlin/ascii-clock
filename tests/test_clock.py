import pytest

from ascii_clock.clock import AsciiClock, TimeValidationError, HourHand, MinuteHand


def test_ascii_clock_validation_raises_error_when_not_correct_length():
    with pytest.raises(TimeValidationError):
        AsciiClock('')
    with pytest.raises(TimeValidationError):
        AsciiClock('0')
    with pytest.raises(TimeValidationError):
        AsciiClock('00')
    with pytest.raises(TimeValidationError):
        AsciiClock('000')
    with pytest.raises(TimeValidationError):
        AsciiClock('0000')
    with pytest.raises(TimeValidationError):
        AsciiClock('00:')
    with pytest.raises(TimeValidationError):
        AsciiClock(':00')


def test_ascii_clock_validation_raises_error_when_no_digits():
    with pytest.raises(TimeValidationError):
        AsciiClock('0h:00')
    with pytest.raises(TimeValidationError):
        AsciiClock('h0:00')
    with pytest.raises(TimeValidationError):
        AsciiClock('00:0m')
    with pytest.raises(TimeValidationError):
        AsciiClock('00:m0')


def test_ascii_clock_validation_raises_error_when_invalid_time():
    with pytest.raises(TimeValidationError):
        AsciiClock('24:60')


def test_ascii_clock_attributes():
    clock = AsciiClock('21:35')
    assert isinstance(clock.hour_hand, HourHand)
    assert clock.hour_hand.value == 21
    assert isinstance(clock.minute_hand, MinuteHand)
    assert clock.minute_hand.value == 35


@pytest.mark.parametrize('hours, position', [
    ([0, 12], 0),
    ([1, 13], 1),
    ([2, 14], 2),
    ([3, 15], 3),
    ([4, 16], 4),
    ([5, 17], 5),
    ([6, 18], 6),
    ([7, 19], 7),
    ([8, 20], 8),
    ([9, 21], 9),
    ([10, 22], 10),
    ([11, 23], 11)
])
def test_hour_hand_to_clock_position(hours, position):
    for hour in hours:
        assert HourHand(hour).to_clock_position() == position


@pytest.mark.parametrize('minutes, position', [
    ([0, 1, 2, 3, 4], 0),
    ([5, 6, 7, 8, 9], 1),
    ([10, 11, 12, 13, 14], 2),
    ([15, 16, 17, 18, 19], 3),
    ([20, 21, 22, 23, 24], 4),
    ([25, 26, 27, 28, 29], 5),
    ([30, 31, 32, 33, 34], 6),
    ([35, 36, 37, 38, 39], 7),
    ([40, 41, 42, 43, 44], 8),
    ([45, 46, 47, 48, 49], 9),
    ([50, 51, 52, 53, 54], 10),
    ([55, 56, 57, 58, 59], 11)
])
def test_minute_hand_to_clock_position(minutes, position):
    for minute in minutes:
        assert MinuteHand(minute).to_clock_position() == position


def test_ascii_clock_to_clock_face():
    assert AsciiClock('04:59').to_clock_face() == """
     o
  m     o
 o       o
o         o
 o       h
  o     o
     o
"""
    assert AsciiClock('21:35').to_clock_face() == """
     o
  o     o
 o       o
h         o
 o       o
  m     o
     o
"""
    assert AsciiClock('01:06').to_clock_face() == """
     o
  o     x
 o       o
o         o
 o       o
  o     o
     o
"""
