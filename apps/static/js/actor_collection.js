$(document).ready(function(){

    $("#rating_button").click(function(){
        // alert("rate");
        $(".rating_list").show();
        $(".bookmark_list").hide();
    });

    $("#bookmark_button").click(function(){
        $(".rating_list").hide();
        $(".bookmark_list").show();
    });


});/**
 * Created by hongsa on 2014-12-22.
 */
