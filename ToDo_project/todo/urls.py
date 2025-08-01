from django.urls import path
from . import views


urlpatterns = [
    path("",views.signin_page,name='signin_page'),
    path("index",views.index,name='index'),
    path("register",views.register,name='register'),
    path("signin", views.signin,name='signin'),
    path("page", views.signin_page, name='signin')
]