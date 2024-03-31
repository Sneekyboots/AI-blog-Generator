from django.urls import path
from . import views
urlpatterns=[
    path('', views.index, name='index'),
    path('login', views.user_login, name='login'),
    path('signup', views.user_signup, name='signup'),
    path('logout', views.user_logout, name='logout'),
    path('accounts/login/', views.user_login, name='login'),
     path('accounts/login/login', views.user_login, name='login'),
    path('accounts/login/signup/', views.user_signup, name='signup'),
    path('accounts/login/signup/login', views.user_logout, name='login'),
    path('accounts/login/signup/signup', views.user_logout, name='signup'),
    path('generate_blogs', views.generate_blogs, name='generate_blogs')
]

