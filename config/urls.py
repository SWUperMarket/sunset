"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # 관리자 URL 패턴 정의
    # path('user/', include('user.urls')),  # user 앱의 URL 패턴
    # path('common/', include('common.urls')),  # common 앱의 URL 패턴
    path('qna/', include('qna.urls')),  # qna 앱의 URL 패턴
    path('welfare1/', include('welfare1.urls')),  # welfare1 앱의 URL 패턴
    #path('main/', include('main.urls')),  # main 앱의 URL 패턴
    path('team/', include('team.urls')),  # team 앱의 URL 패턴
    path('', include('main.urls')),  # 루트 URL을 main 앱으로 포워딩
]

