from DentistDAO import dentistDAO

dentist1 = {
    'dentistName': 'Victor Hugo', 
    'position': 'general dentist',
    'regNumber': '120/M'
}

dentist2 = {
    'dentistName': 'Victor Hugo', 
    'position': 'endodontist',
    'regNumber': '120/M'
}

# Create.
latestid = dentistDAO.create(dentist1)
print(f"New dentist was added to the records")

# Get All.
returnValue = dentistDAO.get_all()
print(f"All dentists {returnValue}")

# Find by ID.
returnValue = dentistDAO.find_by_dentistId()
print(f"Found by id {returnValue}")

# Update.
returnValue = dentistDAO.update(dentist2)
print(f"Updated {returnValue}")

# Delete.
returnValue = dentistDAO.delete()
print(f"Deleted {returnValue}")
