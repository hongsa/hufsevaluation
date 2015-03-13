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
                    $('#b_like').html('<span class="glyphicon glyphicon-thumbs-up"></span>'+data.like);
                    $('#b_hate').html('<span class="glyphicon glyphicon-thumbs-down"></span>'+data.hate);

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

                    Command: toastr["success"]("좋아요~~~!");
                }
                else{
                    alert("error");
                }
            }
        });
    });

});