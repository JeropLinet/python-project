import sqlite3

class AnimalDB:
    def __init__(self):
        self.conn=sqlite3.connect("vetpatientmanager.db")
        self.cursor=self.conn.cursor()

    def add_animal(self,name,age,type,breed):
        self.cursor.execute("INSERT INTO animals (name,age,type,breed) VALUES (?,?,?,?)",
                            (name,age,type,breed))
        self.conn.commit()
        animal_id=self.cursor.lastrowid
        return animal_id

    def all_animals(self):
        self.cursor.execute("SELECT * FROM animals")
        return self.cursor.fetchall()
    
    def animal_present(self,animal_id):
        self.cursor.execute("SELECT * FROM animals WHERE id=?",
                            (animal_id,))
        return self.cursor.fetchone()
    
    def delete_animal(self, animal_id):
 
     if not self.animal_present(animal_id):
        print(f"Animal with ID:{animal_id} is not in our database")
        return
     
     self.cursor.execute("DELETE FROM animals WHERE id = ?", (animal_id,))
     self.conn.commit()
     print(f"Animal with ID:{animal_id} has been removed.")

    def fetch_one_animal(self,animal_id):
        self.cursor.execute("SELECT * FROM animals WHERE id=?",
                                (animal_id,))
        row=self.cursor.fetchone()
        if row:
          return row
        else:
            print("Animal not found")
            return None
        
    def update_animal_name(self,old_name,new_name):
        self.cursor.execute("UPDATE animals SET name=? WHERE name=?",
                            
                            (new_name,old_name))
        self.conn.commit()
        if self.cursor.rowcount == 0:
          print("Update failed: No animal found with the provided name.")
        else:
         print(f"{old_name}'s name has been updated to {new_name}.")
