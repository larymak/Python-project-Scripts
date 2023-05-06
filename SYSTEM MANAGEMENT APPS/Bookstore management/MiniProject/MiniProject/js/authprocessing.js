$( document ).ready(function() {
    $(".otp-bod").hide()
    $(".otp-bodni").hide()
    $(".reg-bod").fadeIn("slow")
  
});
var g_mobilenumber = "";
var g_email = "";
var phnopatt = /^(\+\d{1,3}[- ]?)?\d{10}$/
// $("#repassword-input-reg").click(function(){
//     $(".showpass").show()
// })
// $("#password-input-reg").click(function(){
//     $(".showpass").show()
// })

$("#login-btn").click(function(){
    var email,pass;
    email =  $("#email-input-login").val()
    pass = $("#password-input-login").val()
    var mailpatt = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/


    if(email.trim() == ""){
      
        $("#email-input-login").addClass("is-invalid")
        $("#password-input-login").removeClass("is-invalid")
       
        $(".log-msg").html('<div class="alert alert-danger alert-dismissible fade show" role="alert"><strong>Oops! </strong>Please Enter Your E-Mail ID<button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button></div>')
    }
    // else if(!mailpatt.test(email)){
      
    //     $("#email-input-login").addClass("is-invalid")
    //     $("#password-input-login").removeClass("is-invalid")

    //     $(".log-msg").html('<div class="alert alert-danger alert-dismissible fade show" role="alert"><strong>Oops! </strong>Invalid E-Mail ID<button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button></div>')
    // }
    else if(pass.trim() == ""){
   
        $("#email-input-login").removeClass("is-invalid")
        $("#password-input-login").addClass("is-invalid")
    
        $(".log-msg").html('<div class="alert alert-danger alert-dismissible fade show" role="alert"><strong>Oops! </strong>Please Enter Your Password<button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button></div>')
    }
    else{
        // login
        $( "#login-form" ).submit();
        
        
    }
})
$("#email-input-login").click(function(){
    $(".showpaslogin").hide()
})
$("#password-input-login").click(function(){
    $(".showpaslogin").show()
})

var input = document.querySelector("#mobile-input-reg");
var iti = window.intlTelInput(input, {
    initialCountry: "in",
    separateDialCode: true,
    preferredCountries: ["in"],
    utilsScript: "https://cdn.jsdelivr.net/npm/intl-tel-input@16.0.3/build/js/utils.js",
});

// console.log(iti.isValidNumber());

$("#reg-btn").click(function(){
    var mobilenumber,email,pass,repass,fname;
    
    fname = $("#fname-input-reg").val()
    mobilenumber = $("#mobile-input-reg").val()
    email = $("#email-input-reg").val()
    pass = $("#password-input-reg").val()
    repass = $("#repassword-input-reg").val()
    g_mobilenumber = mobilenumber;
    g_email = email;
    var mailpatt = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
    

    // Minimum eight characters, at least one uppercase letter, one lowercase letter, one number and one special character:
    var passpatt = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$/
    // if(!phnopatt.test(mobilenumber)){
    //     $(".reg-msg").html('<div class="alert alert-danger alert-dismissible fade show" role="alert"><strong>Please Note! </strong>You Will Recive OTP on E-Mail<button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button></div>')
    //     alert('Not India')
    // }

    if(mobilenumber.trim() == ""){

        $("#mobile-input-reg").addClass("is-invalid")
        $("#email-input-reg").removeClass("is-invalid")
        $("#password-input-reg").removeClass("is-invalid")
        $("#repassword-input-reg").removeClass("is-invalid")
        $(".reg-msg").html('<div class="alert alert-danger alert-dismissible fade show" role="alert"><strong>Oops! </strong>Please Enter Your Mobile Number<button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button></div>')
    }
    else if(!iti.isValidNumber()){

        $("#mobile-input-reg").addClass("is-invalid")
        $("#email-input-reg").removeClass("is-invalid")
        $("#password-input-reg").removeClass("is-invalid")
        $("#repassword-input-reg").removeClass("is-invalid")
        $(".reg-msg").html('<div class="alert alert-danger alert-dismissible fade show" role="alert"><strong>Oops! </strong>Please Enter Valid Mobile Number<button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button></div>')
    }
    else if(email.trim() == ""){

        $("#mobile-input-reg").removeClass("is-invalid")
        $("#email-input-reg").addClass("is-invalid")
        $("#password-input-reg").removeClass("is-invalid")
        $("#repassword-input-reg").removeClass("is-invalid")
        $(".reg-msg").html('<div class="alert alert-danger alert-dismissible fade show" role="alert"><strong>Oops! </strong>Please Enter Your E-Mail ID<button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button></div>')
    }
    else if(!mailpatt.test(email)){

        $("#mobile-input-reg").removeClass("is-invalid")
        $("#email-input-reg").addClass("is-invalid")
        $("#password-input-reg").removeClass("is-invalid")
        $("#repassword-input-reg").removeClass("is-invalid")
        $(".reg-msg").html('<div class="alert alert-danger alert-dismissible fade show" role="alert"><strong>Oops! </strong>Please Enter Valid E-Mail ID<button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button></div>')
    }
    else if(pass.trim() == ""){
    
        $("#mobile-input-reg").removeClass("is-invalid")
        $("#email-input-reg").removeClass("is-invalid")
        $("#password-input-reg").addClass("is-invalid")
        $("#repassword-input-reg").removeClass("is-invalid")
        $(".reg-msg").html('<div class="alert alert-danger alert-dismissible fade show" role="alert"><strong>Oops! </strong>Please Create A Password<button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button></div>')
    }
    else if(!passpatt.test(pass)){

        $("#mobile-input-reg").removeClass("is-invalid")
        $("#email-input-reg").removeClass("is-invalid")
        $("#password-input-reg").addClass("is-invalid")
        $("#repassword-input-reg").removeClass("is-invalid")
        $(".reg-msg").html('<div class="alert alert-danger alert-dismissible fade show" role="alert"><strong>Please Note! </strong> Password Must Contain Minimum Eight Characters, At Least One Uppercase Letter, One Lowercase Letter, One Number And One Special Character<button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button></div>')
    }
    else if(repass.trim() == ""){

        $("#mobile-input-reg").removeClass("is-invalid")
        $("#email-input-reg").removeClass("is-invalid")
        $("#password-input-reg").removeClass("is-invalid")
        $("#repassword-input-reg").addClass("is-invalid")
        $(".reg-msg").html('<div class="alert alert-danger alert-dismissible fade show" role="alert"><strong>Oops! </strong>Please Re-Enter Your Password<button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button></div>')
    }
    else if(pass != repass){

        $("#mobile-input-reg").removeClass("is-invalid")
        $("#email-input-reg").removeClass("is-invalid")
        $("#password-input-reg").removeClass("is-invalid")
        $("#repassword-input-reg").addClass("is-invalid")
        $(".reg-msg").html('<div class="alert alert-danger alert-dismissible fade show" role="alert"><strong>Oops! </strong>Re-Entered Password Does Not Match<button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button></div>')
    }
    else{

        $("#signin-form").submit()
        
      
    }

});

function onSuccessLog(){
  
    email = $("#email-input-login").val("")
    pass = $("#password-input-login").val("")

    $("#email-input-login").removeClass("is-invalid")
    $("#password-input-login").removeClass("is-invalid")
   
}

function onSuccessReg(){
    fname = $("#fname-input-reg").val("")
    lname = $("#lname-input-reg").val("")
    city = $("#city-input-reg").val("")
    country = $("#country-input-reg").val("")
    mobilenumber = $("#mobile-input-reg").val("")
    email = $("#email-input-reg").val("")
    pass = $("#password-input-reg").val("")
    repass = $("#repassword-input-reg").val("")
    $("#fname-input-reg").removeClass("is-invalid")
    $("#lname-input-reg").removeClass("is-invalid")
    $("#city-input-reg").removeClass("is-invalid")
    $("#country-input-reg").removeClass("is-invalid")
    $("#mobile-input-reg").removeClass("is-invalid")
    $("#email-input-reg").removeClass("is-invalid")
    $("#password-input-reg").removeClass("is-invalid")
    $("#repassword-input-reg").removeClass("is-invalid")
    
}

function showPassword() {
    var x = document.getElementById("password-input-login");
    if (x.type === "password") {
      x.type = "text";
      $("#showpass").toggleClass("fa-eye fa-eye-slash");
    } else {
      x.type = "password";
      $("#showpass").toggleClass("fa-eye fa-eye-slash");
    }
}
function showPasswordReg() {
    var x = document.getElementById("password-input-reg");
    var y = document.getElementById("repassword-input-reg");
    if (x.type === "password" && y.type === "password") {

        $(".showpass").toggleClass("fa-eye fa-eye-slash");
        x.type = "text";
        y.type = "text"
    } else {
        
      $(".showpass").toggleClass("fa-eye fa-eye-slash");
        x.type = "password";
        y.type = "password";
    }
}

$("#password-input-reg").focusin(function(){
    $(this).popover({
        trigger: 'focus',
        content: "<div style='width:300px'><ul class='list-group'><li class='list-group-item border-0'>At Least One Uppercase Letter</li><li class='list-group-item border-0'>At Least One Lowercase Letter</li><li class='list-group-item border-0'>Between 8-15 Characters</li><li class='list-group-item border-0'>At Least One Number</li><li class='list-group-item border-0'>At Least One Special Character<br>&, @, $, %, #, *, _</li></ul></div>",
        html: true,
        placement: 'right'
    });
});
$("#repassword-input-reg").focusin(function(){
    $(this).popover({
        trigger: 'focus',
        content: "<div style='width:300px'><ul class='list-group'><li class='list-group-item border-0'>At Least One Uppercase Letter</li><li class='list-group-item border-0'>At Least One Lowercase Letter</li><li class='list-group-item border-0'>Between 8-15 Characters</li><li class='list-group-item border-0'>At Least One Number</li><li class='list-group-item border-0'>At Least One Special Character<br>&, @, $, %, #, *, _</li></ul></div>",
        html: true,
        placement: 'right'
    });
});

function goBack(){
    $(".otp-bod").hide()
    $(".reg-bod").fadeIn("slow")
}

// $("#email-input-reg").bind('input propertychange',function(){
    
// });
    
$("#verify-otp-btn").click(function(){
    var code =$("#otp-input-reg").val();
    var req = "req"; 
    $.ajax({
        type: 'POST',
        url: 'getsitedata.php',
        data: {req : req},
        dataType: 'json',
        success: function(site_data){
            
            $.ajax({ //Validating OTP
                type: 'POST',
                url: 'https://www.smsalert.co.in/api/mverify.json?apikey='+site_data.sms_api_key+'&mobileno='+g_mobilenumber+'&code='+code+'',
                dataType: 'json',
                success: function(data_validate){
                    
                    if(data_validate.description.desc == "Code does not match."){
                        $(".otp-msg").html('<div class="alert alert-danger alert-dismissible fade show" role="alert"><strong>Opps! </strong> Invalid OTP<button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button></div>')
                        // alert(data_validate.status)
                        
                    }
                    else{
                        //Submit Form
                        $("#signin-form").submit()
                        
                    }
                    
                },
                error: function(xhr, type){
                    alert("Error")
                    $(".otp-msg").html('<div class="alert alert-danger alert-dismissible fade show" role="alert"><strong>Opps! </strong>Somthing Went Wrong<button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button></div>')
                    //alert("Error in Ajax")
                    //$(".msgdiv").html('<div class="alert alert-danger alert-dismissible fade show" role="alert"><strong>OOPS!!</strong> Somthing Went Wrong<button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button></div>')
                }
            })
            
            
        },
        error: function(xhr, type){
            $(".otp-msg").html('<div class="alert alert-danger alert-dismissible fade show" role="alert"><strong>Opps! </strong>Somthing Went Wrong<button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button></div>')
            //alert("Error in Ajax")
            //$(".msgdiv").html('<div class="alert alert-danger alert-dismissible fade show" role="alert"><strong>OOPS!!</strong> Somthing Went Wrong<button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button></div>')
        }
    })
})

$("#verify-otp-onmail-btn").click(function(){

    var otp = $("#otp-email-input-reg").val()
    
    $.ajax({ //Validating OTP
        type: 'POST',
        data: {email : g_email, otp: otp},
        url: 'validateemailotp.php',
        dataType: 'json',
        success: function(data_validate_otp){
            
            if(data_validate_otp.result == "-1"){
                $(".otp-e-msg").html('<div class="alert alert-danger alert-dismissible fade show" role="alert"><strong>Opps! </strong> Invalid OTP<button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button></div>')
                // alert(data_validate.status)
                
            }
            else{
                //Submit Form
                $("#signin-form").submit()
                
            }
            
        },
        error: function(xhr, type){
            $(".otp-e-msg").html('<div class="alert alert-danger alert-dismissible fade show" role="alert"><strong>Opps! </strong>Somthing Went Wrong<button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button></div>')
            //alert("Error in Ajax")
            //$(".msgdiv").html('<div class="alert alert-danger alert-dismissible fade show" role="alert"><strong>OOPS!!</strong> Somthing Went Wrong<button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button></div>')
        }
    })
})