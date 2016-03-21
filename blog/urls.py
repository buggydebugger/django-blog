from django.conf.urls import include, url
from django.contrib.auth.decorators import login_required
from rest_framework.urlpatterns import format_suffix_patterns


from .views import PostViewSet
from . import views

post_list = PostViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
post_detail = PostViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

urlpatterns = [
    url(r'^$', views.home, name="home" ),
    url(r'post/view/(?P<slug>[-\w]+)/$', views.PostDetailView.as_view(), name='postdetails'),
    url(r'post/update/(?P<slug>[-\w]+)/$', login_required(views.PostUpdateView.as_view()), name='postupdate'),
    url(r'post/create/$', login_required(views.PostCreateView.as_view()), name='postcreate'),
    url(r'post/list/$', views.PostListView.as_view(), name='postlist'),
    url(r'post/usr/list/$', login_required(views.UserPostListView.as_view()), name='userpostlist'),
    url(r'post/delete/(?P<slug>[-\w]+)/$', login_required(views.PostDeleteView.as_view()), name='postdelete'),
]

urlpatterns += format_suffix_patterns([
    url(r'^postapi/$', post_list, name='post-list'),
    url(r'^postapi/(?P<slug>[-\w]+)/$', post_detail, name='post-detail'),
])