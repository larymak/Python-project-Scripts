<?php
    error_reporting(0);
    if(isset($_COOKIE["email"])){
        header('Location: index.php');                                           
    }
    
    
    require_once "connection.php";
    
    
    if($_POST){
    
        $msg = '';
        
    
        if(empty($_POST["email"])){
            $msg = '<div class="alert alert-danger alert-dismissible fade show" role="alert"><strong>Oops! </strong>Please Enter Your E-Mail ID<button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button></div>';
        }
    
        else if(empty($_POST["password"])){
            $msg = '<div class="alert alert-danger alert-dismissible fade show" role="alert"><strong>Oops! </strong>Please Enter Your Password<button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button></div>';
        }
    
        else{
      
            $email = $_POST["email"];
            $password = md5($_POST["password"]); 
        
    
            $query = $link->prepare('SELECT * FROM `users` WHERE `email` = (?) OR `mobile_number` = ?');
    
            $query -> bind_param("ss", $email,$email);
    
            
            if($query->execute()){
                //If Query has A Result
                $res = $query->get_result();
                $row = mysqli_fetch_array($res);
    
                if($row == null){
                    $msg = '<div class="alert alert-danger alert-dismissible fade show" role="alert"><strong>Oops! </strong> Invalid E-Mail ID/Mobile Number <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button></div>';
                }
                else{
                    if($row['email'] == $email || $row['mobile_number'] == $email){
                        //If Username Match 
                        if($row['password'] == $password){

                            setcookie("email", $row['email'], time() + 60*60*24);
                            
                            //If Username And Password Matches
                            $msg = '<div class="alert alert-success alert-dismissible fade show" role="alert"><strong>Hurray! </strong> Loged In Successfuilly <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button></div>';
                            header("Location: index.php");
                           
                        }
                        else{
                            //invalid Password
                            $msg = '<div class="alert alert-danger alert-dismissible fade show" role="alert"><strong>Oops! </strong> Invalid Password <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button></div>';
                        }
                    }
                    else{
                        $msg = '<div class="alert alert-danger alert-dismissible fade show" role="alert"><strong>Oops! </strong> Invalid E-Mail ID/Mobile Number <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button></div>';
                        //Invalid Username  
                    }
                }
                
            }
            else{
                $msg = '<div class="alert alert-danger alert-dismissible fade show" role="alert"><strong>Oops! </strong> Somthing Went Wrong <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button></div>';
                
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
        <?php
            include('logo.php')
        ?>
      
        <!-- jQuery -->
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.css" />
 

        

        <!-- Custom Css -->

        <link href="css/authstyle.css" rel="stylesheet">

        <title>Login</title>
        <style>
            .acc-btn:hover{
                color: red;
                transition: 0.4s ease-in-out;
            }
        </style>
    </head>

    <body class="bg-1">


        
        <!-- Login -->

        <div class="container login-bod">
        <h1 class="display-6" style="color:white">Welcome</h1>

            <div class="mb-4 log-msg">
                <?=$msg?>
            </div>

            <form id="login-form" method="post">
                <div class="form-floating mb-4">
                    <input type="email" class="form-control" name="email" id="email-input-login" placeholder="username@gmail.com">
                    <label for="email-input-login">E-Mail Id</label>
                </div>
                <div class="form-floating mb-4">
                    <input type="password" class="form-control" name="password" id="password-input-login" placeholder="Password">
                    <label for="password-input-login">Password</label>
                    <div class="showpassword-container">
                    <span onclick="showPassword()" id="showpass"  class="fa fa-eye"></span>
                    </div>
                </div>
                <a class="acc-btn" href="signin.php" >Create Account &#8594;</a><br><br>
                
            </form>
            <button type="button" id="login-btn" class="btn btn-danger">Log In</button>
        </div>

        
        <div class="footer" ></div>
        <!-- Option 1: Bootstrap Bundle with Popper -->
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM" crossorigin="anonymous"></script>
        <script src="js/authprocessing.js"></script>
    </body>
</html>