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
                    $('#b_like').html(data.like);
                    $('#b_hate').html(data.hate);
                    alert('싫어용!!');
                }
                else{
                    alert("error");
                }
            }
        });
    });

});