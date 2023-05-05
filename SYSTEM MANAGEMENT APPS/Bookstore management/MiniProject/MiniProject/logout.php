<?php
    setcookie("email", "", time() - 1);
    setcookie("___manage__req", "", time() - 1);
    setcookie("sender_id","", time() - 1);
    setcookie("bookid", "", time() - 1);
    setcookie("reciver_id", "", time() - 1);
    header("Location: login.php");
?>  