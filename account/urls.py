from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'account'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', views.dashboard, name='dashboard'),
    path('register/', views.register, name='register'),
    path('create/', views.edit_user, name='edit_user'),
]
