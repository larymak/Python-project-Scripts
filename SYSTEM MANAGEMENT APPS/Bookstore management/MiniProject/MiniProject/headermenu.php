<?php
    if($_POST['logout']){
        require_once('logout.php');
    }
?>  
<link href="css/headermenu.css" rel="stylesheet">
<nav class="navbar navbar-expand-lg navbar-dark custom-nav fixed-top nav-bg">
    <div class="container-fluid">
        <a class="navbar-brand" href="index.php" id="logo"><img src="Resources/logo.jpg" width="50xp" height="50px"></a>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNavAltMarkup" aria-controls="navbarNavAltMarkup" aria-expanded="false" aria-label="Toggle navigation">
            <img src="Resources/menu-icon-white.png">
        </button>
        <div class="collapse navbar-collapse"  id="navbarNavAltMarkup">
            <div class="navbar-nav" style="background-color: #313a46;">
                <!-- <a class="nav-link custom-link " id="home-link" href="https://adotcreation.com/" aria-current="page">Home</a> -->
            
                <?php
                    if(isset($_COOKIE["email"])){
                        ?>
                            <li class="nav-item dropdown">
                                <a class="nav-link dropdown-toggle custom-link" href="dashboard.php" id="navbarDropdownMenuLink" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                                    Dashboard
                                </a>
                                <ul class="dropdown-menu" aria-labelledby="navbarDropdownMenuLink">
                                    <li><a class="dropdown-item" id="create-book" href="upload.php">Upload Book</a></li>
                                    <li>
                                        <a class="dropdown-item" id="manage-book" href="dashboard.php">Manage Book</a>
                                    </li>
                                </ul>
                            </li>
                            <a class="nav-link custom-link" id="chat-link" href="chats.php" aria-current="page" >Chats</a>
                        <?php
                    }
                ?>
                
                <a class="nav-link custom-link" id="index-link" href="index.php" aria-current="page" >Books</a>
                
                <?php
                    if(!isset($_COOKIE["email"])){
                        ?>
                            <a class="nav-link" id="login-link" href="login.php" aria-current="page">Login</a>
                            <a class="nav-link" id="login-link" href="signin.php" aria-current="page">Register</a>
                            
                        <?php
                    }
                    else{
                    ?>
                    <li class="nav-item dropdown">
                        <a class="nav-link dropdown-toggle custom-link" href="javascript:void(0)" id="navbarDropdownMenuLink" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                            <?=$_COOKIE['email']?>
                        </a>
                        <ul class="dropdown-menu" aria-labelledby="navbarDropdownMenuLink">
                            <li><a class="dropdown-item" id="profile-link" href="profile.php">Profile</a></li>
                            <li>
                            <form method="post">
                                <input name="logout" type="hidden" value="logout">
                                <input class="dropdown-item logoutbtn" type="submit" value="Log Out" name="logout">
                            </form>
                            </li>
                        </ul>
                    </li>
                <?php
                    } 
                ?>
                
            </div>
        </div>
    </div>
</nav>

