import sqlite3

class DoctorDB:
    def __init__(self):
        self.conn=sqlite3.connect("vetpatientmanager.db")
        self.cursor=self.conn.cursor()

    def add_doctors(self,name,specialization):
        self.cursor.execute("INSERT INTO doctors (name,specialization) VALUES (?,?)",
                            (name,specialization))
        self.conn.commit()

    def all_doctors(self):
        self.cursor.execute("SELECT * FROM doctors")
        return self.cursor.fetchall()
   
    def doctor_present(self,doctor_id):
        self.cursor.execute("SELECT * FROM doctors WHERE id=?",
                            (doctor_id,))
        return self.cursor.fetchone()
    
    def delete_doctor(self,doctor_id):
        self.cursor.execute("DELETE FROM doctors WHERE id=?",
                            (doctor_id,))
        self.conn.commit()
        print(f"Doctor with ID:{doctor_id} is removed")