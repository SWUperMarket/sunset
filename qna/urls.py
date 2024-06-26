from django.urls import path
from . import views

app_name = 'qna'

urlpatterns = [
    ## 질문 불러오기
    path('', views.index, name='index'),
    ## 질문 상세 조회
    path('<int:question_id>/', views.detail, name='detail'),
    ## 댓글 작성
    path('answer/create/<int:question_id>/', views.answer_create, name='answer_create'),
    ## 질문 작성
    path('question/create/', views.question_create, name='question_create'),
    ## 댓글 삭제
    path('answer/delete/<int:answer_id>/', views.answer_delete, name='answer_delete'),
]