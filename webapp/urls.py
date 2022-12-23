from django.urls import path
from webapp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('upload', views.upload, name='upload'),
    path('display_list', views.display_list, name='display_list'),
    path('display_text', views.display_text, name='display_text'),

]
