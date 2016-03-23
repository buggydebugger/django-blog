from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView
from django.core.urlresolvers import reverse_lazy
from django.utils.text import slugify
from django.http import JsonResponse
from rest_framework import generics
from rest_framework import viewsets
from rest_framework import permissions
from django.shortcuts import get_object_or_404
from .models import Post
from .serializers import PostSerializer
from .permissions import IsOwnerOrReadOnly

def home(req):
    return render(req, template_name="index.html")


class PostDetailView(DetailView):
	model = Post
	context_object_name = 'post'


class PostUpdateView(UpdateView):
    model = Post
    fields = ['title', 'content', ]	


class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'content',]
    template_name = 'blog/post_create_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.slug = slugify(form.instance.title)
        form.save()
        return super(PostCreateView, self).form_valid(form)



class PostListView(ListView):
    paginate_by = 2
    model = Post

    def get(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()
        allow_empty = self.get_allow_empty()
        if not allow_empty:
            # When pagination is enabled and object_list is a queryset,
            # it's better to do a cheap query than to load the unpaginated
            # queryset in memory.
            if (self.get_paginate_by(self.object_list) is not None
                    and hasattr(self.object_list, 'exists')):
                is_empty = not self.object_list.exists()
            else:
                is_empty = len(self.object_list) == 0
            if is_empty:
                raise Http404(_("Empty list and '%(class_name)s.allow_empty' is False.")
                        % {'class_name': self.__class__.__name__})
        context = self.get_context_data()
        if self.request.GET.get('page'):
            new_context = {}
            for i, post in enumerate(context['object_list']):
                new_context[str(i)]={'can_edit': post.author == self.request.user ,'slug':post.slug, 'title': post.title, 'content':post.content,'author': post.author.username, 'pub_date': post.pub_date}
            new_context.update({ 'page_num': context['page_obj'].number, 'total_pages': context['page_obj'].paginator.num_pages  })
            return JsonResponse(new_context)
        return self.render_to_response(context)


class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy('blog:postlist')


class UserPostListView(ListView):
    model = Post
    paginate_by = 2
    template_name = 'blog/post_usr_list.html'

    def get_queryset(self):
        return self.request.user.posts.all()

# Api Views


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)
    lookup_field = 'slug'
    
