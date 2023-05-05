$("#search").click(function(){
  
    var search = $("#searchtxt").val()
    if(search.trim() != ""){
        $("#searchform").submit()
    }
})