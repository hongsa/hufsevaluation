/**
 * Created by hongsa on 2014-12-20.
 */
$(document).ready(function(){

    $('.v_star_area').find('input').rating({
        extendSymbol: function (rate) {
            $(this).tooltip({
                container: 'body',
                placement: 'top',
                title: '평점 ' + rate+ "점!"
            });
        }
    });

    $('.v_star_area').find('input').on('change', function () {
        alert($(this).val()+'점이 평가되었습니다!');
    });

    $('.v_star_area').find('input').on('change', function () {
        $.ajax({
            url: '/v_save_star',
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