/**
 * Created by hongsa on 2014-12-20.
 */
$(document).ready(function(){

    $('.a_bookmark').click(function () {
        $.ajax({
            url: '/a_bookmark',
            type: 'POST',
            dataType: 'JSON',
            data:{
                name: $(this).parent().parent().attr('id')
            },
            success: function(data) {
                if(data.success){

                    alert('배우 컬렉션에 찜꽁!!');
                }
                else{
                    alert("error");
                }
            }
        });
    });

});