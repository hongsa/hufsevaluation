// $(document).ready(function() {
//    var number = 0;

//    $.ajax({
//       url:'/video_detail',
//       dataType:'JSON',
//       success:function(data){

//          number = data.rows-5;

//       }

//    });

//    function getArticle(id){

//       $.ajax({
//          url:'/more',
//          dataType:'JSON',
//          data:{
//             number: id
//          },
//          success:function(data){
//          	i=data.id
//          	t=data.title
//          	c=data.content
//          	$("#article").append('<div class="panel panel-default"><div class="panel-heading"><a href="detail/' +i+ '">' +i+ ". " +t+ '</a></div><div class="panel-body">' +c+ '</div></div>');
//          }
//       });

//    }


//    $('#load_more_button').click(function(){
      
//       if(number>=1){
//       getArticle(number);
//       number = number -1;
//    }
//       else{
//          $('#load_more_button').hide();
//       }

      
      
//    });
// });