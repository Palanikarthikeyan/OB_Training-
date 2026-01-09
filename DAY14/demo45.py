import sqlite3
class LogParser:
    def __init__(self,log_fname):
        self.log_fname = log_fname
        self.pattern = "ERROR"
    def parse(self):
        with open(self.log_fname,'r') as fobj:
            for var in fobj:
                if('ERROR' in var):
                    self.L=var.split()
                    self.time_stamp = self.L[:2]
                    self.time_stamp="-".join(self.time_stamp)
                    self.Log_level = self.L[2]
                    self.Log_msg = "-".join(self.L[3:])
        yield {
            'time': self.time_stamp,
            'level':self.Log_level,
            'message':self.Log_msg
        }
        
class DatabaseManager:
    def __init__(self,db_file):
        self.db_file = db_file
        self.conn = sqlite3.connect(self.db_file)
        self.cursor = self.conn.cursor()
        self.create_table()
    def create_table(self):
        self.cursor.execute("""
                            create table if not exists logs(
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                log_time TEXT,
                                level TEXT,
                                message TEXT
                            )""")
        self.conn.commit()
    def insert_log(self,log_time,level,message):
        self.cursor.execute("insert into logs (log_time,level,message) values (?,?,?)",(log_time,level,message))
        self.conn.commit()
    def close(self):
        self.conn.close()
        
class LogProcessor:
    def __init__(self,parser,db_manager):
        self.parser = parser
        self.db = db_manager
    def process(self):
        for var in self.parser.parse():
            self.db.insert_log(
                var["time"],
                var["level"],
                var["message"]
            )
            
log_file = "production.log"
db_file = "logs.db"

parser = LogParser(log_file)

db_manager = DatabaseManager(db_file)

processor =LogProcessor(parser,db_manager)

processor.process()


db_manager.close()

