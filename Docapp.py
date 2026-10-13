print("\t***DOCTOR APPOINTMENT SYSTEM***")

appointments=[]
def book_appointment():
    name = input("Enter Patient Name: ")
    age = int(input("Enter Age: "))
    doctor = input("Enter Doctor Name: ")
    date = input("Enter Appointment Date : ")

    appointments.append([name, age, doctor, date])
    print("appointment booked successfully")

def display_appointments():
    if len(appointments) == 0:
        print("No appointments booked.")
    else:
        print("few appointments")

def cancel_appointment():
    if len(appointments) == 0:
        print("No appointments available.")
        return
         
    n = int(input("Enter appointment number to cancel: "))
    if 1 <= n <= len(appointments):
        appointments.pop(n-1)
        print("Appointment cancelled successfully")
    else:
        print("Invalid appointment number.")

choice = input("select\n1.Bookappointment\n2.DisplayAppointments\n3.Cancel Appointment")
if choice == '1':
    book_appointment()
elif choice == '2':
    display_appointments()
elif choice == '3':
    cancel_appointment()
elif choice == '4':
    print("Thank you for using the Doctor Appointment System.")

else:
    print("Invalid choice")
