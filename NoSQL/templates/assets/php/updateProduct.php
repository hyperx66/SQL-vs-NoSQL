<?php
require('connection.php');

$itemId = $_POST["itemId"];
$productName = $_POST["productName"];
$productPrice = $_POST["productPrice"];
$productQuantity = $_POST["productQuantity"];
$storeId = $_COOKIE["storeId"];

$preparedStatement = $conn->prepare("UPDATE item SET itemName = ?, price = ? WHERE itemId = ?");
$preparedStatement->bind_param("sdi", $productName, $productPrice, $itemId);
if($preparedStatement->execute()){
    $preparedStatement = $conn->prepare("UPDATE store_item SET quantity = ? WHERE itemId = ? AND storeId = ?");
    $preparedStatement->bind_param("iii", $productQuantity, $itemId, $storeId);
    if($preparedStatement->execute()){
        echo 1;
    }
    else{
        echo 2;
    }
}
else{
    echo 0;
}