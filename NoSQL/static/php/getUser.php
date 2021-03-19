<?php
require('connection.php');

$staffId = $_COOKIE["staffId"];

$sqlQuery = $conn->prepare("SELECT staffName, mobileNum FROM staff WHERE staffId = ?");
$sqlQuery->bind_param("i", $staffId);
$sqlQuery->execute();
$result = $sqlQuery->get_result();
if ($result->num_rows > 0) {

    // output data of each row  
    while ($row = $result->fetch_assoc()) {
        $data[] = $row;
    }
    
    echo json_encode($data);
}
else{
    echo 0;
}
$conn->close();

?>