function login() {
    var username = document.getElementById("username").value
    var password = document.getElementById("password").value

    $.ajax({
        type: "POST",
        url: "/loginUser",
        data: {
            username: username,
            password: password,
        },
    }).done(function(result) {
        var jsonObj = JSON.parse(result)
        console.log("login.js LOG: " + jsonObj)

        var roleType = jsonObj["role"]
        var staffId = jsonObj["staffId"]
        var storeId = jsonObj["storeId"]
        var uiLogin = document.getElementById("redirectPage").value

        document.cookie = "staffId=" + staffId + "; expires=Sun, 18 Dec 2022 12:00:00 UTC";
        document.cookie = "storeId=" + storeId + "; expires=Sun, 18 Dec 2022 12:00:00 UTC";

        if (roleType == 1) {
            if (uiLogin == "pos") {
                window.location.href = "./posDashboard.html"
            } else if (uiLogin == "pms") {
                alert("You are not allowed to enter this system please choose a different system.")
            } else {
                alert("Please choose a system to log into.")
            }
        } else if (roleType == 2) {
            if (uiLogin == "pos") {
                window.location.href = "./posDashboard.html"
            } else if (uiLogin == "pms") {
                window.location.href = "./staffDashboard.html"
            } else {
                alert("Please choose a system to log into.")
            }
        } else if (roleType == 3) {
            if (uiLogin == "pos") {
                window.location.href = "./posDashboard.html"
            } else if (uiLogin == "pms") {
                window.location.href = "./staffDashboard.html"
            } else {
                alert("Please choose a system to log into.")
            }
        }
    });
}