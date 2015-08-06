$(document).ready(function(){

    $("#show_major").click(function () {
        $(".major").show();
        $(".free").hide();
    });

    $("#show_free").click(function () {
        $(".major").hide();
        $(".free").show();
    });
});