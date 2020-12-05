/* Alert timeout
Aparted from https://stackoverflow.com/questions/50365291/auto-closing-bootstrap-alerts-after-form-submission */

window.setTimeout(function() {
    $(".alert").fadeTo(3000, 10000).slideUp(500, function() {
        $(this).hide();
    }); 10000
    });