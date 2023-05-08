<?php
    error_reporting(0);
    if(isset($_COOKIE["email"])){
        header('Location: index.php');                                           
    }
    require_once "connection.php";
    if($_POST){

        $msg = '';
        $mobilepattern = '/^(\+\d{1,3}[- ]?)?\d{10}$/';
        $passpattern = '/^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/';
        $mailpatters = '/^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$/';
        
        if(empty($_POST["mobilenumber"])){
            $msg = '<div class="alert alert-danger alert-dismissible fade show" role="alert"><strong>Oops! </strong>Please Enter Your Mobile Number<button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button></div>';
        }
        else if(preg_match($mailpattern, $_POST["mobilenumber"])){
            $msg = '<div class="alert alert-danger alert-dismissible fade show" role="alert"><strong>Oops! </strong>Please Enter Valid Mobile Number<button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button></div>';
        }
        else if(empty($_POST["email"])){
            $msg = '<div class="alert alert-danger alert-dismissible fade show" role="alert"><strong>Oops! </strong>Please Enter Your E-Mail ID<button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button></div>';
        }
        else if(preg_match($mailpattern, $_POST["email"])){
            $msg = '<div class="alert alert-danger alert-dismissible fade show" role="alert"><strong>Oops! </strong>Please Enter Valid E-Mail ID<button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button></div>';
        }
        else if(empty($_POST["password"])){
            $msg = '<div class="alert alert-danger alert-dismissible fade show" role="alert"><strong>Oops! </strong>Please Create A Password<button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button></div>';
        }
        else if(preg_match($passpattern, $_POST["password"])){
            $msg = '<div class="alert alert-danger alert-dismissible fade show" role="alert"><strong>Please Note! </strong> Password Must Contain Minimum Eight Characters, At Least One Uppercase Letter, One Lowercase Letter, One Number And One Special Character<button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button></div>';
        }
        else{


            $email = $_POST["email"];

            $query = $link->prepare('SELECT * FROM `users` WHERE `email` = (?)');

            $query -> bind_param("s", $email);

            
            if($query->execute()){
                //If Query has A Result
                $res = $query->get_result();
                $row = mysqli_fetch_array($res);
                
                if($row == null){
                    
                   
                    $mobileno = $_POST["mobilenumber"];
                    $email = $_POST["email"];
                    $password = md5($_POST["password"]); 
                    echo $fname;
        
                    $query = $link->prepare('INSERT INTO `users` (`email`,`mobile_number`,`password`) VALUES (?,?,?)');
                    
                    // $query = "INSERT INTO `users` (`mobile_number`,`email`,`password`) VALUES ('$mobileno','$email','$password')"
                    $query->bind_param("sss",$email,$mobileno,$password);
        
                    if($query->execute()){
                        
                        setcookie("email", $email, time() + 60*60*24);
                        $msg = '<div class="alert alert-success alert-dismissible fade show" role="alert"><strong>Hurray! </strong> Account Created Successfuily <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button></div>'; 
                        header("Location: index.php");
                    }
                    else{
                        $msg = '<div class="alert alert-danger alert-dismissible fade show" role="alert"><strong>Oops! </strong>Something Went Wrong<button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button></div>'; 
                    }
                }
                else{
                    $msg = '<div class="alert alert-danger alert-dismissible fade show" role="alert"><strong>Oops! </strong> User Already Exist<button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button></div>';
                    
                }
                
            }
            else{
                $msg = '<div class="alert alert-danger alert-dismissible fade show" role="alert"><strong>Oops! </strong> Something Went Wrong<button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button></div>';
            }
            
           
        }
        $query -> close();
        $link -> close();     
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
        <link rel="icon" href="Resources/icon.png">
        <!-- Custom Css -->
        
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.css" />
        <!-- jQuery -->
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>
        <link href="css/authstyle.css" rel="stylesheet">
        <link rel="stylesheet"href="https://cdnjs.cloudflare.com/ajax/libs/intl-tel-input/17.0.8/css/intlTelInput.css">
        <script src="https://cdnjs.cloudflare.com/ajax/libs/intl-tel-input/17.0.8/js/intlTelInput.min.js"></script>
        <?php
            include('logo.php')
        ?>
        <title>Register</title>
        <style>
            .acc-btn:hover{
                color: red;
                font-size: 15px;
                transition: 0.4s ease-in-out;
            }
        </style>
    </head>

    <body class="bg-1">

        <!-- Sign In -->
        
        <br><br>
        <div class="container reg-bod">
            <!-- <img src="Resources/logo.png" class="mb-4"> -->
            <h1 class="display-6" style="color:white">Welcome</h1>
            <div class="mb-4 reg-msg" >
                
            </div>
            <form id="signin-form" method="post">
            
               
    
                <div class="form-floating mb-4">
                    <input type="tel" id="mobile-input-reg" class="form-control" name="mobilenumber" required="required">
                </div>
                <div class="form-floating mb-4">
                    <input type="email" class="form-control" id="email-input-reg" name="email" placeholder="username@gmail.com">
                    <label for="email-input-reg">E-Mail Id</label>
                </div>
                <div class="form-floating mb-4">
                    <input type="password" class="form-control" id="password-input-reg" name="password" placeholder="Password">
                    <label for="password-input-reg">Password</label>
                    <div class="showpassword-container">
                    <span onclick="showPasswordReg()" class="showpass fa fa-eye"></span>
                    </div>
                </div>
                <div class="form-floating mb-4">
                    <input type="password" class="form-control" id="repassword-input-reg" placeholder="Password">
                    <label for="repassword-input-reg">Re-Enter Password</label>
                    <div class="showpassword-container">
                    <span onclick="showPasswordReg()" class="showpass fa fa-eye"></span>
                    </div>
                </div>
                <a class="acc-btn" href="login.php" >Already Have An Account?</a><br><br>
                <button type="button" id="reg-btn" class="btn btn-danger">Sign Up</button>
            </form>
            
        </div>
  
        <!-- Option 1: Bootstrap Bundle with Popper -->

        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM" crossorigin="anonymous"></script>
        <script src="js/authprocessing.js"></script>

    </body>
</html>