/**
 * Created by hongsasung on 15. 2. 17..
 */
$.ajax({
     type:"POST"
    ,url: '/recomm'
    ,data:""
    ,success:function(data){
        //(조회성공일 때 처리)

    }
    ,beforeSend:function(){
        //(이미지 보여주기 처리)
        $('.wrap-loading').removeClass('display-none');
    }
    ,complete:function(){
        //(이미지 감추기 처리)
        $('.wrap-loading').addClass('display-none');

    }
    ,error:function(e){
        //조회 실패일 때 처리
    }
    ,timeout:100000
});