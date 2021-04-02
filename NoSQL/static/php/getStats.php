<?php
require('connection.php');

$storeId = $_COOKIE["storeId"];

$currentYear = idate("Y");

$sqlQuery = $conn->prepare("select year(datePurchased) AS year,
month(datePurchased) as month,
COALESCE(sum(price),0) as earnings, 
count(transactionId) as transactions from transaction where storeId = ? AND 
year(datePurchased) = ? group by year(datePurchased),month(datePurchased) order by year(datePurchased),month(datePurchased)");
$sqlQuery->bind_param("is", $storeId, $currentYear);
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
