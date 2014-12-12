$(document).ready(function(){

	$("#view_button").click(function(){
		$("#v_list").addClass("active").removeClass("hidden");
		$("#r_list").addClass("hidden").removeClass("active");
	});

	$("#rate_button").click(function(){
		// alert("rate");
		$("#v_list").addClass("hidden").removeClass("active");
		$("#r_list").addClass("active").removeClass("hidden");
	});


	$("#view_video_btn").click(function(){
		// alert("123");
		$("#view_video_list").removeClass("hidden");
		$("#view_actor_list").addClass("hidden");
	});

	$("#view_actor_btn").click(function(){
		// alert("345");
		$("#view_video_list").addClass("hidden");
		$("#view_actor_list").removeClass("hidden");
	});

	$("#bookmark").click(function(){
      alert("즐겨찾기에 저장되었습니다!");
	});
});