/**
 * Created by hongsa on 2014-12-20.
 */
$(document).ready(function(){

    $('.a_star_area').find('input').rating({
        extendSymbol: function (rate) {
            $(this).tooltip({
                container: 'body',
                placement: 'top',
                title: '평점 ' + rate+ "점!"
            });
        }
    });


    $('.a_star_area').find('input').on('change', function () {
        alert($(this).val()+'점 평가 완료!!');
    });

    $('.a_star_area').find('input').on('change', function () {
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

                    alert($(this).val()+'점 평가 완료!!');
                }
                else{
                    alert("error");
                }
            }
        });
    });

});