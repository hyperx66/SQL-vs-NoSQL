<?php
require('connection.php');

$staffName = $_GET["staffName"];
$mobileNum = $_GET["mobileNum"];
$storeId = $_GET["storeId"];
$role = $_GET["role"];
$currentDateTime = date("Y-m-d H:m:s");

$preparedStatement = $conn->prepare("INSERT INTO staff(staffName,mobileNum, storeId, role, createdDate, updatedDate) VALUES(?,?,?,?,?,?)");
$preparedStatement->bind_param("siiss", $staffName, $mobileNum, $storeId, $role, $currentDateTime, $currentDateTime);