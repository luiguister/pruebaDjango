from django.urls import path

from . import views

urlpatterns = [
    ##path('home', views.home),
    path('', views.HomeView.as_view(), name='home'),
    path('about', views.about, name='home.about'),
    ##path('auth', views.auth),
    path('auth', views.AuthView.as_view()),
    path('login', views.LoginInterfaceView.as_view(), name='login'),
    path('logout', views.LogoutInterfaceView.as_view(), name='logout'),
    path('signup', views.SignUpView.as_view(), name='signup'),
]