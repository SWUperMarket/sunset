# team/urls.py

from django.urls import path
from . import views

app_name = 'team'

urlpatterns = [
    path('', views.index, name='index'),  # 기본 URL에 대해 views.index 호출
    
]