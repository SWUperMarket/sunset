from django.contrib import auth
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.http import JsonResponse
import json
import my_settings

from .models import User
from .forms import *

"""
 * API No. 1
 * API Name : 로그인
 * [POST] /login
 * django.contrib.auth 이용해 구현 (urls.py에서 확인)
"""

"""
 * API No. 2
 * API Name : 회원가입
 * [POST] /register
"""
def get_secret_key(request):
    # 시크릿 키를 secret.json 파일에서 읽어옵니다.
    with open('secret.json') as f:
        secret_data = json.load(f)
        secret_key = secret_data.get('SECRET_KEY', None)
    #secret_key = my_settings.SECRET_KEY

    # 클라이언트에게 JSON 응답을 반환합니다.
    return JsonResponse({'SECRET_KEY': secret_key})

# 회원가입 함수
def register(request):
    page = 'register'
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        # 회원가입에 성공한 경우 (정보가 적절히 입력된 경우)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            # user 인증에 성공해 회원가입+로그인이 가능한 경우
            if user is not None:
                login(request, user)
                messages.success(request, '회원가입이 완료되었습니다.')
                # 로그인된 상태로 메인으로 이동
                return redirect('/')
            
            else:
                messages.error(request, '로그인에 실패하였습니다.')
        # form = UserCreationForm()
        else:
            error_messages = form.errors.values()
            return render(request, 'common/register.html', {'form': form, 'error_messages': error_messages})
    
    return render(request, 'common/register.html', {'form': form})

"""
 * API No. 3
 * API Name : 로그아웃
 * [PUT] /logout
"""

def logout_user(request):
    logout(request)
    # 로그아웃 시 메인 페이지로 이동
    return redirect('/')

"""
 * API No. 4
 * API Name : 유저 정보 조회 + 회원 정보 변경 (-패스워드 변경)
 * [GET/POST] /mypage
"""

def mypage(request):
    
    form = CustomUserChangeForm(instance=request.user)

    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        
        if form.is_valid():
            form.save()
            return redirect('common:mypage')
        
    context = { 'form': form }
    return render(request, 'common/mypage.html', context)

"""
 * API No. 5
 * API Name : 패스워드 변경
 * [POST] /password
"""

def change_password(request):

    if request.method == 'POST':
        form = CustomPasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '비밀번호가 성공적으로 변경되었습니다. 다시 로그인 해 주세요.')
            # 비밀번호 변경 후에도 로그인 상태가 유지되도록 함
            update_session_auth_hash(request, form.user)
            return redirect('/')
        
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f'{field}: {error}')
                
    else:
        form = CustomPasswordChangeForm(request.user)

    return render(request, 'common/change_password.html', {'form': form})

