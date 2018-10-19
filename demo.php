<?php
$con = mysqli_connect("localhost","jerry","2308","mydb");

// Check connection
if (mysqli_connect_errno())
  {
  echo "Failed to connect to MySQL: " . mysqli_connect_error();
  }
$lot_id=$_POST['id'];
if (isset($_POST['booked'])) {
  $status = 'booked';
    $stmt = $con->prepare("INSERT INTO status_table (id, status) VALUES (?, ?)");
    $stmt->bind_param('ds',$lot_id, $status);
    $stmt->execute();
}elseif (isset($_POST['park'])) {
  $stmt = $con->prepare("update status_table set status='parked' where id=?");
  $stmt->bind_param('d',$lot_id);
  $stmt->execute();
}else {
  $stmt = $con->prepare("DELETE FROM status_table where id= ?");
  $stmt->bind_param('d',$lot_id);
  $stmt->execute();
}
$con->close();
?>
