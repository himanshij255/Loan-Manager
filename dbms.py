# dbms.py
import sqlite3

# Shared connection and cursor
con = sqlite3.connect("mydb")
cur = con.cursor()
