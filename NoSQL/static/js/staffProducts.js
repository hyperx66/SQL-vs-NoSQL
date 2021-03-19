var jsonObj;
var currentSelectedProduct = 0

$(document).ready(function() {
    var productTable = $('#dataTable').DataTable();

    $.ajax({
        type: "GET",
        url: "./assets/php/getUser.php",
        data: {},
    }).done(function(result) {
        var jsonObj = JSON.parse(result)
        var staffName = jsonObj[0]["staffName"]
        $("#staffLogin").html(staffName)
    })

    $.ajax({
        type: "GET",
        url: "./assets/php/getItemStore.php",
        data: {},
    }).done(function(result) {
        jsonObj = JSON.parse(result)
        var productIndex = 0
        jsonObj.forEach(product => {
            productTable.row.add([product["itemName"], product["price"], product["quantity"], '<div class=\"d-flex justify-content-around\"><a onclick=\"info(' + productIndex + ')\"><i style=\"cursor:pointer\" class=\"fas fa-info-circle text-dark\"></i></a></div>']).draw(false);
            productIndex++
        });
    })
})

function info(productIndex) {
    var productArr = jsonObj[productIndex]
    var productId = productArr["itemId"]
    var productName = productArr["itemName"]
    var productPrice = productArr["price"]
    var productQuantity = productArr["quantity"]

    currentSelectedProduct = productId
    document.getElementById("productName").value = productName
    document.getElementById("productPrice").value = productPrice
    document.getElementById("productQuantity").value = productQuantity

    $("#detailModal").modal("show")
}

function updateProduct() {
    var productName = document.getElementById("productName").value
    var productPrice = document.getElementById("productPrice").value
    var productQuantity = document.getElementById("productQuantity").value

    $.ajax({
        type: "POST",
        url: "./assets/php/updateProduct.php",
        data: {
            itemId: currentSelectedProduct,
            productName: productName,
            productPrice: productPrice,
            productQuantity: productQuantity
        },
    }).done(function(result) {
        if (result == 1) {
            alert("Product successfully updated")
            $("#detailModal").modal("hide")
        } else {
            alert("There was an error updating the product, please try again.")
        }
    })
}

$("#detailModal").on("hidden.bs.modal", function() {
    window.location.reload()
});