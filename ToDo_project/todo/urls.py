from django.urls import path
from . import views


urlpatterns = [
    path("",views.signin_page,name='sigin_page'),
    path("index",views.index,name='index'),
    path("register",views.register,name='register'),
    path("sigin", views.signin,name='sigin'),
    path("page", views.signin_page, name='sigin')
]