import time
import sqlite3
import logging

## ----------logging configuration
logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s %(message)s"
)
logging.info("Application Started")

### ------------ DB Operation
try:
    conn = sqlite3.connect('emp.db')
    if(conn):
        logging.info("Connected to Emp DB")
    sth = conn.cursor()
    sth.execute('''create table emp (eid INT,
            ename TEXT,
            edept TEXT)''')
    with open("emp.csv") as fobj:
        for var in fobj:
            eid,ename,edept,eplace,ecost = var.split(",")
            sth.execute("insert into emp (eid,ename,edept) values(?,?,?)",(eid,ename,edept))
    conn.commit()
    logging.info("Emp records are inserted")
    with open("e1.log","w") as wobj:
        sth.execute("select *from emp")
        logging.info("Fetched emp records")
        for v in sth:
            time.sleep(1)
            wobj.write(f"{v[0]}:{v[1]}:{v[-1]}\t Entry Time:{time.ctime()}\n") # write to log file
except Exception as eobj:
    logging.error(f"Database error occurred:{eobj}")
finally:
    if conn:
        conn.close()
        logging.info("Database connection closed")

logging.info("Application finished")
