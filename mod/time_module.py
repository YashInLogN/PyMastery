# The time module provides functions for working with time and time-related operations.
# It can be used to get the current time, pause program execution, and measure time intervals.
# Common functions include time(), sleep(), ctime(), and strftime().

import time

# time.time() returns the current time as the number of seconds since the Unix Epoch.
# time.ctime() converts that timestamp into a readable date and time format.
# Both are useful for working with and displaying the current time.

print(time.ctime())

print(time.time())