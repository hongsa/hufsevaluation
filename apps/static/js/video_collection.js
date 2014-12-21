$(document).ready(function(){

	$("#v_bookmark_button").click(function(){
		$("#v_bookmark_list").addClass("active").removeClass("hidden");
		$("#v_rating_list").addClass("hidden").removeClass("active");
	});

	$("#v_rating_button").click(function(){
		// alert("rate");
		$("#v_bookmark_list").addClass("hidden").removeClass("active");
		$("#v_rating_list").addClass("active").removeClass("hidden");
	});


});/**
 * Created by hongsa on 2014-12-22.
 */
