<?php
//    if($_REQUEST){
        require_once "connection.php";


        $query = $link->prepare('SELECT * FROM `users` WHERE `email` = (?)');
        $query -> bind_param("s", $_COOKIE['email']);
        $query->execute();
        $res = $query->get_result();
        $row = mysqli_fetch_array($res);
        $reciverid = $row['user_id'];

        $query_extract_chats = $link->prepare('SELECT `sender_id`,`reciver_id`,`time`,`message` FROM `chat` WHERE `sender_id` = (?) AND `reciver_id` = (?) OR `sender_id` = (?) AND `reciver_id` = (?)');
        $query_extract_chats -> bind_param("iiii",$_COOKIE['sender_id'], $reciverid,$reciverid,$_COOKIE['sender_id']);

            


        if($query_extract_chats->execute()){
            $res_query_extract_chats = $query_extract_chats->get_result();
            $row = mysqli_fetch_array($res_query_extract_chats);
            $callback['result'] = $row;
        }
        else{
            $callback["result"] = "-1";
        }
        echo json_encode($callback);
    // }

?>