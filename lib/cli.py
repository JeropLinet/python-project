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
        choice = input("\n>")
        if choice == "1":
            name = input("Name of Animal: ")
            age = int(input("Age of Animal(weeks): "))
            type = input("Type of Animal: ")  # Renamed to type_ to avoid conflict with Python keyword
            breed = input("Breed of Animal: ")
            animal_id=animal_instance.add_animal(name, age, type, breed)
            print(f"\nAnimal with ID {animal_id} Logged")

        
        elif choice == "2":
            animal_id=int(input("Enter Animal ID:"))
            animal_instance.delete_animal(animal_id)
        
        elif choice == "3":
            animal_id=int(input("Enter Animal ID:"))
            animal = animal_instance.fetch_one_animal(animal_id)
            if animal:
                print(f"{'Animal ID':<15}{'Name':<25}{'Age':<10}{'Type':<15}{'Breed':<20}")
                print("-" * 55)
                print(f"{animal[0]:<15}{animal[1]:<25}{animal[2]:<10}{animal[3]:<15}{animal[4]:<20}")

        elif choice=="4" :
            old_name = input("Enter the animal Name: ")
            new_name = input("Enter the new name for the animal: ")
            animal_instance.update_animal_name(old_name, new_name)
            
        elif choice == "5":
            name = input("Name of Doctor: ")
            speciality = input("Specialisation of Doctor: ")
            doctor_id=doctor_instance.add_doctors(name, speciality)
            print(f"\nDoctor with ID {doctor_id} Logged")
        
        elif choice =="6":
            doctor_id=int(input("Enter Doctor ID:"))
            doctor_instance.delete_doctor(doctor_id)
        
        elif choice== "7":
            doctor_id=int(input("Enter Doctor ID:"))
            doctor= doctor_instance.fetch_one_doctor(doctor_id)
            if doctor:
                print(f"{'Doctor ID':<15}{'Name':<25}{'Speciality':<15}")
                print("-" * 55)
                print(f"{doctor[0]:<15}{doctor[1]:<25}{doctor[2]:<15}")

        elif choice=="8" :
            old_name = input("Enter the doctor Name: ")
            new_name = input("Enter the new name for the doctor: ")
            doctor_instance.update_doctor_name(old_name, new_name)

        elif choice == "9":
            animal_id = int(input("Enter Animal ID: "))
            doctor_id = int(input("Enter Doctor ID: "))
            symptoms = input("Symptoms of Animal: ")
            time_in = input("Time of appointment: ")
            appointment_instance.add_appointments(animal_id, doctor_id,symptoms, time_in)

        elif choice == "10":
            appointment_id = int(input("Appointment ID: "))
            appointment_instance.cancel_appointment(appointment_id)

        elif choice == "11":
            doctors = doctor_instance.all_doctors()
            if doctors:
                print(f"{'Doctor ID':<15}{'Name':<25}{'Speciality':<15}")
                print("-" * 55)
                for doctor in doctors:
                    print(f"{doctor[0]:<15}{doctor[1]:<25}{doctor[2]:<15}")
            else:
                print("No doctors found.")

        elif choice == "12":
            animals = animal_instance.all_animals()
            if animals:
                print(f"{'Animal ID':<15}{'Name':<25}{'Age':<10}{'Type':<15}{'Breed':<20}")
                print("-" * 80)
                for animal in animals:
                    print(f"{animal[0]:<15}{animal[1]:<25}{animal[2]:<10}{animal[3]:<15}{animal[4]:<20}")
            else:
                print("No animals found.")

        elif choice == "13":
            appointments = appointment_instance.all_appointments()
            if appointments:
                print(f"{'Appointment ID':<15}{'Animal Name':<25}{'Doctor Name':<25}{'Time':<20}")
                print("-" * 85)
                for appointment in appointments:
                    print(f"{appointment[0]:<15}{appointment[1]:<25}{appointment[2]:<25}{appointment[3]:<20}")
            else:
                print("No appointments found.")

        elif choice == "14":
            exit_program()
        else:
            print("Invalid choice")


def menu():
    print("\nPlease select an option:")
    print("\n1.Log Animal")
    print("2.Delete Animal")
    print("3.Find Animal by ID")
    print("4.Change Animal's Name")
    print("5.Log Doctor")
    print("6.Delete Doctor")
    print("7.Find Doctor by ID")
    print("8.Change Doctor's Name")
    print("9.Schedule Appointment")
    print("10.Cancel Appointment")
    print("11.List of all Doctors")
    print("12.List of all Animals")
    print("13.List of all Appointments")
    print("14.Exit the Program")


if __name__ == "__main__":
    main()
