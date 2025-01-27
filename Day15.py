# Exercise 2 using if else

import time
timestamp = time.strftime('%I:%M:%S')
print(timestamp)
timestamp = int(time.strftime('%H'))
print(timestamp)
timestamp = int(time.strftime('%M'))
print(timestamp)
timestamp = int(time.strftime('%S'))
print(timestamp)
# https://docs.python.org/3/library/time.html#time.strftime

if timestamp < 12:
    print('Good Morning')
elif timestamp < 18:
    print('Good Afternoon')
else:
    print('Good Evening')
