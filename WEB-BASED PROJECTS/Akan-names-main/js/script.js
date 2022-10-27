function display(){
  let day = document.getElementById("day").value;
  let month = document.getElementById("month").value;
  let year = document.getElementById("year").value;
  let birthday = month + "-" + day + "-" + year;

  if (year === ""){
    alert("Empty Entry, Please Fill the Form");
    document.getElementById("birth-form").reset();    
  }else{
    let machDate = new Date(birthday);
    let dt = machDate.getDate();
    let mon = machDate.getMonth();
    let yr = machDate.getFullYear();

    if (isNaN(dt) == true && isNaN(mon) == true){
      alert("Empty Date Slots, Enter Valid Date");
    }else if(parseInt(day)<=0 || parseInt(day)>31){
      alert("Invalid Day, Enter Between 1 and 31");
    }else if((mon+1)<=0 || (mon+1)>12){
      alert("Invalid Month, Enter Between 1 and 12");
    }else if(yr<=1950 || yr>2030){
      alert("Invalid Year, Enter Between 1950 and 2030");
    }else{
      let fValue = dayWeek(dt, (mon + 1), yr);
      document.getElementById("b-day").innerHTML = "Awesome... You Were Born on <strong>" + fValue[1]+ "</strong> and Your Akan Name is <em>" + fValue[0]+ "</em>";
    }
  }
}


// day of the Week
function dayWeek(day, month, year){
  let male = document.getElementById("male");
  let female = document.getElementById("female");
  let days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];
  ghanaMale = ['Kwasi', 'Kwadwo', 'Kwabena', 'Kwaku', 'Yaw', 'Kofi', 'Kwame'];
  ghanaFemale = ['Akosua', 'Adwoa', 'Abenaa', 'Akua', 'Yaa', 'Afua', 'Ama'];
  //jan and feb considered to be of the previous year

  if (month < 3){
    month += 12
    year -= 1
  }

  let dOfWeek = (day + parseInt(((month + 1) * 26) / 10) + year + parseInt(year / 4) + 6 * parseInt(year / 100) + parseInt(year / 400) - 1) % 7;
  
  if (male.checked ===  true){
    return [ghanaMale[dOfWeek] , days[dOfWeek]]
  }else if (female.checked === true){
    return [ghanaFemale[dOfWeek] , days[dOfWeek]]
  }else{
    alert("Try Again. Select a gender");
    document.getElementById("birth-form").reset();
  }
}

// reset function
function reset() {
  document.getElementById("birth-form").reset();
};