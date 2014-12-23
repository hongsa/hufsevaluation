$(document).ready(function(){

    $("#v_rating_button").click(function(){
        // alert("rate");
        $(".v_rating_list").show();
        $(".v_bookmark_list").hide();
    });

    $("#v_bookmark_button").click(function(){
        $(".v_rating_list").hide();
        $(".v_bookmark_list").show();
    });


});/**
 * Created by hongsa on 2014-12-22.
 */
