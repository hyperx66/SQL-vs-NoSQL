$(document).ready(function() {
    //Load All Roles
    $.ajax({
        type: "GET",
        url: "./assets/php/getRoles.php",
        data: {},
    }).done(function(result) {
        var roleOptions = ""
        jsonObj = JSON.parse(result)
        jsonObj.forEach(row => {
            roleOptions += "<option value=\"" + row["roleId"] + "\">" + row["roleName"] + "</option>"
        });
        $("#accountType").html(roleOptions)
    });

    //Load All Stores
    $.ajax({
        type: "GET",
        url: "./assets/php/getStores.php",
        data: {},
    }).done(function(result) {
        var storeOptions = ""
        jsonObj = JSON.parse(result)
        jsonObj.forEach(row => {
            storeOptions += "<option value=\"" + row["storeId"] + "\">" + row["storeName"] + "</option>"
        });
        $("#stores").html(storeOptions)
    });
});

function registerUser() {

}