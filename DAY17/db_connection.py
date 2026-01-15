import sqlite3

conn = sqlite3.connect("emp.db")

conn.execute("create table emp(name TEXT,dob TEXT)")
conn.close()
