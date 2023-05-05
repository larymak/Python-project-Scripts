<?php
    if(!isset($_COOKIE["email"])){
        header('Location: login.php');                                           
    }
    // error_reporting(0);
    require_once "connection.php";
    $query = $link->prepare('SELECT * FROM `users` WHERE `email` = (?)');
    $query -> bind_param("s", $_COOKIE['email']);
    $query->execute();
    $res = $query->get_result();
    $row = mysqli_fetch_array($res);
    $uid = $row['user_id'];

    $senderid = $_COOKIE['sender_id'];
    $reciverid = $uid;

    $query_extract_chats = $link->prepare('SELECT * FROM `chat` WHERE `sender_id` = (?) AND `reciver_id` = (?) OR `sender_id` = (?) AND `reciver_id` = (?)');
    $query_extract_chats -> bind_param("iiii", $senderid,$reciverid,$reciverid,$senderid);
    $query_extract_chats->execute();
    $res_query_extract_chats = $query_extract_chats->get_result();
    // $all_chat = mysqli_fetch_array($res_query_extract_chats);
    // print_r($all_chat);
?>

<!doctype html>
<html lang="en">
    <head>
        <!-- Required meta tags -->
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">

        <!-- Bootstrap CSS -->
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
        
        <!-- Site Icon -->
        <link rel="icon" href="Resources/A-Dot-Icon.png">
        <!-- Custom Css -->

        <link href="css/style.css" rel="stylesheet">
        <link href="css/headermenu.css" rel="stylesheet">
        <!-- jQuery Link -->
        <?php
            include('logo.php')
        ?>
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>
      
        
        <title>Dashboard</title>
    </head>
    <body>
   
        <?php
            include('headermenu.php')
        ?>
        <script>
            $("#chat-link").addClass('active')
        </script>
        <br><br><br>
        <div class="container-fluid chat-bod-pc">
            <div class="row">
                <div class="col">
                    <?php
                        $query = $link->prepare('SELECT * FROM `users` WHERE `user_id` = (?)');
                        $query -> bind_param("s", $_COOKIE['sender_id']);
                        $query->execute();
                        $res = $query->get_result();
                        $row = mysqli_fetch_array($res); 
                        
                    ?>
                    <h1 class="display-6 topbar"><a class="back-btn" href="index.php">&#8592;</a><?=$row['email']?></h1>
                </div>
            </div>
            <div class="row">
                <div class="col display">
                    <?php
                        while ($all_chat = mysqli_fetch_array($res_query_extract_chats)) {
                            if($all_chat['sender_id'] == $_COOKIE['sender_id']){
                                ?>
                                <div class="container recived-message">
                                    <p style="font-size: 20px;"><?=$all_chat['message']?> <span style="font-size: 8px;"><?=$all_chat['time']?></span></p>
                                </div>
                                <?php
                            }
                            else{
                                ?>
                                <div class="container send-message">
                                    <p style="font-size: 20px;"><?=$all_chat['message']?> <span style="font-size: 8px;"><?=$all_chat['time']?></span></p>     
                                </div>
                                <?php
                            }
                        }
                    ?>   
                   
                </div>
            </div>
  
            <div class="row">
                <div class="col-10">
               
                    <input type="text" class="form-control" id="messp" placeholder="Message..">
                
                </div>
                <div class="col-2">
                    <button type="button" class="btn btn-success" id="sendp">Send</button>
                </div>
            </div>
        </div>  

        <br><br>

        <br><br>        
        <!-- <div class="container-fluid chat-bod-mob">
            <div class="row">
                <div class="col display">
                    
                </div>
            </div>
  
            <div class="row">
                <div class="col-9">
               
                    <input type="text" class="form-control" id="messm" placeholder="Message..">
                
                </div>
                <div class="col-2">
                    <button type="button" class="btn btn-success" id="sendm">Send</button>
                </div>
            </div>
        </div>   -->
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM" crossorigin="anonymous"></script>
        <script src="js/chat.js"></script>
    </body>
</html>