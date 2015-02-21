
$(document).ready(function() {
    var name = '{{actorRow.name}}';

	$.ajax({
		url:'../a_comment_rows',
		dataType:'JSON',
		method: 'POST',
        data:{
            name:name
        },
        success:function(data){

			var id = $.parseJSON(rows)

		}

	});

	function getArticle(id){

		$.ajax({
			url:'../a_comment_more',
			dataType:'JSON',
			data:{

				number: id
			},
			success:function(data){
				// string = data.id + ". "+data.title+": "+data.content
				string = '<div class="panel panel-default">'+'<div class="row">'+
                '<div class="col-sm-2 text-left">'+'<p class="comment_author">'+
                '<img src="/static/img/'+data.level+'.png"/>'+'&nbsp;&nbsp;'+
                data.user+'</p>'+'</div>'+'<div class="col-sm-9">'+'<p class="text-center commentBox">'
                +data.comments+'</p>'+'</div>'+'</div>'+'</div>'

				$('#additional').append(string);
			}
		});

	}

	$('#load_more_button').click(function(){
		
        JQuery.each(id, function(){
            getArticle(id);
        });

		
		
	});
});

