console.log("main js started")

$(document).ready(function(){
    // Change text color when the document is ready
    $("#form_btn").click(function(){
      // Replace "yourColorHere" with the desired color code or name
      $("#ptext").css("color", "red");
      let txt = $("#ptext").text();
      $("#ptext").text(txt + " added text")
    });
});

// document.addEventListener("DOMContentLoaded", function() {
//     var submitBtn = document.getElementById("submit_btn");
//     var pText = document.getElementById("ptext");

//     submitBtn.addEventListener("click", function() {
//       // Replace "red" with the desired color code or name
//       pText.style.color = "red";
//     });
// });



