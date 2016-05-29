import click

from ascii_clock.clock import time_to_clock, validate_time, TimeValidationError


def get_time():
    time = None
    while time is None:
        time = str(input(''))
        try:
            validate_time(time)
        except TimeValidationError as e:
            print e.message
            time = None
    return time


@click.command()
def clock():
    time = get_time()
    clock = time_to_clock(time)
    print clock


if __name__ == '__main__':
    clock()
