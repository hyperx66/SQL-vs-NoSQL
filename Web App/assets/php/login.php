<?php
require('connection.php');

$username = $_GET["username"];
$password = $_GET["password"];
$currentDateTime = date("Y-m-d H:m:s");

//Retrieve user details
$sqlQuery = $conn->prepare("SELECT staffId, role FROM staff INNER JOIN login ON staff.staffId = login.loginUser WHERE login.loginUsername = ? AND login.loginPassword = ?");
$sqlQuery->bind_param("ss", $username, $password);
$sqlQuery->execute();
$result = $sqlQuery->get_result();
if ($result->num_rows > 0) {

    // output data of each row  
    while ($row = $result->fetch_assoc()) {
        $data[] = $row;
    }

    //Update last login of login table
    $sqlQuery = $conn->prepare("UPDATE login SET lastLogin = ? WHERE login.loginUsername = ? AND login.loginPassword = ?");
    $sqlQuery->bind_param("sss", $currentDateTime,$username, $password);
    $sqlQuery->execute();
    
    echo json_encode($data);
}
else{
    echo 0;
}
$conn->close();

?>