
var val;

var img = $("#thumbnail").change(function (event) {

    if(this.files[0].size > 2097152){
        $("#thumbnail").addClass("is-invalid");
        $(".msg").html(
            '<div class="alert  alert-danger alert-dismissible fade show" role="alert"><strong>Oops! </strong>File size is more than 2MB.<button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button></div>'
        );
        img.val('');
    }
    else{
        $("#thumbnail").removeClass("is-invalid");
        $(".msg").html('');

        var reader = new FileReader();
        reader.onload = function () {
        $("#JobProfileImage").attr("src", reader.result);
        };
        reader.readAsDataURL(event.target.files[0]);
    }
    
});

function priceToggle(){
    val = $("#myselect").val()
    if( val == "1"){
        $(".pricediv").hide()
    }
    else{
        $(".pricediv").show()
        
    }
}

function priceToggle2(){
    val = $("#myselect").val()
    if( val == "1"){
        $(".divs").hide()
    }
    else{
        $(".divs").show()
        
    }
}


$("#uploadbtn").click(function(){
    var thumb, bookname, price, description,bookauthor,keywords;
  
    thumb = $("#thumbnail").val()
    bookname = $("#bookname").val()
    if(val == "1"){
        price = $("#price").val()
    }
    else{
        price = "0"
    }
    
    description = $("#decs").val()
    bookauthor = $("#author").val()
    keywords = $("#keywords").val()

    if(thumb == ""){
        $("#thumbnail").addClass("is-invalid")
        $("#bookname").removeClass("is-invalid")
        $("#status").removeClass("is-invalid")
        $("#price").removeClass("is-invalid")
        $("#decs").removeClass("is-invalid")
        $("#author").removeClass("is-invalid")
        $("#keywords").removeClass("is-invalid")
        $(".msg").html('<div class="alert alert-danger alert-dismissible fade show" role="alert"><strong>Oops! </strong>Please Upload A Thumbnail<button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button></div>')
    }
    else if(bookname.trim() == ""){
        $("#thumbnail").removeClass("is-invalid")
        $("#bookname").addClass("is-invalid")
        $("#status").removeClass("is-invalid")
        $("#price").removeClass("is-invalid")
        $("#decs").removeClass("is-invalid")
        $("#author").removeClass("is-invalid")
        $("#keywords").removeClass("is-invalid")
        $(".msg").html('<div class="alert alert-danger alert-dismissible fade show" role="alert"><strong>Oops! </strong>Please Enter Book Name<button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button></div>')
    }
    else if(price.trim() == ""){
        $("#thumbnail").removeClass("is-invalid")
        $("#bookname").removeClass("is-invalid")
        $("#status").removeClass("is-invalid")
        $("#price").addClass("is-invalid")
        $("#decs").removeClass("is-invalid")
        $("#author").removeClass("is-invalid")
        $("#keywords").removeClass("is-invalid")
        $(".msg").html('<div class="alert alert-danger alert-dismissible fade show" role="alert"><strong>Oops! </strong>Please Enter Price of Book<button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button></div>')
    }
    else if(description.trim() == ""){
        $("#thumbnail").removeClass("is-invalid")
        $("#bookname").removeClass("is-invalid")
        $("#status").removeClass("is-invalid")
        $("#price").removeClass("is-invalid")
        $("#decs").addClass("is-invalid")
        $("#author").removeClass("is-invalid")
        $("#keywords").removeClass("is-invalid")
        $(".msg").html('<div class="alert alert-danger alert-dismissible fade show" role="alert"><strong>Oops! </strong>Please Enter Some Description<button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button></div>')
    }
    else if(bookauthor.trim() == ""){
        $("#thumbnail").removeClass("is-invalid")
        $("#bookname").removeClass("is-invalid")
        $("#status").removeClass("is-invalid")
        $("#price").removeClass("is-invalid")
        $("#decs").removeClass("is-invalid")
        $("#author").addClass("is-invalid")
        $("#keywords").removeClass("is-invalid")
        $(".msg").html('<div class="alert alert-danger alert-dismissible fade show" role="alert"><strong>Oops! </strong>Please Enter Author<button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button></div>')
    }
    else if(keywords.trim() == ""){
        $("#thumbnail").removeClass("is-invalid")
        $("#bookname").removeClass("is-invalid")
        $("#status").removeClass("is-invalid")
        $("#price").removeClass("is-invalid")
        $("#decs").removeClass("is-invalid")
        $("#author").removeClass("is-invalid")
        $("#keywords").addClass("is-invalid")
        $(".msg").html('<div class="alert alert-danger alert-dismissible fade show" role="alert"><strong>Oops! </strong>Please Enter Some Keywords<button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button></div>')
    }
    else{
        $("#uploadbooks").submit()
    }
})