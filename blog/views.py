from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView
from django.core.urlresolvers import reverse_lazy
from django.utils.text import slugify
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
    
