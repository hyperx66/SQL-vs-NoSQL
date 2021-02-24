<?php
require('connection.php');

$storeId = $_COOKIE["storeId"];

$sqlQuery = $conn->prepare("SELECT store_itemID, itemId, quantity FROM store_item WHERE storeId = ?");
$sqlQuery->bind_param("i", $storeId);
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