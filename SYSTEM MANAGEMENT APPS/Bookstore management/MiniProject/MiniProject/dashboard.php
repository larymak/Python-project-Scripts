<?php
    if(!isset($_COOKIE["email"])){
        header('Location: login.php');                                           
    }
    error_reporting(0);
    require_once "connection.php";
    if($_POST['managereq']){
        setcookie("___manage__req", $_POST['managereq'], time() + 60*60*24);
        header('Location: manage.php');
    }
    if($_POST['deletereq']){
        
        $query = $link->prepare('DELETE FROM `books` WHERE `book_id` = ?');
        $query -> bind_param("i", $_POST['deletereq']);
        if($query->execute()){
            header('Location: dashboard.php');
        }
        else{
            $msg = '<div class="alert  alert-danger alert-dismissible fade show" role="alert"><strong>Oops! </strong>Error While Deleting Book.<button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button></div>';
        }
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
      
        
        <title>Dashboard</title>
    </head>
    <body>
        <?php
            include('headermenu.php')
        ?>
        <script>
            $("#navbarDropdownMenuLink").addClass('active')
            $("#manage-book").addClass('active-d')
        </script>
        
        <br><br><br><br><br>

        <div class="container">
            
      
            <div class="row">
                <div class="col"></div>
                <div class="col">
                    <div class="alert alert-secondary" role="alert">
                        All the books uplaoded can be seen and managed here.
                    </div>
                </div>
                <div class="col"></div>
            </div>
            <div class="row">
                <div class="col"></div>
                <div class="col">
                    <?=$msg?>
                </div>
                <div class="col"></div>
            </div>
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

                $querydashboard = $link->prepare("SELECT * FROM `books` WHERE `user_id` = ?");
                $querydashboard -> bind_param("i",$uid);

                $idnum = 0;
                if ($querydashboard->execute()) {
                    $res = $querydashboard->get_result();

                    if (mysqli_num_rows($res) > 0) {

                        while ($books = mysqli_fetch_array($res)) {
                            $idnum++;
                            ?>
                            <div class="container single-view" >
                                            
                                <div class="row">
                                    <div class="col" style="text-align: center;">
                                        <img src="showimg.php?id=<?= $books['book_id'] ?>" style="width:100px; height:150px">
                                        <!-- <img src="Resources/Demo.jpg" style="width:100px; height:150px"> -->
                                    </div>
                                    <div class="col ">
                                        <h1 class="display-6 jobtitle"><strong><?=$books['book_title']?></strong></h1>
                                        <br>
                                        <div class="row">
                                            <div class="col">
                                                <?php
                                                    if($books['availability'] == 'Available' || $books['availability'] == 'Comming Soon'){
                                                        ?>
                                                            <p class="internship" style="text-align: center;"><?=$books['availability']?></p>
                                                        <?php
                                                    }
                                                    else{
                                                    ?>
                                                        <p class="part-time-job"><?=$books['availability']?></p>
                                                    <?php
                                                    }
                                                    ?>
                                            </div>
                                            <div class="col">
                                                <?php
                                                    if($books['price'] == ""){
                                                        ?>
                                                            <p class="micro-job2">For Donation</p>
                                                        <?php
                                                    }
                                                    else{
                                                        ?>
                                                            <p class="micro-job">Rs: <?=$books['price']?></p>
                                                        <?php
                                                    }
                                                ?>
                                                
                                            </div>

                                        </div>
                                        <div class="row">
                                            <div class="col">
                                                <form method="post">
                                                    <input type="hidden" value="<?=$books['book_id']?>" name="deletereq">
                                                    <button class="know-more-btn" type="submit">
                                                        Delete Book
                                                    </button>
                                                </form>
                                            </div>
                                            <div class="col">
                                                <button class="know-more-btn" type="button" data-bs-toggle="collapse" data-bs-target="#my<?=$idnum?>" aria-expanded="false" aria-controls="collapseExample">
                                                    View Details &#8594
                                                </button> 
                                            </div>
                                        </div>
                                        <br>
                                    
                                    </div>
                                </div>
                                <div class="collapse" id="my<?=$idnum?>">
                                    <div class="card card-body">
                                        <div class="row mb-2">
                                            <strong><p class="jobdetails">Description:</p></strong>
                                            <p class="jobdetails"><?=$books['description']?></p>
                                            <strong><p class="jobdetails">Author:</p></strong>
                                            <p class="jobdetails"><?=$books['book_author']?></p>
                                           
                                        </div>
                                        <div class="row">
                                            
                                            <div class="col" style="border-right: 2px solid black;">
                                                <strong><p class="jobdetails">Conditon:</p></strong>
                                                <p class=" jobdetails" ><?=$books['book_condition']?></p>
                                                
                                            </div>
                                            <div class="col">
                                                <strong><p class="jobdetails">Keywords:</p></strong>
                                                <p class=" jobdetails" ><?=$books['keywords']?></p>
                                                
                                            </div>
                                        </div><br>
                                        <div class="continer" style="text-align: center;">
                                            <form method="post">
                                                <input type="hidden" name="managereq" value="<?=$books['book_id']?>">
                                                <input type="submit" id="apply-btn" class="btn btn-danger" name="applybtn" value="Manage">
                                            </form>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <br>
                            <?php

                        }
                    }
                    else{
                        ?>
                        <div class="container" style="text-align: center;">
                            <div class="alert alert-secondary" role="alert">
                                <a href="upload.php">Upload</a> Your Book Now And Start Earning And Helping Others!  
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