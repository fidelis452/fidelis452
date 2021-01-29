# WRITE YOUR CODE SOLUTION HERE
import datetime
# import bus fare challenge
from datetime import date
import calendar
date = date.today()
print("Date:" + str(date))
print("Day:" + date.strftime("%a"))
fare = int(0)
if date.strftime('Mon'):
    fare = 100

if date.strftime('Tue'):
    fare = 100
if date.strftime("Wed"):
    fare = 100
if date.strftime("Thu"):
    fare = 100
if date.strftime("Fri"):
    fare = 100
if date.strftime("Sat"):
    fare = 60
if date.strftime("Sun"):
    fare = 80
print("Fare:" + str(fare))
