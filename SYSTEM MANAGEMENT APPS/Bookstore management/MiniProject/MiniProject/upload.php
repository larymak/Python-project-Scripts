<?php
    if(!isset($_COOKIE["email"])){
        header('Location: login.php');                                           
    }
    require_once "connection.php";
    error_reporting(0);
    if($_POST['keywords']){
        
        $query = $link->prepare('SELECT * FROM `users` WHERE `email` = (?)');
        $query -> bind_param("s", $_COOKIE['email']);
        $query->execute();
        $res = $query->get_result();
        $row = mysqli_fetch_array($res);
        $uid = $row['user_id'];

        $bookname = $_POST['bookname'];
        $status = $_POST['status'];
        $price = $_POST['price'];
        $desc  =$_POST['decs'];
        $author = $_POST['author'];
        $condition = $_POST['condition'];
        $keywords = $_POST['keywords'];

        // $name = $_FILES['thumbnail']['name'];
        // $type = $_FILES['thumbnail']['type'];
        $image = addslashes(file_get_contents($_FILES['image']['tmp_name']));
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

        $queryupload = $link->prepare('INSERT INTO `books` (`user_id`, `book_title`, `image`, `availability`, `price`, `description`, `book_author`, `book_condition`, `keywords`) VALUES (?,?,"' . $image . '",?,?,?,?,?,?)');

        $queryupload->bind_param("isssssss",$uid,$bookname,$status,$price,$desc,$author,$condition,$keywords);

        if ($queryupload->execute()) {
            header("Location: dashboard.php");
            $msg = '<div class="alert  alert-success alert-dismissible fade show" role="alert"><strong>Hurray! </strong>New Book Uploaded Successfully.<button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button></div>';
        } 
        else {
            $msg = '<div class="alert  alert-danger alert-dismissible fade show" role="alert"><strong>Oops! </strong>Error while uploading book.<button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button></div>';
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
        
        <!-- Custom Css -->

        <link href="css/style.css" rel="stylesheet">
        <link href="css/headermenu.css" rel="stylesheet">
        <!-- jQuery Link -->
        <?php
            include('logo.php')
        ?>
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>
      
        
        <title>Upload Book</title>
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
                        Created Book Will Be Displayed As Created Here
                    </div>
                </div>
                <div class="col"></div>
            </div>
            <div class="row">
                <div class="col"></div>
                <div class="col">
                    <div class="msg"><?=$msg?></div>
                </div>
                <div class="col"></div>
            </div>
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
                        <div class="col" style="text-align: center;">
                            <p class="jobdetails">Thumbnail:</p>
                            <img src="Resources/placeholder.png" alt="Thumbnail" id="JobProfileImage" width="150px" height="150px"><br><br>
                            <input type="file" id="thumbnail" name="image" accept="image/*">
                        </div>
                        <div class="col ">
                            <div class="form-floating mb-4">
                                <input type="text" class="form-control" name="bookname" id="bookname" placeholder="Name">
                                <label for="bookname">Name</label>
                            </div>
                            <br>
                            <div class="row">
                                <div class="col">
                                    <p class="jobdetails">Status:</p>
                                    <div style="width: 200px;">
                                        <select class="form-select" aria-label="Default select example" id="status" name="status">
                                            <option selected value="Available">Available</option>
                                            <option value="Out of Stock">Out of Stock</option>
                                            <option value="Comming Soon">Comming Soon</option>
                                        </select>
                                    </div>
                            
                                </div>
                                <div class="col">
                                    <p class="jobdetails">Price in Rs:</p>
                                    <select class="form-select mb-4" id="myselect" aria-label="Default select example" onchange="priceToggle()">
                                        <option value="1" selected>Donate</option>
                                        <option value="2" >Sell</option>
                                    </select>
                                    <div class="pricediv form-floating mb-4">
                                        <input type="text" class="form-control" name="price" id="price" placeholder="Name">
                                        <label for="price">Price</label>
                                    </div>
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
                                    <button class="know-more-btn" type="button" data-bs-toggle="collapse" data-bs-target="#my2" aria-expanded="false" aria-controls="collapseExample">
                                        On View Details &#8594
                                    </button> 
                                </div>
                            </div>
                            <br>
                        
                        </div>
                    </div>
                    <div class="collapse" id="my2">
                        <div class="card card-body">
                            <div class="row">
                                <strong><p class="jobdetails">Description:</p></strong>
                                <div class="form-floating">
                                    <textarea class="form-control" placeholder="Description" id="decs" name="decs" style="height: 150px; resize: none;"></textarea>
                                    <label for="decs">Description</label>
                                </div>
                                <strong><p class="jobdetails">Author:</p></strong>
                                <div class="form-floating mb-4">
                                    <input type="text" class="form-control" name="author" id="author" placeholder="Name">
                                    <label for="author">Author Name</label>
                                </div>
                            </div>
                            <div class="row">
                                
                                <div class="col" style="border-right: 2px solid black;">
                                    <strong><p class="jobdetails">Conditon:</p></strong>
                                    <div class="form-check">
                                        <input class="form-check-input" type="radio" value="New" name="condition" id="new" checked>
                                        <label class="form-check-label" for="new">
                                            New
                                        </label>
                                    </div>
                                    <div class="form-check">
                                        <input class="form-check-input" type="radio" name="condition" value="Old" id="old" >
                                        <label class="form-check-label" for="old">
                                            Old
                                        </label>
                                    </div>
                                    
                                </div>
                                <div class="col">
                                    <strong><p class="jobdetails">Keywords:</p></strong>
                                    <div class="form-floating">
                                        <textarea class="form-control" placeholder="Description" id="keywords" name="keywords" style="height: 150px; resize: none;"></textarea>
                                        <label for="keywords">Keywords</label>
                                    </div>
                                </div>
                            </div><br>
                            <div class="continer" style="text-align: center;">
                        
                                <input type="button" id="uploadbtn" class="btn btn-danger" name="uploadbtn" value="Upload Book">
                        
                            </div>
                        </div>
                    </div>
                </form>
                
            </div>
        
            <br>
        <!-- Modal -->
        <div class="modal fade" id="staticBackdrop" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" aria-labelledby="staticBackdropLabel" aria-hidden="true">
            <div class="modal-dialog">
                <div class="modal-content">
                    <div class="modal-header">
                    <h5 class="modal-title" id="staticBackdropLabel">Please Note!</h5>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                    </div>
                    <div class="modal-body">
                        Are You Sure You Want To Upload This Book?
                    </div>
                    <div class="modal-footer">
                        <button type="button" class="btn btn-outline-secondary" data-bs-dismiss="modal">Close</button>
                        <button type="button" class="btn btn-danger" id="confirm">Yes</button>
                    </div>
                </div>
            </div>
        </div>
        <script src="js/bookprocessing.js"></script>
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM" crossorigin="anonymous"></script>

    </body>
</html>