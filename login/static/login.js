// Remember user's name and password
// Adapted from https://forums.caspio.com/topic/8448-add-a-checkbox-remember-me/
$(function() {
 
    if (localStorage.chkbx && localStorage.chkbx != '') {
        $('#remember_me').attr('checked', 'checked');
        $('#user_name').val(localStorage.usrname);
        $('#user_password').val(localStorage.pass);
    } else {
        $('#remember_me').removeAttr('checked');
        $('#user_name').val('');
        $('#user_password').val('');
    }

    $('#remember_me').click(function() {

        if ($('#remember_me').is(':checked')) {
            // save username and password
            localStorage.usrname = $('#user_name').val();
            localStorage.pass = $('#user_password').val();
            localStorage.chkbx = $('#remember_me').val();
        } else {
            localStorage.usrname = '';
            localStorage.pass = '';
            localStorage.chkbx = '';
        }
    });
});