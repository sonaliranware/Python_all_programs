'''
inbuilt function(modues)---math,sys,os,datetime,random,calender'''

import math as m
print("factorial is ",m.factorial(5))
print("floor value is",m.floor(5.6))
print("ceil value is ",m.ceil(7.5))
print("sqrt valur is",m.sqrt(25))
print("pi is",m.pi) 
print("pow is ",m.pow(3,2))

#area of circle using math function
def area1(r):
    return m.pi*r*r
print("area of circle is ",area1(2))    



#date time function
import datetime as d
import time as t
print(d.datetime.now())
print(d.date.today())
print(t.localtime())
tk=t.localtime()
print("current year is ",tk.tm_year)
print("current month is ",tk.tm_mon)
print("current day is ",tk.tm_mday)


import calendar
c=calendar.TextCalendar(calendar.TUESDAY)
c.prmonth(2024,10)


#random module
import random
mylist=["java","python","sql","Wd","django"]
for i in range (5):
    print(random.choice(mylist))



