function showCreate() {
    document.getElementById('showCreateButton').style.display = "none"
    document.getElementById('dentistTable').style.display = "none"
    document.getElementById('createUpdateForm').style.display = "block"

    document.getElementById('createLabel').style.display = "inline"
    document.getElementById('updateLabel').style.display = "none"

    document.getElementById('doCreateButton').style.display = "inline"
    document.getElementById('goBackButton').style.display = "inline"
    document.getElementById('doUpdateButton').style.display = "none"

}
function showViewAll() {
    document.getElementById('showCreateButton').style.display = "block"
    document.getElementById('dentistTable').style.display = "block"
    document.getElementById('createUpdateForm').style.display = "none"
}
function showUpdate(buttonElement) {
    document.getElementById('showCreateButton').style.display = "none"
    document.getElementById('dentistTable').style.display = "none"
    document.getElementById('createUpdateForm').style.display = "block"

    document.getElementById('createLabel').style.display = "none"
    document.getElementById('updateLabel').style.display = "inline"

    document.getElementById('doCreateButton').style.display = "none"
    document.getElementById('doUpdateButton').style.display = "inline"
    document.getElementById('goBackButton').style.display = "inline"

    var rowElement = buttonElement.parentNode.parentNode
    var dentist = getDentistFromRow(rowElement)
    populateFormWithDentist(dentist)
}
// adapted from https://stackoverflow.com/questions/26517974/javascript-redirect-not-working-anyway/26518061#26518061
function goBack() {
    window.location = '/';
    return false;
}

// Create.
function doCreate() {
    var form = document.getElementById('createUpdateForm')
    var dentist = {}
    dentist.dentistName = form.querySelector('input[name="dentistName"]').value
    dentist.position = form.querySelector('select[name="position"').value
    dentist.regNumber = form.querySelector('input[name="regNumber"]').value
    console.log(JSON.stringify(dentist))
    createDentistAjax(dentist)
}

// Update
function doUpdate() {
    var dentist = getDentistFromForm();
    document.getElementById(dentist.dentistId);
    updateDentistAjax(dentist);

    clearForm();
    showViewAll();
}
// Delete
function doDelete(r) {
    // Confirm with the user deletion of the requested entry.
    if (!confirm('Are you sure you want to delete this entry from the database?')) {
        return false;
    }
    var tableElement = document.getElementById('dentistTable');
    var rowElement = r.parentNode.parentNode;
    var index = rowElement.rowIndex;
    deleteDentistAjax(rowElement.getAttribute("dentistId"));
    tableElement.deleteRow(index);
}

function addDentistToTable(dentist) {
    var tableElement = document.getElementById('dentistTable')
    var rowElement = tableElement.insertRow(-1)
    rowElement.setAttribute('dentistId', dentist.dentistId)
    var cell1 = rowElement.insertCell(0);
    cell1.innerHTML = dentist.dentistId
    var cell2 = rowElement.insertCell(1);
    cell2.innerHTML = dentist.dentistName
    var cell3 = rowElement.insertCell(2);
    cell3.innerHTML = dentist.position
    var cell4 = rowElement.insertCell(3);
    cell4.innerHTML = dentist.regNumber
    var cell5 = rowElement.insertCell(4);
    cell5.innerHTML = '<button onclick="showUpdate(this)">Update</button>'
    var cell6 = rowElement.insertCell(5);
    cell6.innerHTML = '<button class="delete-back" onclick=doDelete(this)>Delete</button>'
}

function clearForm() {
    var form = document.getElementById('createUpdateForm')
    form.querySelector('input[name="dentistName"]').value = ''
    form.querySelector('select[name="position"]').value = ''
    form.querySelector('input[name="regNumber"]').value = ''
}
function getDentistFromRow(rowElement) {
    var dentist = {}
    dentist.dentistId = rowElement.getAttribute('dentistId')
    dentist.dentistName = rowElement.cells[1].firstChild.textContent
    dentist.position = rowElement.cells[2].firstChild.textContent
    dentist.regNumber = rowElement.cells[3].firstChild.textContent
    return dentist
}
function populateFormWithDentist(dentist) {
    var form = document.getElementById('createUpdateForm')
    form.querySelector('input[name="dentistId"]').disabled = true

    form.querySelector('input[name="dentistId"]').value = dentist.dentistId
    form.querySelector('input[name="dentistName"]').value = dentist.dentistName
    form.querySelector('select[name="position"]').value = dentist.position
    form.querySelector('input[name="regNumber"]').value = dentist.regNumber
    return dentist
}
function getDentistFromForm() {
    var form = document.getElementById('createUpdateForm')
    var dentist = {}
    dentist.dentistId = form.querySelector('input[name="dentistId"]').value
    dentist.dentistName = form.querySelector('input[name="dentistName"]').value
    dentist.position = form.querySelector('select[name="position"]').value
    dentist.regNumber = form.querySelector('input[name="regNumber"]').value
    console.log(JSON.stringify(dentist))
    return dentist
}
function getAllAjax() {
    $.ajax({
        "url": "http://127.0.0.1:5000/dentists",
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
                addDentistToTable(dentist);
            }
        }
    });
}
function createDentistAjax(dentist) {
    console.log(JSON.stringify(dentist));
    $.ajax({
        "url": "http://127.0.0.1:5000/dentists",
        "method": "POST",
        "data": JSON.stringify(dentist),
        "dataType": "JSON",
        contentType: "application/json; charset=utf-8",
        "success": function (result) {
            //console.log(result);
            dentist.dentistId = result.dentistId
            addDentistToTable(dentist)
            clearForm()
            showViewAll()
        },
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
        }
    });
}
function updateDentistAjax(dentist) {
    console.log(JSON.stringify(dentist));
    $.ajax({
        "url": "http://127.0.0.1:5000/dentists/" + encodeURI(dentist.dentistId),
        "method": "PUT",
        "data": JSON.stringify(dentist),
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
            // console.log(result);
        }
    });
}
function deleteDentistAjax(dentistId) {
    $.ajax({
        "url": "http://127.0.0.1:5000/dentists/" + encodeURI(dentistId),
        "method": "DELETE",
        "data": "",
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
            // console.log(result);
        }
    });
}
getAllAjax();