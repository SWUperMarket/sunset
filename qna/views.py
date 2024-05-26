from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Answer, Question
from .forms import QuestionForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q


"""
 * API No. 1
 * API Name : 게시글 불러오기
 * [GET] /questionBoard
"""
def index(request):
    page = request.GET.get('page', '1')  # 페이지
    kw = request.GET.get('kw', '')  # 검색어
    #게시글 작성 역순으로 출력
    question_list = Question.objects.order_by('-create_date')
    if kw:
        question_list = question_list.filter(
            Q(subject__icontains=kw) |  # 제목 검색
            Q(content__icontains=kw) |  # 내용 검색
            Q(answer__content__icontains=kw) |  # 답변 내용 검색
            # Q(author__username__icontains=kw) |  # 질문 글쓴이 검색
            Q(answer__author__username__icontains=kw)  # 답변 글쓴이 검색
        ).distinct()
    paginator = Paginator(question_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)
    context = {'question_list': page_obj, 'page': page, 'kw': kw}
    return render(request, 'qna/qna_list.html', context)


"""
 * API No. 2
 * API Name : 게시글 상세 조회
 * [GET] /questionBoard/{boardId}
"""
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'qna/qna_detail.html', context)


"""
 * API No. 3
 * API Name : 댓글 작성
 * [POST] /questionBoard/answer/create/{answerID}
"""
@login_required(login_url='common:login')
def answer_create(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    content = request.POST.get('content','').strip()
    if content:
        question.answer_set.create(content=request.POST.get('content'), create_date=timezone.now(), author=request.user)
    return redirect('qna:detail', question_id=question.id)


"""
 * API No. 4
 * API Name : 게시글 작성
 * [GET] /questionBoard/question/create
"""
def question_create(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.create_date = timezone.now()
            question.save()
            return redirect('qna:index')
    else:
        form = QuestionForm()
    context = {'form': form}
    return render(request, 'qna/qna_write.html', context)


"""
 * API No. 6
 * API Name : 댓글 삭제
 * [GET] /questionBoard/answer/delete
"""
def answer_delete(request, answer_id):
    answer = get_object_or_404(Answer, pk=answer_id)
    answer.delete()
    return redirect('qna:detail', question_id=answer.question.id)
