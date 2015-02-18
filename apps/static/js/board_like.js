/**
 * Created by hongsasung on 15. 2. 18..
 */

$(document).ready(function(){

    $('#b_like').click(function () {
        $.ajax({
            url: '/b_like',
            type: 'POST',
            dataType: 'JSON',
            data:{
                id: $(this).parent().attr('id')
            },
            success: function(data) {
                if(data.success){
                    $('#b_like').html(data.like);
                    $('#b_hate').html(data.hate);

                    alert('좋아용!!');
                }
                else{
                    alert("error");
                }
            }
        });
    });

});