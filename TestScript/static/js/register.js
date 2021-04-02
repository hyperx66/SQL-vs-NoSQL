$(document).ready(function () {
    //Load All Roles
    $.ajax({
        type: "GET",
        url: "/getRoles",
        data: {},
    }).done(function (result) {
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
        url: "/getStores",
        data: {},
    }).done(function (result) {
        var storeOptions = ""
        jsonObj = JSON.parse(result)
        jsonObj.forEach(row => {
            storeOptions += "<option value=\"" + row["storeId"] + "\">" + row["storeName"] + "</option>"
        });
        $("#stores").html(storeOptions)
    });
});

function registerUser() {
    var role = document.getElementById("accountType").value
    var store = document.getElementById("stores").value
    var username = document.getElementById("username").value
    var password = document.getElementById("password").value
    var confirmPassword = document.getElementById("confirmPassword").value
    var fullName = document.getElementById("fullName").value
    var phoneNum = document.getElementById("phoneNum").value

    if (confirmPassword == password) {
        $.ajax({
            type: "POST",
            url: "/addUser",
            data: {
                username: username,
                password: password,
                staffName: fullName,
                mobileNum: phoneNum,
                store: store,
                role: role
            },
        }).done(function (result) {
            if (result == 1) {
                alert("Account creation successful")
                window.location.href = "./login"
            } else {
                alert("An error occurred. Please try again.")
            }
        });
    }
}