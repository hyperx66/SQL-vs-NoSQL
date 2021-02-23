$(document).ready(function() {
    $.ajax({
        type: "GET",
        url: "./php/newsletter.php",
        data: {},
    }).done(function(result) {
        var roleOptions = ""
        jsonObj = JSON.parse(result)
        jsonObj.forEach(row => {
            roleOptions += "<option value=\"" + row["rowId"] + "\">" + row["roleName"] + "</option>"
        });
        $("#accountType").html(roleOptions)
    });
});

function registerUser() {

}