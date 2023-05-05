$("#sendp").click(function(){
    var message = $("#messp").val()
    if(message.trim() != ""){
        $.ajax({
            type: 'POST',
            url: 'sendmessage.php',
            // data to be added to query string:
            data: {message: message},
            // type of data we are expecting in return:
            dataType: 'json',
            timeout: 300,
            context: $('body'),
            success: function(data){
                if(data.result == "1"){
                    location.reload();
                    // $.ajax({
                    //     type: 'POST',
                    //     url: 'updateui.php',
                    //     // data to be added to query string:
                    //     data: {message: message},
                    //     // type of data we are expecting in return:
                    //     dataType: 'json',
                    //     timeout: 300,
                    //     context: $('body'),
                    //     success: function(data){
                    //         if(data){
                    //             alert(data.result.message)
                    //         }
                    //         else{
                    //             alert("SOmthing Went Wrong")
                    //         }
                            
                    //     },
                    //     error: function(xhr, type){
                    //         alert("Ajax error")
                    //         //$(".msgdiv").html('<div class="alert alert-danger alert-dismissible fade show" role="alert"><strong>OOPS!!</strong> Somthing Went Wrong<button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button></div>')
                    //     }
                    // })
                }
                else{
                    alert("Somthing Went Wrong")
                }
                
            },
            error: function(xhr, type){
                alert("Ajax error")
                //$(".msgdiv").html('<div class="alert alert-danger alert-dismissible fade show" role="alert"><strong>OOPS!!</strong> Somthing Went Wrong<button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button></div>')
            }
        })
    }

})


setTimeout(function(){ 
    var message = $("#messp").val()
    if(message.trim() == ""){
        location.reload();
    }
        
}, 3000);

$("#sendm").click(function(){
    
})
