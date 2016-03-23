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
	plug_post(post1, '#post-1');
	plug_post(post2, '#post-2');
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
	links_obj = get_links_obj(slug);

	$(id_listnode+" > #post_title").text(title);
	$(id_listnode+" > #post_content").html("<pre  style='white-space: pre-wrap;'>"+ content.substring(0,300)+"</pre>" );
	$(id_listnode+" > #post_author").text(author);
	$(id_listnode+" > #post_date").text(pub_date);
	$(id_listnode+" > #read").attr("href",links_obj['read_link']);
	


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
	return {'read_link': read_link, 'update_link': update_link};
}