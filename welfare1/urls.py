from django.urls import path
from . import views

app_name = 'welfare1'

urlpatterns = [
    path('', views.index, name='index'),
    path('policy_main', views.policy_main, name='policy_main'),
    path('policy/01/', views.policy_01, name='policy_01'),
    path('policy/02/', views.policy_02, name='policy_02'),
    path('policy/03/', views.policy_03, name='policy_03'),
    path('policy/04/', views.policy_04, name='policy_04'),
    path('policy/05/', views.policy_05, name='policy_05'),
    path('policy/06/', views.policy_06, name='policy_06'),
    path('policy/07/', views.policy_07, name='policy_07'),
    path('policy/08/', views.policy_08, name='policy_08'),
    path('policy/09/', views.policy_09, name='policy_09'),
    path('policy/10/', views.policy_10, name='policy_10'),
    path('policy/11/', views.policy_11, name='policy_11'),
    path('policy/12/', views.policy_12, name='policy_12'),
    path('protect', views.protect, name='protect'),
    path('home', views.home, name='home'),
    path('welfare_detail', views.welfare_detail, name='welfare_detail'),
    path('senior_class', views.senior_class, name='senior_class'),
    path('nursing', views.nursing, name='nursing'),

]