#DICE CODE
'''import random
while True:
    input("enter the roll of dice")
    a=random .randint (1,6)
    print(a)
    option=input("roll again?(Y/N)")
    if option=="Y":
        continue
    elif option =="n":
        break
    else:
       print("invalid option")



#6.CALENDAR MODULE      
import calendar
year=2026
month=8
print(calendar.month(year,month))

import calender
year=2026
print(calender.calendar(year))

import calendar
a=int(input("enter the year"))
b=int(iput("enter the month"))
print(calendar.month(a,b))


#7.DATE MODULE
from datetime import date
a=date.today()
print(a)

#8.DATETIME MODULE
a=datatime.datetime.now()
print(a)'''

#TIME MODULE
#EPOCH TIME
import time
a=time.time()
print(a)
#o/p-->1785328620.6388078


#LOCAL TIME
b=time.localtime(a)
print(b)

#time.struct_time(tm_year=2026, tm_mon=7, tm_mday=29, tm_hour=18, tm_min=21, tm_sec=22, tm_wday=2, tm_yday=210, tm_isdst=0)

#HUMANREADABLE TIME

print(f"today date is  {b.tm_mday}/{b.tm_mon}/{b.tm_year}")
#o/p-->today date is  29/7/2026

print(f"today time is  {b.tm_hour}:{b.tm_min}:{b.tm_sec}")
#o/p-->today time is  18:21:22

print(f"day is{b.tm_wday}-{b.tm_yday}-{b.tm_isdst}")
#day is2-210-0




#TASK
import random
import time
for i range (10):
    a=random.randint (1000,9999)
    print(a)
    time.sleep(2)
