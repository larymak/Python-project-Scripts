<?php
    if(!isset($_COOKIE["email"])){
        header('Location: login.php');                                          
    }
    require_once "connection.php";
    error_reporting(0);
    // if($_POST['keywords']){
       
        $query = $link->prepare('SELECT * FROM `users` WHERE `email` = (?)');
        $query -> bind_param("s", $_COOKIE['email']);
        $query->execute();
        $res = $query->get_result();
        $row = mysqli_fetch_array($res);
        $uid = $row['user_id'];

        // $bookname = $_POST['bookname'];
        // $status = $_POST['status'];
        // $price = $_POST['price'];
        // $desc  =$_POST['decs'];
        // $author = $_POST['author'];
        // $condition = $_POST['condition'];
        // $keywords = $_POST['keywords'];

        // $name = $_FILES['thumbnail']['name'];
        // $type = $_FILES['thumbnail']['type'];
        // $image = addslashes(file_get_contents($_FILES['image']['tmp_name']));
        // echo $uid;
        // echo $bookname;
        // echo $status;
        // echo $price;
        // echo $desc;
        // echo $author;
        // echo $condition;
        // echo $keywords;
        // print_r($_FILES['thumbnail']);
        // $image = addslashes(file_get_contents($_FILES['thumbnail']['tmp_name']));

        // $queryupload = $link->prepare('INSERT INTO `books` (`user_id`, `book_title`, `image`, `availability`, `price`, `description`, `book_author`, `book_condition`, `keywords`) VALUES (?,?,"' . $image . '",?,?,?,?,?,?)');

        // $queryupload->bind_param("isssssss",$uid,$bookname,$status,$price,$desc,$author,$condition,$keywords);

        // if ($queryupload->execute()) {
        //     header("Location: dashboard.php");
        //     $msg = '<div class="alert  alert-success alert-dismissible fade show" role="alert"><strong>Hurray! </strong>New Book Uploaded Successfully.<button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button></div>';
        // }
        // else {
        //     $msg = '<div class="alert  alert-danger alert-dismissible fade show" role="alert"><strong>Oops! </strong>Error while uploading book.<button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button></div>';
        // }

    // }
?>
<!doctype html>
<html lang="en">
    <head>
        <!-- Required meta tags -->
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">

        <!-- Bootstrap CSS -->
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
       
        <!-- Custom Css -->

        <link href="css/style.css" rel="stylesheet">
        <link href="css/headermenu.css" rel="stylesheet">
        <!-- jQuery Link -->
        <?php
            include('logo.php')
        ?>
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>
     
       
        <title>User Profile Information</title>
    </head>
    <body>

        <br><br><br><br><br>
        <div class="container">
           
            <?php
                include('headermenu.php')
            ?>
            <script>
                $("#navbarDropdownMenuLink").addClass('active')
                $("#create-book").addClass('active-d')
            </script>
            <div class="row">
                <div class="col"></div>
                <div class="col">
                    <div class="alert alert-secondary" role="alert">
                       User Profile
                    </div>
                </div>
                <div class="col"></div>
            </div>
            <!-- <div class="row">
                <div class="col"></div>
                <div class="col">
                    <div class="msg"><?=$msg?></div>
                </div>
                <div class="col"></div>
            </div> -->
            <br>
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
            </ul> -->
        </div>  
        <div class="container internship-bod">
           
            <div class="container single-view-admin" >
                <form id="uploadbooks" method="POST" enctype="multipart/form-data">
                    <div class="row">
                       
                   
                        <div class="col ">
                           
                            <div class="row">
                                <div class="col">
                                   <strong> Name :</strong>  <?= $row['user_id'];?>
                           
                                </div>
                                <div class="col">
                                    <strong> Email:</strong>  <?=$row['email']?>
                                </div>
                                <div class="col">
                                    <strong>Phone Number: </strong> <?= $row['mobile_number'];?>
                                </div>
                               
               
                            </div>
                            <!-- <div class="row">
                                <div class="col"></div>
                                <div class="col">
                                    <button class="know-more-btn" type="button" data-bs-toggle="collapse" data-bs-target="#my2" aria-expanded="false" aria-controls="collapseExample">
                                        On View Details &#8594
                                    </button>
                                </div>
                            </div> -->
                            <!-- <br> -->
                       
                        </div>
                    </div>
                   
                </form>
               
            </div>
       
            <br>
        <!-- Modal -->
   
        <script src="js/bookprocessing.js"></script>
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM" crossorigin="anonymous"></script>

    </body>
</html>