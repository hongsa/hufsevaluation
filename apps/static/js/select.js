function categoryChange(val){

    if (val == "major"){
        $(".major").show();
        $(".free").hide();
    }
    else{
        $(".major").hide();
        $(".free").show();
    }
};