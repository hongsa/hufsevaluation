/**
 * Created by hongsa on 2014-12-20.
 */
$(document).ready(function(){

    $('#a_star').on('change',function() {
        $.ajax({
            url: '/a_save_star',
            type: 'POST',
            dataType: 'JSON',
            data:{
                name: $(this).parent().parent().attr('id'),
                star: this.value
            },
            success: function(data) {
                if(data.success){

                    alert($(this).val()+'점이 평가되었습니다!');
                }
                else{
                    alert("error");
                }
            }
        });
    });

});