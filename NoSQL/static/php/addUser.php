<?php
require('connection.php');

$username = $_POST["username"];
$password = $_POST["password"];
$staffName = $_POST["staffName"];
$mobileNum = $_POST["mobileNum"];
$storeId = $_POST["store"];
$role = $_POST["role"];
$currentDateTime = date("Y-m-d H:m:s");

$userId = 0;

$preparedStatement = $conn->prepare("INSERT INTO staff(staffName,mobileNum, storeId, role, createdDate, updatedDate) VALUES(?,?,?,?,?,?)");
$preparedStatement->bind_param("siiiss", $staffName, $mobileNum, $storeId, $role, $currentDateTime, $currentDateTime);
if($preparedStatement->execute()){
    $userId = $conn->insert_id;
    $preparedStatement = $conn->prepare("INSERT INTO login(loginUsername,loginPassword, loginUser) VALUES(?,?,?)");
    $preparedStatement->bind_param("ssi", $username, $password, $userId);
    if($preparedStatement->execute()){
        echo 1;
    }
    else{
        echo 0;
    }
}
else{
    echo 0;
}
$conn->close();