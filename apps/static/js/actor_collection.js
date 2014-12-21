$(document).ready(function(){

	$("#bookmark_button").click(function(){
		$("#bookmark_list").addClass("active").removeClass("hidden");
		$("#rating_list").addClass("hidden").removeClass("active");
	});

	$("#rating_button").click(function(){
		// alert("rate");
		$("#bookmark_list").addClass("hidden").removeClass("active");
		$("#rating_list").addClass("active").removeClass("hidden");
	});


});/**
 * Created by hongsa on 2014-12-22.
 */
