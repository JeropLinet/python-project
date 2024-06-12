import sqlite3
from .animal import AnimalDB
from .doctor import DoctorDB

class AppointmentDB:
    def __init__(self):
        self.conn=sqlite3.connect("vetpatientmanager")
        self.cursor=self.conn.cursor()
        self.animal_db=AnimalDB()
        self.doctor_db=DoctorDB()
    
    def add_appointments(self,animal_id,doctor_id,symptoms,time_in):
        if not self.animal_db.animal_present(animal_id):
            print(f"Animal with ID:{animal_id} is not in our database")
            return
        if not self.doctor_db.doctor_present(doctor_id):
            print(f"Doctor with ID:{doctor_id} is not in our database")
            return
        self.cursor.execute("INSERT INTO appointments (animal_id, doctor_id,symptoms, time_in) VALUES (?, ?, ?, ?)", 
                            (animal_id, doctor_id,symptoms, time_in))
        self.conn.commit()
        print(f"Doctor with ID:{doctor_id} is assigned to Animal with ID:{animal_id}")
        