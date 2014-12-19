/**
 * Created by hongsa on 2014-12-20.
 */
$(document).ready(function(){

   $('#v_star_area').find('div').hover(function(){
      // alert("hehe");
      for(v=1; v<=5; v++)
      {
         if( v <= this.id )
            $('#' + v).attr("class", "glyphicon glyphicon-heart");

         else
            $('#' + v).attr("class", "glyphicon glyphicon-heart-empty");
      }

   });


   $('#v_star_area').find('div').click(function(){
      // alert("평가되었습니다.");
      $.ajax({
         url: '/v_save_star',
         type: 'POST',
         dataType: 'JSON',
         data:{
            name: name,
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