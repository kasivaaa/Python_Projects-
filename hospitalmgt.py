# CLINIC MANAGEMENT SYSTEM
#Creating a dictionary


hospital_records = {
    "Patient001": {
        "Name": "Mary Kamau",
        "Age": 38,
        "Doctor": None,
        "Status": "Waiting"
    },
    "Patient002": {
        "Name": "Kate Kerubo",
        "Age": 26,
        "Doctor": "Dr. Njoroge",
        "Status": "Under Treatment"
    }
}


# ADD PATIENT

def add_patient():

    name = input("Enter patient name: ").strip()

    for details in hospital_records.values():
        #what to do if name exists
        if details["Name"].lower() == name.lower():
            print("Patient already exists.")
            return
# what to continue with if name does not exist
    try:
        age = int(input("Enter patient age: "))
    # Incase input is not an integer
    except ValueError:
        print("Age must be a number.")
        return
# Add patient ID
    patient_id = f"Patient{len(hospital_records) + 1:03}"
    # Add 1 to the legnth. :03 means minimum width 3 digits, fill blank spaces with 0
    

    hospital_records[patient_id] = {
        "Name": name,
        "Age": age,
        "Doctor": None,
        "Status": "Waiting"
    }

    print(f"{patient_id} added successfully.")



# VIEW PATIENTS


def view_patients():

    if not hospital_records:
        print("No patient records found.")
        return
# print details when patients records are available
    for patient_id, details in hospital_records.items():

        print("\n----------------------")
        print(f"Patient ID: {patient_id}")
        print(f"Name: {details['Name']}")
        print(f"Age: {details['Age']}")
        print(f"Doctor: {details['Doctor']}")
        print(f"Status: {details['Status']}")



# SEARCH PATIENT


def search_patient():

    name = input("Enter patient name: ").lower()
# Start by assuming you haven't found the patient yet
    found = False
# Goes through each record
    for patient_id, details in hospital_records.items():

        if name in details["Name"].lower():
#if name is found python executes true
            found = True
            
            print("\n----------------------")
            print(f"Patient ID: {patient_id}")
            print(f"Name: {details['Name']}")
            print(f"Age: {details['Age']}")
            print(f"Doctor: {details['Doctor']}")
            print(f"Status: {details['Status']}")

    if not found:
        print("Patient not found.")



# ASSIGN DOCTOR

def assign_doctor():

    patient_id = input("Enter Patient ID: ")

    if patient_id not in hospital_records:
        print("Patient not found.")
        return

    doctor = input("Enter doctor's name: ")

    hospital_records[patient_id]["Doctor"] = doctor
    #change 
    hospital_records[patient_id]["Status"] = "Under Treatment"

    print("Doctor assigned successfully.")

# ==========================
# DISCHARGE PATIENT
# ==========================

def discharge_patient():

    patient_id = input("Enter Patient ID: ")

    if patient_id not in hospital_records:
        print("Patient not found.")
        return

    patient = hospital_records[patient_id]

    if patient["Status"] != "Under Treatment":
        print("Patient must be under treatment first.")
        return
# change doctor to None once patient is discharged
    patient["Doctor"] = None
    patient["Status"] = "Discharged"

    print("Patient discharged successfully.")


# ==========================
# SUMMARY REPORT
# ==========================

def summary_report():
    waiting = 0
    treatment = 0
    discharged = 0

    for details in hospital_records.values():

        if details["Status"] == "Waiting":
            waiting += 1

        elif details["Status"] == "Under Treatment":
            treatment += 1

        elif details["Status"] == "Discharged":
            discharged += 1

    print("\n===== SUMMARY REPORT =====")
    print(f"Waiting Patients: {waiting}")
    print(f"Patients Under Treatment: {treatment}")
    print(f"Discharged Patients: {discharged}")

# STORING IT IN A FILE

def load_file():
#To tell python to work with our dictionary
    global hospital_records

    try:

        hospital_records = {}

        with open("patients.txt", "r") as file:
            for line in file:

                patient_id, name, age, doctor, status = line.strip().split(",")

                hospital_records[patient_id] = {
                    "Name": name,
                    "Age": int(age),
                    "Doctor": None if doctor == "None" else doctor,
                    "Status": status
                }

    except FileNotFoundError:
        pass
# MENU

while True:

    print("\n===== CLINIC MANAGEMENT SYSTEM =====")
    print("1. Add Patient")
    print("2. View Patients")
    print("3. Search Patient")
    print("4. Assign Doctor")
    print("5. Discharge Patient")
    print("6. Summary Report")
    print("7. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        add_patient()

    elif choice == "2":
        view_patients()

    elif choice == "3":
        search_patient()

    elif choice == "4":
        assign_doctor()

    elif choice == "5":
        discharge_patient()

    elif choice == "6":
        summary_report()

    elif choice == "7":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")