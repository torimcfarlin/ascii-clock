import click

from ascii_clock.clock import TimeValidationError, AsciiClock


def get_ascii_clock():
    ascii_clock = None
    while ascii_clock is None:
        try:
            ascii_clock = AsciiClock(str(input('')))
        except TimeValidationError as e:
            print e.message
    return ascii_clock


@click.command()
def clock():
    ascii_clock = get_ascii_clock()
    print ascii_clock.to_clock_face()


if __name__ == '__main__':
    clock()
