<?php
   if($_REQUEST){
        require_once "connection.php";


        $query = $link->prepare('SELECT * FROM `users` WHERE `email` = (?)');
        $query -> bind_param("s", $_COOKIE['email']);
        $query->execute();
        $res = $query->get_result();
        $row = mysqli_fetch_array($res);
        $senderid = $row['user_id'];

        $reciverid =  $_COOKIE['sender_id'];
        date_default_timezone_set('Asia/Kolkata');
        $time = date("h:i:sa");
        $message = $_REQUEST['message'];
        
       

        $query_update_chat = $link->prepare('INSERT INTO `chat` (`sender_id`,`reciver_id`,`time`,`message`) VALUES (?,?,?,?)');
        $query_update_chat->bind_param("iiss",$senderid,$reciverid,$time,$message);
        if($query_update_chat->execute()){
            $callback["result"] = "1";
        }
        else{
            $callback["result"] = "-1";
        }
        echo json_encode($callback);
    }

?>