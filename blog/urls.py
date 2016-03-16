from django.conf.urls import include, url
from django.contrib.auth.decorators import login_required

from . import views

urlpatterns = [
    url(r'^$', views.home, name="home" ),
    url(r'post/view/(?P<slug>[-\w]+)/$', views.PostDetailView.as_view(), name='postdetails'),
    url(r'post/update/(?P<slug>[-\w]+)/$', login_required(views.PostUpdateView.as_view()), name='postupdate'),
    url(r'post/create/$', login_required(views.PostCreateView.as_view()), name='postcreate'),
    url(r'post/list/$', views.PostListView.as_view(), name='postlist'),
    url(r'post/usr/list/$', views.UserPostListView.as_view(), name='userpostlist'),
    url(r'post/delete/(?P<slug>[-\w]+)/$', login_required(views.PostDeleteView.as_view()), name='postdelete'),
]
