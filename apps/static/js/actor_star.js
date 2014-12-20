$(document).ready(function(){

   $('#a_star_area').find('div').hover(function(){
      // alert("hehe");
      for(aa=1; aa<=5; aa++)
      {
         if( aa <= this.id )
            $('#' + aa).attr("class", "glyphicon glyphicon-heart");

         else
            $('#' + aa).attr("class", "glyphicon glyphicon-heart-empty");
      }

   });
   

   $('#a_star_area').find('div').click(function(){
      // alert("평가되었습니다.");
      $.ajax({
         url: '/a_save_star',
         type: 'POST',
         dataType: 'JSON',
         data:{
            name: $('this').parent().parent().attr("id"),
            star: this.id
         },
         success: function(data) {
            if(data.success){
               alert("평가되었습니다!");
            }
            else{
               alert("error");
            }
         }
      });
   });

});