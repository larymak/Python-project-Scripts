function printContent() {
    const printButton = document.querySelector(".print:last-child button");
    if (printButton) {
        printButton.style.display = "none";
    }

    window.print();

    if (printButton) {
        printButton.style.display = "block";
    }
}
function test_result(){
    const result = document.querySelector(".print:result");
    if(result=="Non-Diabetic"){
        console.log("Hello");
    }
}



// script.js
document.addEventListener("DOMContentLoaded", function () {
    var genderRadios = document.querySelectorAll('input[name="gender"]');
    var pregnancyQuestion = document.getElementById('pregnancyQuestion');
    var pregnanciesInput = document.getElementById('pregnanciesInput');
    

    // Function to show or hide the "Are you pregnant?" and "No of Pregnancies" fields
    function togglePregnancyFields() {
        if (genderRadios[1].checked) {
            pregnancyQuestion.style.display = 'block';
            pregnancyQuestion.required = true;
            pregnanciesInput.style.display = 'block';
            pregnanciesInput.required = true;
            pregnanciesInput.style.marginBottom = '1rem';

        } else {
            pregnancyQuestion.style.display = 'none';
            pregnancyQuestion.required = false;
            pregnanciesInput.style.display = 'none';
            pregnanciesInput.required = false;
            pregnanciesInput.style.marginBottom = '0';
        }
    }

    // Add event listeners to gender radio buttons
    genderRadios.forEach(function (radio) {
        radio.addEventListener('change', togglePregnancyFields);
    });

    // Initial call to set the initial state
    togglePregnancyFields();
});