import time
import sqlite3
conn = sqlite3.connect('emp_sales.db')
sth = conn.cursor()
sth.execute('''create table emp (eid INT,
            ename TEXT,
            edept TEXT)''')

with open("emp.csv") as fobj:
    for var in fobj:
        if('sales' in var):
            eid,ename,edept,eplace,ecost = var.split(",")
            sth.execute("insert into emp (eid,ename,edept) values(?,?,?)",(eid,ename,edept))
		
conn.commit()
with open("sales.log","w") as wobj:
    sth.execute("select *from emp")
    for v in sth:
        time.sleep(1)
        wobj.write(f"{v[0]}:{v[1]}:{v[-1]}\t Entry Time:{time.ctime()}\n") # write to log file

conn.close()

