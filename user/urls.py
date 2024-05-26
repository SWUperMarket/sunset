from django.urls import path
from . import views

app_name = "user"

urlpatterns = [
    # path('mypage/', views.mypage, name='mypage'),
    path('changepw/', views.changepw, name='changepw'),
]
