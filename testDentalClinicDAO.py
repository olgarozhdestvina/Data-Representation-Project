from DentalClinicDAO import dentalClinicDAO

# DENTISTS
# Create.
def check_dentists():
    print("DENTISTS")
    latest_dentist_id = dentalClinicDAO.create_dentist(('Victor Hugo', 'General Dentist', '120/M'))
    print(f"New dentist was added to the records")

    # Get All.
    returnValue = dentalClinicDAO.get_all_dentists()
    print(f"All dentists {returnValue}")

    # Find by ID.
    returnValue = dentalClinicDAO.find_by_dentistId(latest_dentist_id)
    print(f"Found by id {returnValue}")

    # Update.
    returnValue = dentalClinicDAO.update_dentist(('Victor Hugo', 'endodontist', '120/M', latest_dentist_id))
    print(f"Updated dentist with id {latest_dentist_id}")

    # Delete.
    returnValue = dentalClinicDAO.delete_dentist(latest_dentist_id)
    print(f"Deleted dentist with id {latest_dentist_id}")

    # Get All dentist again.
    returnValue = dentalClinicDAO.get_all_dentists()
    print(f"All dentists {returnValue} \n\n\n")


# PATIENTS
def check_patients():
    print("PATIENTS")
    # Create.
    latest_patient_id  = dentalClinicDAO.create_patient(('Caroline Smith', '0872239565', None))
    print(f"New patient was added to the records")

    # Get All.
    returnValue = dentalClinicDAO.get_all_patients()
    print(f"All patients {returnValue}")

    # Find by ID.
    returnValue = dentalClinicDAO.find_by_patientId(latest_patient_id)
    print(f"Found by id {returnValue}")

    # Update.
    returnValue = dentalClinicDAO.update_patient(('Caroline Spillane', '0892239568', None, latest_patient_id))
    print(f"Updated patient with id {latest_patient_id}")

    # Delete.
    returnValue = dentalClinicDAO.delete_patient(latest_patient_id)
    print(f"Deleted patient with id {latest_patient_id}")

    # Get All dentist again.
    returnValue = dentalClinicDAO.get_all_patients()
    print(f"All patients {returnValue}")

    

check_dentists()
check_patients()
