import sqlite3

class DoctorDB:
    def __init__(self):
        self.conn=sqlite3.connect("vetpatientmanager.db")
        self.cursor=self.conn.cursor()

    def add_doctors(self,name,specialization):
        self.cursor.execute("INSERT INTO doctors (name,specialization) VALUES (?,?)",
                            (name,specialization))
        self.conn.commit()
        doctor_id=self.cursor.lastrowid
        return doctor_id

    def all_doctors(self):
        self.cursor.execute("SELECT * FROM doctors")
        return self.cursor.fetchall()
   
    def doctor_present(self,doctor_id):
        self.cursor.execute("SELECT * FROM doctors WHERE id=?",
                            (doctor_id,))
        return self.cursor.fetchone()
    
    def delete_doctor(self, doctor_id):
     if not self.doctor_present(doctor_id):
        print(f"Doctor with ID:{doctor_id} is not in our database")
        return
     self.cursor.execute("DELETE FROM doctors WHERE id = ?", (doctor_id,))
     self.conn.commit()
     print(f"Doctor with ID:{doctor_id} has been removed.")
    
    def fetch_one_doctor(self,doctor_id):
        self.cursor.execute("SELECT * FROM doctors WHERE id=?",
                                (doctor_id,))
        row=self.cursor.fetchone()
        if row:
            return row
        else:
            print("Doctor not found")
            return None
    
    def update_doctor_name(self,old_name,new_name):
        self.cursor.execute("UPDATE doctors SET name=? WHERE name=?",
                            
                            (new_name,old_name))
        self.conn.commit()
        if self.cursor.rowcount == 0:
          print("Update failed: No doctor found with the provided name.")
        else:
         print(f"{old_name}'s name has been updated to {new_name}.")