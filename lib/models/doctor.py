import sqlite3

class DoctorDB:
    def __init__(self):
        self.conn=sqlite3.connect("vetpatientmanager.db")
        self.cursor=self.conn.cursor()
    def add_doctors(self,name,speciality):
        self.cursor.execute("INSERT INTO doctors (name,speciality) VALUES (?,?)",
                            (name,speciality))
        self.conn.commit()
