# SQL-vs-NoSQL
This project is aimed at deducing which type of databases is better by comparing the time required to execute a query. In this experiment, we look at SQL and NoSQL databases in a setting where a shop that sells apparels would need to track their inventory as well as execute transactions.

## Roles:
Executive - Executive are allowed to enter the POS system to perform transactions and additionally, they are given the permission to enter the Product Management System to alter the inventory in the event new stocks arrive.

Manager - Managers are allowed to enter the POS system to perform transactions and additionally, they are given the permission to enter the Product Management System to alter the inventory in the event new stocks arrive.

Staff - Staff's are given the permission to enter the POS system to perform transactions in the event a customer decides to make a purchase.


# SQL
The SQL version was setup using MySQL with PHP to call the database and perform queries and afterwards all the data will be parsed to the HTML page through jQuery.

## Initialising connection:
Here we start the connection to the database and leave it as a variable to be called by other PHP files when called using "require". As the files will be uploaded to the file server, the servername will be maintained as "localhost" and the necessary credentials are then supplied to start the connection.
```
<?php

$servername = "localhost";
$database = "id16214262_dbproject";
$username = "id16214262_root";
$password = "B|w0O{0(q~+^\-}(";

// Create connection
$conn = new mysqli($servername, $username, $password, $database);
// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}


// Check connection
if (!$conn) {
    die("Connection failed: " . mysqli_connect_error());
} 
```

## Prepared Statement:
Each query is done using prepared statement and this allows us to ensure that all variables are parsed according to it's datatype correctly. In this experiment we have utilised the identifier "i" for integer, "d" for decimal and "s" for string. The advantage of using prepared statements is that it helps mitigate against SQL injection however, as some fields are strings, SQL injection can still occur but if paired with sanitization, it would be theoretically hard for anyone to perfomr SQL injection.
```
$sqlQuery = $conn->prepare("SELECT i.itemId, i.itemName, i.price, si.quantity FROM store_item si INNER JOIN item i ON si.itemId = i.itemId WHERE si.storeId = ?");
$sqlQuery->bind_param("i", $storeId);
$sqlQuery->execute();
```

## Parsing data to JSON:
After retrieving the rows from the database according to the query, we parse each row as a dictionary array and JSON encode it to be echoed later.
```
$result = $sqlQuery->get_result();
if ($result->num_rows > 0) {

    // output data of each row  
    while ($row = $result->fetch_assoc()) {
        $data[] = $row;
    }
    
    echo json_encode($data);
}
```

## Closing Connection:
After executing all the queries. We ensure that the connection is closed so that the connection cannot be hijacked for any reason.
```
$conn->close();
```

# NoSQL
