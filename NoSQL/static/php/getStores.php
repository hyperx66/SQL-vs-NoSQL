<?php
require('connection.php');

$sqlQuery = "SELECT storeId, storeName FROM store";

$result = $conn->query($sqlQuery);
if ($result->num_rows > 0) {
    // output data of each row
    while ($row = $result->fetch_assoc()) {
        $data[] = $row;
    }
}

echo json_encode($data);
$conn->close();
?>