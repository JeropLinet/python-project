# lib/cli.py
from models.animal import AnimalDB
from models.doctor import DoctorDB
from models.appointment import AppointmentDB
from helpers import (exit_program)

def main():
    animal_instance=AnimalDB()
    doctor_instance=DoctorDB()
    appointment_instance=AppointmentDB()
    while True:
        menu()
        choice = input(">")
        if choice == "1":
            name = input("Name of Animal: ")
            age = int(input("Age of Animal(weeks): "))
            type = input("Type of Animal: ")  # Renamed to type_ to avoid conflict with Python keyword
            breed = input("Breed of Animal: ")
            animal_instance.add_animal(name, age, type, breed)
        
        elif choice == "2":
            animal_id=int(input("Enter Animal ID:"))
            animal_instance.delete_animal(animal_id)

        elif choice == "3":
            name = input("Name of Doctor: ")
            speciality = input("Specialisation of Doctor: ")
            doctor_instance.add_doctors(name, speciality)

        elif choice =="4":
            doctor_id=int(input("Enter Doctor ID:"))
            doctor_instance.delete_doctor(doctor_id)

        elif choice == "5":
            animal_id = int(input("Enter Animal ID: "))
            doctor_id = int(input("Enter Doctor ID: "))
            symptoms = input("Symptoms of Animal: ")
            time_in = input("Time of appointment: ")
            appointment_instance.add_appointments(animal_id, doctor_id,symptoms, time_in)

        elif choice == "6":
            appointment_id = int(input("Appointment ID: "))
            appointment_instance.cancel_appointment(appointment_id)

        elif choice == "7":
            doctors = doctor_instance.all_doctors()
            if doctors:
                print(f"{'Doctor ID':<15}{'Name':<25}{'Speciality':<15}")
                print("-" * 55)
                for doctor in doctors:
                    print(f"{doctor[0]:<15}{doctor[1]:<25}{doctor[2]:<15}")
            else:
                print("No doctors found.")

        elif choice == "8":
            animals = animal_instance.all_animals()
            if animals:
                print(f"{'Animal ID':<15}{'Name':<25}{'Age':<10}{'Type':<15}{'Breed':<20}")
                print("-" * 80)
                for animal in animals:
                    print(f"{animal[0]:<15}{animal[1]:<25}{animal[2]:<10}{animal[3]:<15}{animal[4]:<20}")
            else:
                print("No animals found.")

        elif choice == "9":
            appointments = appointment_instance.all_appointments()
            if appointments:
                print(f"{'Appointment ID':<15}{'Animal Name':<25}{'Doctor Name':<25}{'Time':<20}")
                print("-" * 85)
                for appointment in appointments:
                    print(f"{appointment[0]:<15}{appointment[1]:<25}{appointment[2]:<25}{appointment[3]:<20}")
            else:
                print("No appointments found.")

        elif choice == "10":
            exit_program()
        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("\n1.Log Animal")
    print("2.Delete Animal")
    print("3.Log Doctor")
    print("4.Delete Doctor")
    print("5.Schedule Appointment")
    print("6.Cancel Appointment")
    print("7.List of all Doctors")
    print("8.List of all Animals")
    print("9.List of all Appointments")
    print("10.Exit the Program")


if __name__ == "__main__":
    main()
