#exercise 2 solution day 15
import time
t = time.strftime('%I')
hour = int(time.strftime('%I'))
print(hour)

# https://docs.python.org/3/library/time.html#time.strftime

if (hour>=0 and hour<12):
    print('Good Morning')
elif (hour>=12 and hour<17):
    print('Good Afternoon')
elif (hour>=17 and hour<0):
    print('Good Evening')