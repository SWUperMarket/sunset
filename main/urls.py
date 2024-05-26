# main/urls.py

from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),  # 기본 URL에 대해 views.index 호출
    
]
