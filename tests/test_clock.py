import pytest

from ascii_clock.clock import (
    get_minutes_position, get_hours_position, convert_time, render_clock_face,
    validate_time, TimeValidationError, parse_time, time_to_clock)


def test_validate_time_raises_error_when_not_correct_length():
    with pytest.raises(TimeValidationError):
        validate_time('')
    with pytest.raises(TimeValidationError):
        validate_time('0')
    with pytest.raises(TimeValidationError):
        validate_time('00')
    with pytest.raises(TimeValidationError):
        validate_time('000')
    with pytest.raises(TimeValidationError):
        validate_time('0000')
    with pytest.raises(TimeValidationError):
        validate_time('00:')
    with pytest.raises(TimeValidationError):
        validate_time(':00')


def test_validate_time_raises_error_when_no_digits():
    with pytest.raises(TimeValidationError):
        validate_time('0h:00')
    with pytest.raises(TimeValidationError):
        validate_time('h0:00')
    with pytest.raises(TimeValidationError):
        validate_time('00:0m')
    with pytest.raises(TimeValidationError):
        validate_time('00:m0')


def test_validate_time_raises_error_when_invalid_time():
    with pytest.raises(TimeValidationError):
        validate_time('24:60')


def test_parse_time():
    assert parse_time('21:35') == (21, 35)
    assert parse_time('01:16') == (1, 16)
    assert parse_time('17:21') == (17, 21)


def test_get_hours_position():
    assert get_hours_position(0) == 0
    assert get_hours_position(1) == 1
    assert get_hours_position(2) == 2
    assert get_hours_position(3) == 3
    assert get_hours_position(4) == 4
    assert get_hours_position(5) == 5
    assert get_hours_position(6) == 6
    assert get_hours_position(7) == 7
    assert get_hours_position(8) == 8
    assert get_hours_position(9) == 9
    assert get_hours_position(10) == 10
    assert get_hours_position(11) == 11
    assert get_hours_position(12) == 0
    assert get_hours_position(13) == 1
    assert get_hours_position(14) == 2
    assert get_hours_position(15) == 3
    assert get_hours_position(16) == 4
    assert get_hours_position(17) == 5
    assert get_hours_position(18) == 6
    assert get_hours_position(19) == 7
    assert get_hours_position(20) == 8
    assert get_hours_position(21) == 9
    assert get_hours_position(22) == 10
    assert get_hours_position(23) == 11


def test_get_minutes_position():
    assert get_minutes_position(0) == 0
    assert get_minutes_position(1) == 0
    assert get_minutes_position(2) == 0
    assert get_minutes_position(3) == 0
    assert get_minutes_position(4) == 0
    assert get_minutes_position(5) == 1
    assert get_minutes_position(6) == 1
    assert get_minutes_position(7) == 1
    assert get_minutes_position(8) == 1
    assert get_minutes_position(9) == 1
    assert get_minutes_position(10) == 2
    assert get_minutes_position(11) == 2
    assert get_minutes_position(12) == 2
    assert get_minutes_position(13) == 2
    assert get_minutes_position(14) == 2
    assert get_minutes_position(15) == 3
    assert get_minutes_position(16) == 3
    assert get_minutes_position(17) == 3
    assert get_minutes_position(18) == 3
    assert get_minutes_position(19) == 3
    assert get_minutes_position(20) == 4
    assert get_minutes_position(21) == 4
    assert get_minutes_position(22) == 4
    assert get_minutes_position(23) == 4
    assert get_minutes_position(24) == 4
    assert get_minutes_position(25) == 5
    assert get_minutes_position(26) == 5
    assert get_minutes_position(27) == 5
    assert get_minutes_position(28) == 5
    assert get_minutes_position(29) == 5
    assert get_minutes_position(30) == 6
    assert get_minutes_position(31) == 6
    assert get_minutes_position(32) == 6
    assert get_minutes_position(33) == 6
    assert get_minutes_position(34) == 6
    assert get_minutes_position(35) == 7
    assert get_minutes_position(36) == 7
    assert get_minutes_position(37) == 7
    assert get_minutes_position(38) == 7
    assert get_minutes_position(39) == 7
    assert get_minutes_position(40) == 8
    assert get_minutes_position(41) == 8
    assert get_minutes_position(42) == 8
    assert get_minutes_position(43) == 8
    assert get_minutes_position(44) == 8
    assert get_minutes_position(45) == 9
    assert get_minutes_position(46) == 9
    assert get_minutes_position(47) == 9
    assert get_minutes_position(48) == 9
    assert get_minutes_position(49) == 9
    assert get_minutes_position(50) == 10
    assert get_minutes_position(51) == 10
    assert get_minutes_position(52) == 10
    assert get_minutes_position(53) == 10
    assert get_minutes_position(54) == 10
    assert get_minutes_position(55) == 11
    assert get_minutes_position(56) == 11
    assert get_minutes_position(57) == 11
    assert get_minutes_position(58) == 11
    assert get_minutes_position(59) == 11


def test_convert_time():
    assert convert_time(1, 10) == ['o', 'h', 'm', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o']
    assert convert_time(2, 15) == ['o', 'o', 'h', 'm', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o']
    assert convert_time(2, 17) == ['o', 'o', 'h', 'm', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o']
    assert convert_time(21, 10) == ['o', 'o', 'm', 'o', 'o', 'o', 'o', 'o', 'o', 'h', 'o', 'o']
    assert convert_time(2, 10) == ['o', 'o', 'x', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o']
    assert convert_time(1, 5) == ['o', 'x', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o']
    assert convert_time(3, 15) == ['o', 'o', 'o', 'x', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o']
    assert convert_time(4, 20) == ['o', 'o', 'o', 'o', 'x', 'o', 'o', 'o', 'o', 'o', 'o', 'o']
    assert convert_time(12, 1) == ['x', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o']


def test_render_clock_face():
    assert render_clock_face(['o', 'h', 'm', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o']) == """
     o
  o     h
 o       m
o         o
 o       o
  o     o
     o
"""


def test_time_to_clock():
    assert time_to_clock('21:35') == """
     o
  o     o
 o       o
h         o
 o       o
  m     o
     o
"""
    assert time_to_clock('01:06') == """
     o
  o     x
 o       o
o         o
 o       o
  o     o
     o
"""
