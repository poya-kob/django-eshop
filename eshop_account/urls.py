from django.urls import path
from .views import login_page, register_page, logout_page

urlpatterns = [
    path('login', login_page),
    path('logout', logout_page),
    path('register', register_page),
]
