import sqlite3

class AnimalDB:
    def __init__(self):
        self.conn=sqlite3.connect("vetpatientmanager.db")
        self.cursor=self.conn.cursor()

    def add_animal(self,name,age,type,breed):
        self.cursor.execute("INSERT INTO animals (name,age,type,breed) VALUES (?,?,?,?)",
                            (name,age,type,breed))
        self.conn.commit()

    def all_animals(self):
        self.cursor.execute("SELECT * FROM animals")
        return self.cursor.fetchall()
    
    def animal_present(self,animal_id):
        self.cursor.execute("SELECT * FROM animals WHERE id=?",
                            (animal_id))
        self.cursor.fetchone()
