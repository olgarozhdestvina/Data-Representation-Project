// PATIENT JS.

// Visability of elements for viewing patients.
function showViewAll() {
    document.getElementById('showCreateButton').style.display = "block"
    document.getElementById('patientTable').style.display = "block"
    document.getElementById('createUpdateForm').style.display = "none"
    document.getElementById('divForTable').style.display = "block"
}

// Visability of elements when creating a new patient.
function showCreate() {
    // Load background API image.
    unsplash_API_images();
    // Table and form.
    document.getElementById('patientTable').style.display = "none"
    document.getElementById('createUpdateForm').style.display = "block"
    document.getElementById('divForTable').style.display = "none"
    // Labels.
    document.getElementById('createLabel').style.display = "inline"
    document.getElementById('updateLabel').style.display = "none"
    // Buttons.
    document.getElementById('showCreateButton').style.display = "none"
    document.getElementById('doCreateButton').style.display = "inline"
    document.getElementById('goBackButton').style.display = "inline"
    document.getElementById('doUpdateButton').style.display = "none"
    
}

// Visability of elements when updating a patient.
function showUpdate(buttonElement) {
    // Load background API image.
    unsplash_API_images();
    // Table and form.
    document.getElementById('patientTable').style.display = "none"
    document.getElementById('createUpdateForm').style.display = "block"
    document.getElementById('divForTable').style.display = "none"
    // Labels.
    document.getElementById('createLabel').style.display = "none"
    document.getElementById('updateLabel').style.display = "inline"
    // Buttons.
    document.getElementById('showCreateButton').style.display = "none"
    document.getElementById('doCreateButton').style.display = "none"
    document.getElementById('doUpdateButton').style.display = "inline"
    document.getElementById('goBackButton').style.display = "inline"
    // Populating form with patient information.
    var rowElement = buttonElement.parentNode.parentNode
    var patient = getPatientFromRow(rowElement)
    populateFormWithPatient(patient)
}

// Go back button.
// adapted from https://stackoverflow.com/questions/26517974/javascript-redirect-not-working-anyway/26518061#26518061
function goBack() {
    window.location = '/login/patient_database';
    return false;
}

// Create.
function doCreate() {
    var form = document.getElementById('createUpdateForm')
    var patient = {}
    patient.patientName = form.querySelector('input[name="patientName"]').value
    patient.phone = form.querySelector('input[name="phone"]').value
    patient.dentistId = form.querySelector('select[name="dentistId"]').value
    // console.log(JSON.stringify(patient))
    createPatientAjax(patient)
}

// Update.
function doUpdate() {
    var patient = getPatientFromForm();
    document.getElementById(patient.patientId);
    updatePatientAjax(patient);
    clearForm();
    showViewAll();
}

// Delete.
function doDelete(r) {
    // Confirm with the user deletion of the requested entry.
    if (!confirm('Are you sure you want to delete this entry from the database?')) {
        return false;
    }
    var tableElement = document.getElementById('patientTable');
    var rowElement = r.parentNode.parentNode;
    var index = rowElement.rowIndex;
    deletePatientAjax(rowElement.getAttribute("patientId"));
    tableElement.deleteRow(index);
}

// Adding patient info to the table.
function addPatientToTable(patient) {
    var tableElement = document.getElementById('patientTable')
    var rowElement = tableElement.insertRow(-1)
    rowElement.setAttribute('patientId', patient.patientId)
    var cell1 = rowElement.insertCell(0);
    cell1.innerHTML = patient.patientId
    var cell2 = rowElement.insertCell(1);
    cell2.innerHTML = patient.patientName
    var cell3 = rowElement.insertCell(2);
    cell3.innerHTML = patient.phone
    var cell4 = rowElement.insertCell(3);
    cell4.innerHTML = patient.dentistId
    var cell5 = rowElement.insertCell(4);
    cell5.innerHTML = '<button onclick="showUpdate(this)">Update</button>'
    var cell6 = rowElement.insertCell(5);
    cell6.innerHTML = '<button class="delete-back" onclick=doDelete(this)>Delete</button>'
}

// Get patient info from the table.
function getPatientFromRow(rowElement) {
    var patient = {}
    patient.patientId = rowElement.getAttribute('patientId')
    patient.patientName = rowElement.cells[1].firstChild.textContent
    patient.phone = parseInt(rowElement.cells[2].firstChild.textContent, 10)
    return patient
}

// Populate the form with with inputted patient info.
function populateFormWithPatient(patient) {
    var form = document.getElementById('createUpdateForm')
    form.querySelector('input[name="patientId"]').disabled = true
    form.querySelector('input[name="patientId"]').value = patient.patientId
    form.querySelector('input[name="patientName"]').value = patient.patientName
    form.querySelector('input[name="phone"]').value = patient.phone
    form.querySelector('select[name="dentistId"]').value = patient.dentistId
    return patient
}

// Get patient info from the form.
function getPatientFromForm() {
    var form = document.getElementById('createUpdateForm')
    var patient = {}
    patient.patientId = form.querySelector('input[name="patientId"]').value
    patient.patientName = form.querySelector('input[name="patientName"]').value
    patient.phone = parseInt(form.querySelector('input[name="phone"]').value, 10)
    patient.dentistId = form.querySelector('select[name="dentistId"]').value
    // console.log(JSON.stringify(patient))
    return patient
}

// Populate the dropdown box with existing dentist IDs.
function addDentistIdToSelect(dentist) {
    var select = document.getElementById('dentistIds');
    var option = document.createElement("option");
    option.text = dentist.dentistId;
    select.add(option);
    select.options[0].selected="true";
}

// Clear form from inputs.
function clearForm() {
    var form = document.getElementById('createUpdateForm')
    form.querySelector('input[name="patientName"]').value = ''
    form.querySelector('input[name="phone"]').value = ''
    form.querySelector('select[name="dentistId"]').value = ''
}

// AJAX CALLS.
// For calls to work on PythonAnywhere.
host = window.location.origin
// Get all patients.
function getAllAjax() {
    $.ajax({
        "url": host+"/patients/",
        "method": "GET",
        "data": "",
        "dataType": "JSON",
        "error": function (xhr, status, error) {
            if (xhr.status == 404) {
                alert('Page is not found');
            } else if (xhr.status == 500) {
                alert('Internal Server Error.');
            } else if (error === 'parsererror') {
                alert('Requested JSON parse failed');
            } else if (error === 'timeout') {
                alert('Time out error');
            } else if (error === 'abort') {
                alert('Ajax request aborted');
            } else {
                alert('Uncaught Error.\n' + xhr.responseText + ' - Click \'OK\' and try to re-submit your entries');
            }
        },
        "success": function (result) {
            //console.log(result);
            for (patient of result) {
                addPatientToTable(patient);
            }
        }
    });
}

// Create a new patient.
function createPatientAjax(patient) {
    console.log(JSON.stringify(patient));
    $.ajax({
        "url": host+"/patients/",
        "method": "POST",
        "data": JSON.stringify(patient),
        "dataType": "JSON",
        contentType: "application/json; charset=utf-8",
        "error": function (xhr, status, error) {
            if (xhr.status == 404) {
                alert('Page is not found - Click \'OK\' and try to re-submit your entries.');
            } else if (xhr.status == 500) {
                alert('Check for empty entries - Click \'OK\' and try to re-submit your entries');
            } else if (error === 'parsererror') {
                alert('Requested JSON parse failed - Click \'OK\' and try to re-submit your entries');
            } else if (error === 'timeout') {
                alert('Time out error - Click \'OK\' and try to re-submit your entries');
            } else if (error === 'abort') {
                alert('Ajax request aborted - Click \'OK\' and try to re-submit your entries');
            }
            else {
                alert('Uncaught Error.\n' + xhr.responseText + ' - Click \'OK\' and try to re-submit your entries');
            }
        },
        "success": function (result) {
            //console.log(result);
            patient.patientId = result.patientId
            addPatientToTable(patient)
            clearForm()
            showViewAll()
        }
    });
}

// Update a patient.
function updatePatientAjax(patient) {
    console.log(JSON.stringify(patient));
    $.ajax({
        "url": host+"/patients/"+encodeURI(patient.patientId),
        "method": "PUT",
        "data": JSON.stringify(patient),
        "dataType": "JSON",
        contentType: "application/json; charset=utf-8",
        "error": function (xhr, status, error) {
            if (xhr.status == 404) {
                alert('Page is not found - Click \'OK\' and try to re-submit your entries.');
            } else if (xhr.status == 500) {
                alert('Check for empty entries - Click \'OK\' and try to re-submit your entries');
            } else if (error === 'parsererror') {
                alert('Requested JSON parse failed - Click \'OK\' and try to re-submit your entries');
            } else if (error === 'timeout') {
                alert('Time out error - Click \'OK\' and try to re-submit your entries');
            } else if (error === 'abort') {
                alert('Ajax request aborted - Click \'OK\' and try to re-submit your entries');
            }
            else {
                alert('Uncaught Error.\n' + xhr.responseText + ' - Click \'OK\' and try to re-submit your entries');
            }
        },
        "success": function (result) {
            console.log("AJAX UPDATE: " + JSON.stringify(patient));
        }
    });
}

// Delete a patient.
function deletePatientAjax(patientId) {
    //console.log(JSON.stringify('deleting '+patientId));
    $.ajax({
        "url": host+"/patients/"+encodeURI(patientId),
        "method": "DELETE",
        "data": "",
        "dataType": "JSON",
        contentType: "application/json; charset=utf-8",
        "error": function (xhr, status, error) {
            if (xhr.status == 404) {
                alert('Page is not found - Click \'OK\' and try to re-submit your entries.');
            } else if (xhr.status == 500) {
                alert('Internal Server Error - Click \'OK\' and try to re-submit your entries');
            } else if (error === 'parsererror') {
                alert('Requested JSON parse failed - Click \'OK\' and try to re-submit your entries');
            } else if (error === 'timeout') {
                alert('Time out error - Click \'OK\' and try to re-submit your entries');
            } else if (error === 'abort') {
                alert('Ajax request aborted - Click \'OK\' and try to re-submit your entries');
            }
            else {
                alert('Uncaught Error.\n' + xhr.responseText + ' - Click \'OK\' and try to re-submit your entries');
            }
        },
        "success": function (result) {
            // console.log(result);
        }
    });
}

// Get existing dentist IDs from the dentist table.
function getDentistIds() {
    $.ajax({
        "url": host+"/dentists/",
        "method": "GET",
        "data": "",
        "dataType": "JSON",
        "error": function (xhr, status, error) {
            if (xhr.status == 404) {
                alert('Page is not found');
            } else if (xhr.status == 500) {
                alert('Internal Server Error.');
            } else if (error === 'parsererror') {
                alert('Requested JSON parse failed');
            } else if (error === 'timeout') {
                alert('Time out error');
            } else if (error === 'abort') {
                alert('Ajax request aborted');
            } else {
                alert('Uncaught Error.\n' + xhr.responseText + ' - Click \'OK\' and try to re-submit your entries');
            }
        },
        "success": function (result) {
            //console.log(result);
            for (dentist of result) {
                // console.log(JSON.stringify(dentist.dentistId))
                addDentistIdToSelect(dentist);
            }
        }
    });
}

// Load background image for the form.
function unsplash_API_images() {
    $.getJSON('../../static/unsplash_images.json', function(data) {
        // add a background image to the body
        $('body').attr('style', 'background-image: url(' + data[3].urls.full + '); background-repeat: no-repeat; background-position: right;  background-size: cover;');
    });
}

// Get all patients on load.
getAllAjax();