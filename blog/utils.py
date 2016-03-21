from functools import wraps

from django.shortcuts import redirect

def redirect_loggedin(login_view):
	@wraps(login_view)
	def new_login_view(request, *args, **kwargs):
		if request.user.is_authenticated():
			return redirect('/')
		response = login_view(request, *args, **kwargs)
		return response
	return new_login_view

