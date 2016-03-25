var status_class = new Array();
status_class['PUB'] = 'label label-primary';
status_class['B'] = 'label label-danger'
status_class['UP']='label label-info'

function get_set(href) {

	console.log(href);
	$.getJSON(href, set);
	return false;

}


function set(data) {

	console.log(data)
	post1 = data[0];
	post2 = data[1];
	total_pages = data['total_pages'];
	page_num = data['page_num'];
	plug_to_view(post1, post2, total_pages, page_num);

}


function plug_to_view(post1, post2, total_pages, page_num ){
	if(post1){
		$('#post-1').parent().parent().show();
	plug_post(post1, '#post-1');
	}
	else{

		$('#post-1').parent().parent().hide();

	}
	if(post2){
		$('#post-2').parent().parent().show();
	plug_post(post2, '#post-2');
	}
	else{
		$('#post-2').parent().parent().hide();
	}
	set_paginator(total_pages, page_num);
}

function plug_post(post, id_listnode){

	title = post['title'];
	content = post['content'];
	console.log("content is "+content);
	author = post['author'];
	pub_date = post['pub_date'];
	can_edit = post['can_edit'];
	slug = post['slug']
	status = post['status']
	status_disp = post['status_disp']
	links_obj = get_links_obj(slug);

	$(id_listnode+" > #post_title").text(title);
	$(id_listnode+" > #post_content").html("<pre  style='white-space: pre-wrap;'>"+ content.substring(0,300)+"</pre>" );
	$(id_listnode+" > #post_author").text(author);
	// $(id_listnode+" > #post_status").text(status);
	$(id_listnode+" > #post_date").text(pub_date);
	$(id_listnode+" > #read").attr("href",links_obj['read_link']);
	$(id_listnode+ "> #post_status").val(status);
	$(id_listnode+ " > #statuslbl").text(status);
	$(id_listnode+ " > #statuslbl").attr('class',status_class[status]);



	if(can_edit){

		if($(id_listnode+" > #del_btn").length){
			$(id_listnode+" > #del_btn").attr('href',links_obj['del_link']);
		}
		else{

			$(id_listnode).append('<a id="del_btn" class="btn btn-danger" href="'+ links_obj['del_link']+'"><span class="glyphicon glyphicon-remove"></span> Delete</a>');
			 

		}

		if($(id_listnode+" > #update_btn").length){
			$(id_listnode+" > #update_btn").attr('href', links_obj['update_link']);
		}
		else{

			$(id_listnode).append('  <a id="update_btn" class="btn btn-warning" href="'+links_obj['update_link']+'"><span class="glyphicon glyphicon-edit"></span> Update..</a>');
		}

	}

	else{

		$(id_listnode+" > #del_btn").remove();
		$(id_listnode+" > #update_btn").remove();	

	}
	


}

function set_paginator(total_pages, page_num){
	if (page_num < total_pages) {
		$('#next').show();


	}

	if (page_num == 1) {

		$('#previous').hide();
	}

	if (page_num == total_pages) {
		$('#next').hide();
	}

	if (page_num > 1) {
		$('#previous').show();
	}

		$('#next').attr("href", "?page="+(page_num+1))
		$('#previous').attr("href", "?page="+(page_num-1))

	$('#page-count').text("Page " + page_num + " of " + total_pages);

}

function get_links_obj(slug){
	var read_link = "/post/view/" + slug ;
	var update_link = "/post/update/" + slug ;
	var del_link = "/post/delete/" + slug
	return {'read_link': read_link, 'update_link': update_link, 'del_link': del_link};
}


$(function(){

post_ids = ["#post-1", "#post-2"];
$.each(post_ids, function(index, id){

	$(id+ "> select").change(function(){
		slug= $("#slug-"+(index+1)).val();
		id_statuslbl = id + " > #statuslbl";
		changed_status= $(id + "> select option:selected").val()
		console.log(id+ "  "+ changed_status+ "   "+slug);
		var url= "/post/update/" + slug +"/";
		var data= {status:changed_status};

		$.ajax({
			url: url,
			type: 'POST',
			data: data,
			success: function(data, textStatus, jqXHR) {
				console.log('Data returned from server: ' + data + ', returned status code: ' + textStatus);
				
				

				$(id_statuslbl).text(changed_status);
				$(id_statuslbl).attr('class',status_class[changed_status]);
				alert('updated post status of :' + slug +" to "+changed_status);

			} || $.noop,
			beforeSend: function(xhr) {
				xhr.setRequestHeader("X-CSRFToken", csrftoken);
			},
			error: function(jqXHR, textStatus, errorThrown) {
				alert('update status failed: ' + slug)
				console.log('returned status code: ' + textStatus);
				console.log('errorThrown: ' + errorThrown);

			} || $.noop
		});

	});
});

});