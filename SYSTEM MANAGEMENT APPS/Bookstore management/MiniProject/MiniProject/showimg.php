<?php
require_once "connection.php";

$id=$_GET['id']??NULL;

$query = $link->prepare('SELECT * FROM `books` WHERE `book_id`= ?');
$query -> bind_param("i", $id);

if($query->execute()){
    //If Query has A Result
    $res = $query->get_result();
    $row = mysqli_fetch_array($res);

    $imgdata = $row['image'];

    header("content-type: image/PNG");
    echo $imgdata;

}

?>