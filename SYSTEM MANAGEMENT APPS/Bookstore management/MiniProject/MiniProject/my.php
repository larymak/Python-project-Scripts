
<?php
    
    $myarray = array();
    array_push($myarray,"Numan");   
    $value = "Numans";
    if(in_array("Numan", $myarray)){
        echo "Numan There";
    }
    else{
        echo "not there";
    }
    print_r($myarray);
    
?>


<?php
$people = array("Peter", "Joe", "Glenn", "Cleveland");

if (in_array("Glenns", $people))
  {
  echo "Match found";
  }
else
  {
  echo "Match not found";
  }
?>