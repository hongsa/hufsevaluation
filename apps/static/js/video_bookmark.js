/**
 * Created by hongsa on 2014-12-22.
 */
/**
 * Created by hongsa on 2014-12-20.
 */
$(document).ready(function(){

    $('.v_bookmark').click(function () {
        $.ajax({
            url: '/v_bookmark',
            type: 'POST',
            dataType: 'JSON',
            data:{
                name: $(this).parent().parent().attr('id')
            },
            success: function(data) {
                if(data.success){

                    alert('영상 컬렉션에 저장 완료!!');
                }
                else{
                    alert("error");
                }
            }
        });
    });

});