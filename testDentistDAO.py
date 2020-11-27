from DentistDAO import dentistDAO

# Create.
latestid = dentistDAO.create(('Victor Hugo', 'general dentist', '120/M'))
print(f"New dentist was added to the records")

# Get All.
returnValue = dentistDAO.get_all()
print(f"All dentists {returnValue}")

# Find by ID.
returnValue = dentistDAO.find_by_dentistId(latestid)
print(f"Found by id {returnValue}")

# Update.
returnValue = dentistDAO.update(('Victor Hugo', 'endodontist', '120/M', latestid))
print(f"Updated {latestid}")

# Delete.
returnValue = dentistDAO.delete(latestid)
print(f"Deleted {latestid}")

# Get All dentist again.
returnValue = dentistDAO.get_all()
print(f"All dentists {returnValue}")