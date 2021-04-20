from django.views.generic import ListView
from django.shortcuts import render
from .models import Blog


class BlogList(ListView):
    template_name = 'blog/blog_list.html'
    paginate_by = 4

    def get_queryset(self):
        return Blog.objects.get_queryset().filter(active=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'بلاگ | فروشگاه آزمایشی'
        return context


def blog_detail(request, *args, **kwargs):
    selected_blog_id = kwargs['blogid']
    context = {
        'blog': Blog.objects.get_queryset().filter(active=True, id=selected_blog_id).first(),
        'title': 'جزئیات مطلب | فروشگاه آزمایشی'
    }
    return render(request, 'blog/blog_detail.html', context)
