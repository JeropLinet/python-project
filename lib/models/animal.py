import sqlite3

class AnimalD:
    def __init__(self):
        self.conn=sqlite3.connect("vetpatientmanager.db")
        self.cursor=self.conn.cursor()

    def add_animal(self,name,age,type,breed):
        self.cursor.execute("INSERT INTO animals (name,age,type,breed) VALUES (?,?,?,?)",
                            (name,age,type,breed))
        self.conn.commit()