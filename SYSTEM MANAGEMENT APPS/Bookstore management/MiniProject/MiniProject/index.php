<?php

    error_reporting(0);
    require_once "connection.php";

    

    if($_POST['useridchat']){
        $query = $link->prepare('SELECT * FROM `users` WHERE `email` = (?)');
        $query -> bind_param("s", $_COOKIE['email']);
        $query->execute();
        $res = $query->get_result();
        $row = mysqli_fetch_array($res);
        $uid = $row['user_id'];
        if($_POST['useridchat'] != $uid){
            setcookie("sender_id", $_POST['useridchat'], time() + 60*60*24);
            header('Location: chat.php');
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

        <!-- jQuery Link -->
        <?php
            include('logo.php')
        ?>
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>
      
        
        <title>Books</title>
    </head>
    <body>
        <?php
            include('headermenu.php')
        ?>
        <script>
            $("#index-link").addClass('active')
        </script>
        <br><br><br><br><br>

        <div class="container">
            
      
            <div class="row">
                <div class="col"></div>
                <div class="col">
                <form method="post" id="searchform">
                    <div class="form-floating">
                            <input type="text" class="form-control" name="searchtxt" id="searchtxt" placeholder="Search">
                            <label for="search-input-login">Search</label>
                        </div>
                    </div>
                    <div class="col">
                        <?php
                        if($_POST['searchtxt']){
                            ?>
                                <a href="index.php"><button style="padding: 15px;" class="btn btn-outline-danger" id="removefilter" type="button">Remove Filter</button></a>
                            <?php
                        }
                        else{
                            ?>
                                <button style="padding: 15px;" class="btn btn-outline-success" id="search" type="button">Search</button>
                            <?php
                        }
                        ?>
                        
                        
                    </div>
                    <div class="col"></div>
                </form>
                    
            </div>
        </div>  

        <br><br>
        <div class="container internship-bod">
            <?php
                require_once "connection.php";
                if($_POST['searchtxt']){
                    $querysearch = $link->prepare("SELECT * FROM `books` WHERE `book_title` = ? OR `book_author` = ?");
                    $querysearch -> bind_param("ss",$_POST['searchtxt'],$_POST['searchtxt']);
                    $idnum = 0;
                if ($querysearch->execute()) {
                    $querysearchres = $querysearch->get_result();

                    if (mysqli_num_rows($querysearchres) > 0) {

                        while ($searched = mysqli_fetch_array($querysearchres)) {
                            $idnum++;
                            ?>
                                <div class="container single-view" >
                                            
                                    <div class="row">
                                        <div class="col" style="text-align: center;">
                                            <img src="showimg.php?id=<?= $searched['book_id'] ?>" style="width:100px; height:150px">
                                            <!-- <img src="Resources/Demo.jpg" style="width:100px; height:150px"> -->
                                        </div>
                                        <div class="col ">
                                            <h1 class="display-6 jobtitle"><strong><?=$searched['book_title']?></strong></h1>
                                            <br>
                                            <div class="row">
                                                <div class="col">
                                                    <?php
                                                        if($searched['availability'] == 'Available'){
                                                            ?>
                                                                <p class="internship"><?=$searched['availability']?></p>
                                                            <?php
                                                        }
                                                        else{
                                                        ?>
                                                            <p class="part-time-job"><?=$searched['availability']?></p>
                                                        <?php
                                                        }
                                                    ?>
                                                    
                                                </div>
                                                <div class="col">
                                                    <?php
                                                        if($searched['price'] == ""){
                                                            ?>
                                                                <p class="micro-job">For Donation</p>
                                                            <?php
                                                        }
                                                        else{
                                                            ?>
                                                                <p class="micro-job">Rs: <?=$searched['price']?></p>
                                                            <?php
                                                        }
                                                    ?>
                                                    
                                                </div>
                                                <!-- <div class="col">
                                                    <button class="btn btn-danger know-more-btn" type="button" data-bs-toggle="collapse" data-bs-target="#my<?=$idnum?>" aria-expanded="false" aria-controls="collapseExample">
                                                        View Details 
                                                    </button> 
                                                </div> -->
                                            </div>
                                            <div class="row">
                                                <div class="col"></div>
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
                                                <p class="jobdetails"><?=$searched['description']?></p>
                                                <strong><p class="jobdetails">Author:</p></strong>
                                                <p class="jobdetails"><?=$searched['book_author']?></p>
                                                <!-- <strong><p class="jobdetails">Admin:</p></strong>
                                                <div class="row">
                                                    <div class="col"><p class="jobdetails">Name: Zion</p></div>
                                                    <div class="col">Mobile Number: 9985632698</div>
                                                    <div class="col">Address: 29 Floor, Orchid Inc, Mumbai Central</div>
                                                </div>  -->
                                            </div>
                                            <div class="row">
                                                
                                                <div class="col" style="border-right: 2px solid black;">
                                                    <strong><p class="jobdetails">Conditon:</p></strong>
                                                    <p class=" jobdetails" ><?=$searched['book_condition']?></p>
                                                    
                                                </div>
                                                <div class="col">
                                                    <strong><p class="jobdetails">Keywords:</p></strong>
                                                    <p class=" jobdetails" ><?=$searched['keywords']?></p>
                                                    
                                                </div>
                                            </div><br>
                                            <div class="continer" style="text-align: center;">
                                                <form method="post">
                                                    <input type="hidden" value="<?=$searched['user_id']?>" name="useridchat"> 
                                                    <?php
                                                        $query = $link->prepare('SELECT * FROM `users` WHERE `email` = (?)');
                                                        $query -> bind_param("s", $_COOKIE['email']);
                                                        $query->execute();
                                                        $res = $query->get_result();
                                                        $row = mysqli_fetch_array($res);
                                                        $uid = $row['user_id'];
                                                        if($searched['user_id'] == $uid){
                                                            ?>
                                                                <input type="submit" id="apply-btn" disabled class="btn btn-danger" name="applybtn" value="Contact">
                                                            <?php
                                                        }
                                                        else{
                                                            ?>
                                                                <input type="submit"  id="apply-btn" class="btn btn-danger" name="applybtn" value="Contact">
                                                            <?php 
                                                        }
                                                    ?>
                                                    
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
                        if($_POST['searchtxt']){
                            ?>
                            <div class="container" style="text-align: center;">
                                <div class="alert alert-secondary" role="alert">
                                    Book Not Found
                                </div>
                            </div>
                            <?php
                        }
                        else{
                            ?>
                            <div class="container" style="text-align: center;">
                                <div class="alert alert-secondary" role="alert">
                                    Stay Tuned We Will Be In Stock Soon!  
                                </div>
                            </div>
                            <?php
                        }
                        
                    }
                }
                }
                else{
                    $querydisp = $link->prepare('SELECT * FROM `books`');
                    $idnum = 0;
                if ($querydisp->execute()) {
                    $querydispresres = $querydisp->get_result();

                    if (mysqli_num_rows($querydispresres) > 0) {

                        while ($books = mysqli_fetch_array($querydispresres)) {
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
                                                        if($books['availability'] == 'Available'){
                                                            ?>
                                                                <p class="internship"><?=$books['availability']?></p>
                                                            <?php
                                                        }
                                                        else{
                                                        ?>
                                                            <p class="part-time-job"><del><?=$books['availability']?></del></p>
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
                                                                <p class="micro-job">&#x20AC;: <?=$books['price']?></p>
                                                            <?php
                                                        }
                                                    ?>
                                                </div>
                                                <!-- <div class="col">
                                                    <button class="btn btn-danger know-more-btn" type="button" data-bs-toggle="collapse" data-bs-target="#my<?=$idnum?>" aria-expanded="false" aria-controls="collapseExample">
                                                        View Details 
                                                    </button> 
                                                </div> -->
                                            </div>
                                            <div class="row">
                                                <div class="col"></div>
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
                                                <!-- <strong><p class="jobdetails">Admin:</p></strong>
                                                <div class="row">
                                                    <div class="col"><p class="jobdetails">Name: Zion</p></div>
                                                    <div class="col">Mobile Number: 9985632698</div>
                                                    <div class="col">Address: 29 Floor, Orchid Inc, Mumbai Central</div>
                                                </div>  -->
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
                                                    <input type="hidden" value="<?=$books['user_id']?>" name="useridchat"> 
                                                    <?php
                                                        $query = $link->prepare('SELECT * FROM `users` WHERE `email` = (?)');
                                                        $query -> bind_param("s", $_COOKIE['email']);
                                                        $query->execute();
                                                        $res = $query->get_result();
                                                        $row = mysqli_fetch_array($res);
                                                        $uid = $row['user_id'];
                                                        if($books['user_id'] == $uid){
                                                            ?>
                                                                <input type="submit" id="apply-btn" disabled class="btn btn-danger" name="applybtn" value="Contact">
                                                            <?php
                                                        }
                                                        else{
                                                            ?>
                                                                <input type="submit"  id="apply-btn" class="btn btn-danger" name="applybtn" value="Contact">
                                                            <?php 
                                                        }
                                                    ?>
                                                    
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
                        if($_POST['searchtxt']){
                            ?>
                            <div class="container" style="text-align: center;">
                                <div class="alert alert-secondary" role="alert">
                                    Book Not Found
                                </div>
                            </div>
                            <?php
                        }
                        else{
                            ?>
                            <div class="container" style="text-align: center;">
                                <div class="alert alert-secondary" role="alert">
                                    Stay Tuned We Will Be In Stock Soon!  
                                </div>
                            </div>
                            <?php
                        }
                        
                    }
                }
                }
               
          
                
            ?> 
            
        
            <br>

        </div>
        
        
        <script src="js/search.js"></script>
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM" crossorigin="anonymous"></script>

    </body>
</html>