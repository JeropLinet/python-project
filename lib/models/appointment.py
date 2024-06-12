import sqlite3

class AppointmentDB:
    def __init__(self):
        self.conn=sqlite3.connect("vetpatientmanager")
        self.cursor=self.conn.cursor()
    
    