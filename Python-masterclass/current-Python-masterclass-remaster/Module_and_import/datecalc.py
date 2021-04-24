# import time
#
# print(time.gmtime())  # print(time.gmtime(time.time()))
#
# print(time.localtime())  # print(time.localtime(time.time()))
#
# print(time.time())  # number of seconds since 1/1/1970

# time_here = time.localtime()
# print(time_here)
# print("Year: ", time_here[0], time_here.tm_year)
# print("Month: ", time_here[1], time_here.tm_mon)
# print("Day: ", time_here[2], time_here.tm_mday)

import time
# from time import time as my_timer
from time import perf_counter as my_timer
import random

input("Please enter to start")

wait_time = random.randint(1, 6)
time.sleep(wait_time)  # the program stops for the number of seconds
start_time = my_timer()  # returns the current time in seconds
input("Press enter to stop")

end_time = my_timer()  # returns the end time in seconds

print(f"Started at " + time.strftime("%X", time.localtime(start_time)))  # time.strftime() converts to stringformat, %X local time represention
print("Ended at " + time.strftime("%X", time.localtime(end_time)))

print(f"Your reaction time was {end_time - start_time} seconds")





















