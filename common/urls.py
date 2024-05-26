from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'common'

urlpatterns = [
    path('get-secret-key/', views.get_secret_key, name='get_secret_key'),
    path('login/', auth_views.LoginView.as_view(template_name='common/login.html'), name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register, name='register'),
    path('mypage/', views.mypage, name='mypage'),
    path('password/', views.change_password, name='password'),
]
