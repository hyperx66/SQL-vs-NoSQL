<?php
require('connection.php');

$itemId = $_POST["itemId"];
$chosenQuantity = $_POST["chosenQuantity"];
$originalQuantity = $_POST["originalQuantity"];
$resultingPrice = $_POST["resultingPrice"];
$storeId = $_COOKIE["storeId"];
$staffId = $_COOKIE["staffId"];
$currentDateTime = date("Y-m-d H:m:s");

//Insert into the transaction first
$insertTransaction = $conn-> prepare("INSERT INTO transaction(transactionBy,storeId,itemPurchased,quantityPurchased,price,datePurchased) VALUES(?,?,?,?,?,?)");
$insertTransaction->bind_param("iiiids", $staffId, $storeId, $itemId, $chosenQuantity, $resultingPrice, $currentDateTime);
if($insertTransaction->execute()){

    //Update quantity of the store
    $newQuantity = $originalQuantity - $chosenQuantity;
    $updateQuantity = $conn-> prepare("UPDATE store_item SET quantity = ? WHERE storeId = ? AND itemId = ?");
    $updateQuantity->bind_param("iii", $newQuantity, $storeId, $itemId);
    
    if($updateQuantity->execute()){
        echo 1;
    }
    else{
        echo 0;
    }
}
else{
    echo 0;
}

