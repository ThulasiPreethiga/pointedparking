<?php
$con = mysqli_connect("localhost","jerry","2308","mydb");

// Check connection
if (mysqli_connect_errno())
  {
  echo "Failed to connect to MySQL: " . mysqli_connect_error();
  }
$lot_id=$_GET['id'];
if(isset($_GET['id'])){
  $lot_id=$_GET['id'];
  $stmt = $con->prepare("select * from status_table where id =?");
  $stmt->bind_param('d',$lot_id);
  $stmt->execute();
  $row = mysqli_fetch_assoc($stmt->get_result());
  echo sizeof($row);
}
$con->close();
 ?>
