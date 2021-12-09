#!/usr/bin/env python3
import sqlite3

name = input("Name: ")
birthday = input("Birthday(xx/xx/xx or 01/23/02): ")

conn = sqlite3.connect('birthday.db')
c = conn.cursor()

c.execute('CREATE TABLE IF NOT EXISTS birthdays(name TEXT, date TEXT)')

insert = "INSERT INTO birthdays (name, date) VALUES (?, ?);"
conn.execute(insert, (name, birthday))


conn.commit()
c.close
conn.close()


