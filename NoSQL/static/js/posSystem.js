var productPrice = 0.00
var productQuantity = 0
var jsonObj;

$(document).ready(function() {
    var productTable = $('#dataTable').DataTable();

    $.ajax({
        type: "GET",
        url: "/getUser",
        data: {},
    }).done(function(result) {
        var jsonObj = JSON.parse(result)
        var staffName = jsonObj[0]["staffName"]
        $("#userFullName").html(staffName)
    })

    $.ajax({
        type: "GET",
        url: "/getItemStore",
        data: {},
    }).done(function(result) {
        jsonObj = JSON.parse(result)
        var productIndex = 0
        jsonObj.forEach(product => {
            productTable.row.add([product["itemName"], product["price"], product["quantity"], '<div class=\"d-flex justify-content-around\"><a onclick=\"purchase(' + productIndex + ')\"><i style=\"cursor:pointer\" class=\"fas fa-dollar-sign text-dark\"></i></a></div>']).draw(false);
            productIndex++
        });
    })
})

function chosenQuantityChange() {
    var chosenQuantity = document.getElementById("chosenQuantity").value
    var priceResult = parseFloat(productPrice * parseInt(chosenQuantity))
    $("#resultingPrice").html(priceResult)
}

function purchase(productIndex) {
    var productArr = jsonObj[productIndex]
    var productId = productArr["itemId"]
    var productName = productArr["itemName"]
    productPrice = parseFloat(productArr["price"])
    productQuantity = parseInt(productArr["quantity"])

    currentSelectedProduct = productId
    document.getElementById("productName").value = productName
    $("#productPrice").html(productPrice)

    var quantityOptions = ""
    for (var i = 1; i <= productQuantity; i++) {
        quantityOptions += "<option value=" + i + ">" + i + "</option>"
    }

    $("#resultingPrice").html(productPrice)
    $("#chosenQuantity").html(quantityOptions)
    $("#purchaseModal").modal("show")
}

function purchaseProduct() {
    var chosenQuantity = document.getElementById("chosenQuantity").value
    var resultingPrice = productPrice * parseInt(chosenQuantity)

    $.ajax({
        type: "POST",
        url: "/createTransaction",
        data: {
            itemId: currentSelectedProduct,
            chosenQuantity: chosenQuantity,
            originalQuantity: productQuantity,
            resultingPrice: resultingPrice
        },
    }).done(function(result) {
        if (result == 1) {
            alert("Transaction Successful!")
            $("#purchaseModal").modal("hide")
        } else {
            alert("Transaction Error Occurred")
        }
    })
}

$("#purchaseModal").on("hidden.bs.modal", function() {
    window.location.reload()
});