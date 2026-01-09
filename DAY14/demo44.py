import sqlite3 

conn = sqlite3.connect("prod.log")
sth = conn.cursor()
sth.execute('''create table logs (id INTEGER PRIMARY KEY AUTOINCREMENT,
            log_time TEXT,
            level TEXT,
            message TEXT)''')

fobj = open("C:\\Users\\Karth\\production.log","r")
for var in fobj:
    if('ERROR' in var):
        L=var.split()
        time_stamp = L[:2]
        time_stamp="-".join(time_stamp)
        Log_level = L[2]
        Log_msg = "-".join(L[3:])
        sth.execute("insert into logs (log_time,level,message) values(?,?,?)",(time_stamp,Log_level,Log_msg))
fobj.close()
conn.commit()
conn.close()
