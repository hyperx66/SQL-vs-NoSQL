function login() {
    var username = document.getElementById("username").value
    var password = document.getElementById("password").value

    $.ajax({
        type: "GET",
        url: "./assets/php/login.php",
        data: {
            username: username,
            password: password,
        },
    }).done(function(result) {
        var jsonObj = JSON.parse(result)
        var roleType = jsonObj[0]["role"]
        var staffId = jsonObj[0]["staffId"]
        var uiLogin = document.getElementById("redirectPage").value

        document.cookie = "staffId=" + staffId + "; expires=Sun, 18 Dec 2022 12:00:00 UTC";

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