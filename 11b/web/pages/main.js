$(document).ready(function(){
    
    console.log("test script")
    
    
    //$("#name").css("color", "red");

    $("#name").css("text-align", "center");
    
    let text = "Dynamic header content"

    $("#dynamic_content").html(
      "<div><h5>" + text + "</h5></div>"
    )

              // Function to animate the div
    function animateDiv() {
        $("#animatedDiv").animate({
          left: '+=50px' // Move 50 pixels to the right
        }, 100); // Animation duration in milliseconds
    }

    $("#mybtn").on("click", function() {
        /* resize image js example */
        // var newWidth = 300;
        // var newHeight = 200;

        // $('#myimage').css({
        //   'width': newWidth + 'px',
        //   'height': newHeight + 'px'
        // });
        console.log("button pressed");
        animateDiv();
        $("#animatedParagraph").slideToggle(500);
  
    })

    // next ... 
})