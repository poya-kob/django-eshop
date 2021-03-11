from django.urls import path
from .views import BlogList, blog_detail

urlpatterns = [
    path('blogs', BlogList.as_view()),
    path('blog/<blogid>/<category_name>', blog_detail)
]
