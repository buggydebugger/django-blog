from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

class Post(models.Model):
    title = models.CharField(max_length=100, unique=True)
    author = models.ForeignKey(User, related_name='posts', blank=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    content = models.TextField()
    pub_date = models.DateField(db_index=True, auto_now_add=True)

    def __unicode__(self):
        return '%s' % self.title

    def get_absolute_url(self):
        return reverse('blog:postdetails', kwargs={'slug': self.slug})
