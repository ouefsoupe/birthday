#!/usr/bin/env python3
import sqlite3
from datetime import date
#compare date

#generate current date
today = date.today()
current = (today.strftime("%m/%d/%y"))
foo = (current[:-3])

#prepare Sqlite3 connection
conn = sqlite3.connect('birthday.db')
c = conn.cursor()

#turns db into list
#gets dates
c.execute('''SELECT date FROM birthdays''') 
date_result = c.fetchall();

#gets names
c.execute('''SELECT name FROM birthdays''')
name_result = c.fetchall();

#loop compares db dates to the current date

i = 0

for date in date_result:
    if foo == date[0][:-3]:
        print("Happy birthday", name_result[i][0])
    i += 1
i = 0
for date in date_result:
    if foo[:-3] == date[0][:-6]:
        birt = int(foo[-2:])
        current = date[0][:-3]
        current = int(current[-2:])
        print((current-birt),  " days until ", name_result[i][0], "'s birthday")
    i += 1


conn.commit()
c.close
conn.close()
