#!/usr/bin/env python3

import sqlite3

conn = sqlite3.connect('birthday.db')
c = conn.cursor()

#gets list combo of name and date
c.execute('''SELECT * FROM birthdays''')
combo_list = c.fetchall();

#gets date for comparison
c.execute('''SELECT date FROM birthdays''')
date_list = c.fetchall();

for i in combo_list:
    print(i)

i=0
for date in date_list:
    day = (str(date[0]))
    if day[:-7] == '0':
        day = day[1:-6]
    else:
        day = day[:-6]
#iterable only ranges 1-12 or 1-18 but dates go 1-12 so if its iterable 18 it can't be printed
    for i in range(0,13):
        if int(day) == i: 
           # print(combo_list[i])
            pass
    
conn.commit()
c.close
conn.close()
