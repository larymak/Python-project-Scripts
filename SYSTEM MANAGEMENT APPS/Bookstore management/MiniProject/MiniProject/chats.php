<?php
    if(!isset($_COOKIE["email"])){
        header('Location: login.php');                                           
    }
    error_reporting(0);
    if($_POST['chatstart']){
        setcookie("sender_id", $_POST['chatstart'], time() + 60*60*24);
        header('Location: chat.php');  
    }
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
      
        
        <title>Chats</title>
    </head>
    <body>
        <?php
            include('headermenu.php')
        ?>
        <script>
            $("#chat-link").addClass('active')
        </script>
        
        <br><br><br><br><br>

        <div class="container">
            <div class="row">
                <div class="col"></div>
                <div class="col">
                    <?=$msg?>
                </div>
                <div class="col"></div>
            </div>
            <!-- <ul class="nav nav-pills nav-fill">
                <li class="nav-item" >
                    <a class="nav-link fragment-nav-link" id="internship-fragment" style="border-left: 1px solid rgb(221, 221, 221); background-color:#3d4755; color:white;" href="index.php">Internships</a>
                </li>
               
                <li class="nav-item">
                    <a class="nav-link fragment-nav-link" id="mj-fragment" style="border-left: 1px solid rgb(221, 221, 221);" href="indexmicrojobs.php">Micro-Jobs</a>
                </li>
           
                <li class="nav-item">
                    <a class="nav-link fragment-nav-link" id="ft-fragment" href="indexfulltime.php" style="border-left: 1px solid rgb(221, 221, 221); border-right: 1px solid rgb(221, 221, 221);">Full-Time Internships</a>
                </li>
                https://www.youtube.com/watch?v=XfobCv4YBdk
            </ul> -->
        </div>  

        <br><br>
        <div class="container internship-bod">
            <?php
                require_once "connection.php";
                $query = $link->prepare('SELECT * FROM `users` WHERE `email` = (?)');
                $query -> bind_param("s", $_COOKIE['email']);
                $query->execute();
                $res = $query->get_result();
                $row = mysqli_fetch_array($res);
                $uid = $row['user_id'];

                $chats = $link->prepare("SELECT * FROM `chat` WHERE `reciver_id` = ?");
                $chats -> bind_param("i",$uid);


                $myarray = array();
                
                

                if ($chats->execute()) {
                    $res = $chats->get_result();

                    if (mysqli_num_rows($res) > 0) {

                        while ($chat_users = mysqli_fetch_array($res)) {
                            if (in_array($chat_users['sender_id'], $myarray)){
                                
                            }
                            else{
                                array_push($myarray,$chat_users['sender_id']); 
                                $queryudetails = $link->prepare('SELECT * FROM `users` WHERE `user_id` = (?)');
                                $queryudetails -> bind_param("i",$chat_users['sender_id']);
                                $queryudetails->execute();
                                $res_queryudetails = $queryudetails->get_result();
                                $row_queryudetails = mysqli_fetch_array($res_queryudetails);
                                ?>
                                <div class="container single-view" >
                                                
                                    <div class="row">
                                        <div class="row">
                                            <div class="col">
                                                <p class="m_uname"><?=$row_queryudetails['email']?></p>
                                            </div>
                                            <div class="col">
                                                <form method="post">
                                                    <input type="hidden" value="<?=$chat_users['sender_id']?>" name="chatstart">
                                                    <input type="hidden" value="<?=$chat_users['book_id']?>" name="bookid">
                                                    <button class="know-more-btn" type="submit" data-bs-toggle="collapse" data-bs-target="#my<?=$idnum?>" aria-expanded="false" aria-controls="collapseExample">
                                                        View Messages &#8594
                                                    </button>
                                                </form> 
                                            </div>
                                        </div>   
                                    </div>
                                </div>
                                <br>
                            <?php
                            }
                            

                            

                        }
                    }
                    else{
                        ?>
                        <div class="container" style="text-align: center;">
                            <div class="alert alert-secondary" role="alert">
                                No Chats Recived Yet!
                            </div>
                        </div>
                        <?php
                    }
                }   
            ?>
            
        
         

            
        
            <br>

        </div>
        

        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM" crossorigin="anonymous"></script>

    </body>
</html>