

function clickedButton() {
    $("#fourth_li").append("test")
}

function clickedButton2() {
    $("#fourth_li").append("<h3>H3 header</h3>")
}



$( document ).ready(function() {    
    console.log( "document ready!" );

    $('#mybtn').on('click', clickedButton2);
});
