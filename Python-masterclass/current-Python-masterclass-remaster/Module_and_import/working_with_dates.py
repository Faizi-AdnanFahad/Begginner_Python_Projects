import datetime
import pygame
import pytz

# Naive datetime

# DATES - datetime.date()
# d = datetime.date(2016, 7, 24)  # 2016-07-24
# print(d)
#
today = datetime.date.today()  # Current local date
# print(today)
#
# print(today.weekday())  # the number of day where Mon = 0, Sun = 6
# print(today.isoweekday())  # the number of day where Mon = 1, Sun = 7
#
# # Delta time
# tdelta = datetime.timedelta(days=7)
# print(today + tdelta)  # 7 days ahead of today's date
# print(today - tdelta)  # 7 days earlier of today's date

# ----------------------------
# ***NOTE***
# date2 = date1 + timedelta
# timedelta = date1 + date2
# ----------------------------

# bday = datetime.date(2021, 9, 24)
# till_bday = bday - today
# print(till_bday)  # number of days till the given date form today
# print(till_bday.total_seconds())   # number of seconds till the given date form today
#

# t = datetime.datetime(2016, 12, 23)
# print(t.date())

# ------------------------------------
# *adding days to a certain day and getting a new dat*
# td = datetime.timedelta(days=7)
# print(td + datetime.datetime.today())
# ------------------------------------
# *Countdown till a day*
# bday = datetime.datetime(2021, 6, 4)
# print(bday - datetime.datetime.today())
# ------------------------------------

# # TIMES - datetime.time()
#
# t = datetime.time(9, 30, 45, 10000)
# print(t)  # 09:30:45.010000
# print(t.second)  # 45
#
# print('---------------------------------------------------------------------------------------------------------------')
#
# # TIMES & DATES - datetime.datetime - *****Everything is accessible******
# dt = datetime.datetime(2016, 7, 26, 12, 30, 45, 100000)
# print(dt)  # 2016-07-26 12:30:45.100000
# print(dt.date())  # 2016-07-26
#
# tdelta = datetime.timedelta(hours=11, minutes=12)
# print((tdelta + dt).time())  # 23:42:45.100000
# print(tdelta + dt)  # 2016-07-26 23:42:45.100000
#
#
# print("-----------------------------------------------------------------------")
#
# dt_today = datetime.datetime.today()
# dt_now = datetime.datetime.now()
# dt_utcnow = datetime.datetime.utcnow()
#
# print(dt_today)
# print(dt_now)
# print(dt_utcnow)

# dt = datetime.datetime(2016, 7, 26, 12, 30, 45, tzinfo=pytz.UTC)
# print(dt)
# dt_UTC_now = datetime.datetime.now(tz=pytz.UTC)
# print(dt_UTC_now)
# # dt_utcnow = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)
# # print(dt_utcnow)
#
# for tz in pytz.all_timezones:
#     print(tz)

#
# for i in range(10):
#     print(f"i is {i:02}")  # 2 digits
#
# PI = 3.12313413414134
# print(f"PI is {PI:.2f}")  # PI is 3.12
#
# large = 1000000000000000000000
# print(f"It's separated by commas {large:,.2f}")  # It's separated by commas 1,000,000,000,000,000,000,000.00
#
#














