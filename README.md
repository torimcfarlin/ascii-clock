# ascii-clock
A program which displays the time as an ascii clock


# Setting Up
First, set up your virtual environment

$ pip install virtualenv

$ virtualenv ascii-clock

$ python setup.py develop

# Converting the Time
Run the go script:

$ python go.py clock
```
21:35

     o
  o     o
 o       o
h         o
 o       o
  m     o
     o
```

# Running Tests
Run the go script:

$ python go.py tests
```
============================= test session starts ==============================
platform darwin -- Python 2.7.10, pytest-2.9.1, py-1.4.31, pluggy-0.3.1
rootdir: /Users/tmcfarlin/Documents/code/ascii-clock, inifile:
plugins: cov-2.2.1
collected 29 items

tests/test_clock.py .............................

========================== 29 passed in 0.03 seconds ===========================
```