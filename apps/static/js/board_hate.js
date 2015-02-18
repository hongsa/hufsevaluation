/**
 * Created by hongsasung on 15. 2. 18..
 */

$(document).ready(function(){

    $('#b_hate').click(function () {
        $.ajax({
            url: '/b_hate',
            type: 'POST',
            dataType: 'JSON',
            data:{
                id: $(this).parent().attr('id')
            },
            success: function(data) {
                if(data.success){
                    $('#b_like').html('<span class="glyphicon glyphicon-thumbs-up"></span>'+data.like);
                    $('#b_hate').html('<span class="glyphicon glyphicon-thumbs-down"></span>'+data.hate);
                    alert('싫습니다!!');
                }
                else{
                    alert("error");
                }
            }
        });
    });

});