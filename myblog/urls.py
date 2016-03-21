"""myblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.views import login
# from rest_framework.routers import DefaultRouter



from .forms import MyAuthenticationForm
from blog.views import PostViewSet
from blog.utils import redirect_loggedin


# router = DefaultRouter()
# router.register(r'postapi', PostViewSet)

urlpatterns = [
    # url(r'^', include(router.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('blog.urls', namespace='blog')),
    url(r'^login/$', redirect_loggedin(login), {'template_name': 'login.html',
     'authentication_form':MyAuthenticationForm},
        name='blog_login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout',
        {'next_page': 'blog:home'}, name='blog_logout'),
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),

]
