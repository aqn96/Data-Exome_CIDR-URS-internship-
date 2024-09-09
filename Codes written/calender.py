# -*- coding: utf-8 -*-
"""
Created on Sat Aug  3 14:07:58 2019

@author: aqngu
"""

import calendar
import datetime
from datetime import date

def diff_dates(date1, date2): 
  return abs(date1-date2)

def main():
  month = datetime.date.today().month
  year = datetime.date.today().year
  d1 = date(2019,6,18)
  d2 = date.today()
  result = diff_dates(d1,d2)
  print ("{} days between {}, the day we first date, and today's date {}".format(result,d1,d2))
  print(calendar.month(2019, 6))
  print(calendar.month(year,month)) 

  
main()
    