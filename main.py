from controllers.hospital_controller import HospitalController
from controllers.patient_controller import PatientController
from controllers.appointment_controller import AppointmentController

hospital = HospitalController()
patient = PatientController()
appt = AppointmentController()

while True:
    print("""
---- HEALTHCARE MANAGEMENT SYSTEM ----
1. View hospital structure (Tree)
2. Add patient
3. Add diagnosis (Linked List)
4. Add patient to appointment queue
5. Serve next patient (Queue)
6. Exit
""")

    c = input("Choose: ")

    if c == "1":
        hospital.show_structure()
    elif c == "2":
        patient.add_patient()
    elif c == "3":
        patient.add_diagnosis()
    elif c == "4":
        appt.add_to_queue()
    elif c == "5":
        appt.serve_patient()
    elif c == "6":
        print("Goodbye!")
        break
