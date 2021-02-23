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
//echo "Connected successfully";