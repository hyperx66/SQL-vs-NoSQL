$(document).ready(function() {
    $.ajax({
        type: "GET",
        url: "./assets/php/getUser.php",
        data: {},
    }).done(function(result) {
        var jsonObj = JSON.parse(result)
        var staffName = jsonObj[0]["staffName"]
        $("#userFullName").html(staffName)
    })

    $.ajax({
        type: "GET",
        url: "./assets/php/getItemStore.php",
        data: {},
    }).done(function(result) {
        var jsonObj = JSON.parse(result)
        jsonObj.forEach(product => {
            //insert product into table
        });
    })
})