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

                    toastr.options = {
                        "closeButton": false,
                        "debug": false,
                        "newestOnTop": false,
                        "progressBar": false,
                        "positionClass": "toast-top-center",
                        "preventDuplicates": false,
                        "onclick": null,
                        "showDuration": "300",
                        "hideDuration": "1000",
                        "timeOut": "1500",
                        "extendedTimeOut": "1500",
                        "showEasing": "swing",
                        "hideEasing": "linear",
                        "showMethod": "fadeIn",
                        "hideMethod": "fadeOut"
                    };

                    Command: toastr["success"]("배우컬렉션에 저장되었습니다!");
                }
                else{
                    alert("error");
                }
            }
        });
    });

});