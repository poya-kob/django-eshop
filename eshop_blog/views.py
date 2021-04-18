from django.views.generic import ListView

from django.shortcuts import render
from .models import Blog
from django.contrib.contenttypes.models import ContentType


class BlogList(ListView):
    template_name = 'blog/blog_list.html'
    paginate_by = 4

    def get_queryset(self):
        return Blog.objects.get_queryset().filter(active=True)


def blog_detail(request, *args, **kwargs):
    selected_blog_id = kwargs['blogid']
    context = {
        'blog': Blog.objects.get_queryset().filter(active=True, id=selected_blog_id).first()
    }
    return render(request, 'blog/blog_detail.html', context)
