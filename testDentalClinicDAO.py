# Test of DentalClinicDAO.

from main.DentalClinicDAO import dentalClinicDAO

# DENTISTS.
def check_dentists():
    print("DENTISTS")

    # Create two dentists.
    dentalClinicDAO.create_dentist(('Max Smith', 'General Dentist', '120/M'))
    latest_dentist_id = dentalClinicDAO.create_dentist(
        ('Victor Hugo', 'Implantologist', '34/6M'))
    print(f"New dentists were added to the records")

    # Get All.
    returnValue = dentalClinicDAO.get_all_dentists()
    print(f"All dentists {returnValue}")

    # Find by ID.
    returnValue = dentalClinicDAO.find_by_dentistId(latest_dentist_id)
    print(f"Found by id {returnValue}")

    # Update.
    returnValue = dentalClinicDAO.update_dentist(
        ('Victor Hugo', 'Endodontist', '34/6M', latest_dentist_id))
    print(f"Updated dentist with id {latest_dentist_id}")

    # Delete.
    returnValue = dentalClinicDAO.delete_dentist(latest_dentist_id)
    print(f"Deleted dentist with id {latest_dentist_id}")

    # Get All dentist again.
    returnValue = dentalClinicDAO.get_all_dentists()
    print(f"All dentists {returnValue} \n\n\n")

# PATIENTS.
def check_patients():
    print("PATIENTS")

    # Create.
    latest_patient_id = dentalClinicDAO.create_patient(
        ('Caroline Smith', '0872239565', 1))
    print(f"New patient was added to the records")

    # Get All.
    returnValue = dentalClinicDAO.get_all_patients()
    print(f"All patients {returnValue}")

    # Find by ID.
    returnValue = dentalClinicDAO.find_by_patientId(latest_patient_id)
    print(f"Found by id {returnValue}")

    # Update.
    returnValue = dentalClinicDAO.update_patient(
        ('Caroline Spillane', '0892239568', 1, latest_patient_id))
    print(f"Updated patient with id {latest_patient_id}")

    # Delete.
    returnValue = dentalClinicDAO.delete_patient(latest_patient_id)
    print(f"Deleted patient with id {latest_patient_id}")

    # Get All dentist again.
    returnValue = dentalClinicDAO.get_all_patients()
    print(f"All patients {returnValue}")


# Call the functions.
check_dentists()
check_patients()