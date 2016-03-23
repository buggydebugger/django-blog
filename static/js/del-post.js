// using jQuery
function getCookie(name) {
	var cookieValue = null;
	if (document.cookie && document.cookie != '') {
		var cookies = document.cookie.split(';');
		for (var i = 0; i < cookies.length; i++) {
			var cookie = jQuery.trim(cookies[i]);
			// Does this cookie string begin with the name we want?
			if (cookie.substring(0, name.length + 1) == (name + '=')) {
				cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
				break;
			}
		}
	}
	return cookieValue;
}
var csrftoken = getCookie('csrftoken');


	// var csrftoken = Cookies.get('csrftoken');



function del(node, slug) {
	url = '/postapi/' + slug;
	console.log(url);
	if (confirm('are you sure you want to remove this post? ' + slug) == true) {
		$.ajax({
			url: url,
			type: 'DELETE',
			success: function(data, textStatus, jqXHR) {
				console.log('Data returned from server: ' + data + ', returned status code: ' + textStatus);
				$(node).parent().parent().parent().remove();
				alert('deleted post :' + slug)
			} || $.noop,
			beforeSend: function(xhr) {
				xhr.setRequestHeader("X-CSRFToken", csrftoken);
			},
			error: function(jqXHR, textStatus, errorThrown) {
				alert('delete failed: ' + slug)
				console.log('returned status code: ' + textStatus);
				console.log('errorThrown: ' + errorThrown);

			} || $.noop
		});
	} else {
		return false
	}


}