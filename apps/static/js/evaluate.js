$(document).ready(function(){


    $('#lec_ev').click(function(){
        var input1 = $('input[name=total]').val();
        var input2 = $('input[name=difficulty]').val();
        var input3 = $('input[name=study_time]').val();
        var input4 = $('input[name=attendance]').val();
        var input5 = $('input[name=grade]').val();
        var input6 = $('input[name=achievement]').val();
        var text = $('textarea[name=content]').val();
        var lec_id = $('input[name=id]').val();

        if ((text=="")||(input1=="")|| (input2=="")|| (input3=="")|| (input4=="")|| (input5=="")|| (input6=="")){
            alert("평가와 정보를 자세히 적어주세요!!");
            return;
        }
        if((text.length)<30){
            alert("좀 더 길게 써주셔야 좋은 정보가 공유되겠죠??(30자이상)");
            return;
        }

        $.ajax({
            url: '/ev_input',
            type: 'POST',
            dataType: 'JSON',
            data:{
                id: lec_id,
                total : input1,
                difficulty : input2,
                study_time : input3,
                attendance : input4,
                grade : input5,
                achievement : input6,
                content : text
            },
            success: function(data) {
                if(data.success){
                    alert('정성스런 평가 감사합니다!');
                    window.location.href = "http://hufsev.com/search";
                }
                else{
                    alert("이미 평가를 한 수업입니다.");
                    window.location.href = "http://hufsev.com/search";
                }
            }
        });
    });
});




