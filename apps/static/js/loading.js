$(function() {
    var loading = $('<div id="loading" class="loading"></div><img id="loading_img" alt="loading" src="/img/yadong.png" />').appendTo(document.body).hide();
    $(document).ready(function(){
        $(".loadingWrapper").fadeIn();
    });
        $(window).load(function() {
        $('loadingWrapper').fadeOut();
        $(body).show();
    });

});