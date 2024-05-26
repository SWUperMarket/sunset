from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField, PasswordChangeForm
from django.contrib.auth.forms import UserCreationForm as BaseUserCreationForm, UserChangeForm
from django.contrib.auth.models import User
import re

from .models import User

class UserCreationForm(BaseUserCreationForm):   # 사용자 계정 생성

    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password Confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "name", "password1", "password2", "phone", "email", "flag", "verifyCode"]

    def clean_password2(self):      # 입력된 두 패스워드가 서로 동일한지 검증
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("입력된 비밀번호가 일치하지 않습니다.")
        return password2
    
    def clean_phone(self):
        phone_number = self.cleaned_data.get("phone")

        if phone_number:            # 전화번호 형식에 맞게 입력되었는지 검증
            if not re.match(r'^010-\d{4}-\d{4}$', phone_number):
                raise forms.ValidationError('전화번호를 지정된 형식에 맞게 입력해 주세요.') 
        return phone_number
        
    def clean_verifyCode(self):     # 입력된 검증 코드가 사전에 안내된 코드와 동일한지 확인
        entered_code = self.cleaned_data.get("verifyCode")
        expected_code = "W3LCOM3T0SW!NG"    # 코드 변경 시 이 부분 수정하면 됨

        if entered_code != expected_code:
            raise forms.ValidationError("잘못된 인증 코드가 입력되었습니다.")
        
        return entered_code
    
    def save(self, commit=True):    # 입력된 데이터 저장
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

class CustomUserChangeForm(UserChangeForm):        # 사용자 정보 수정
    password = ReadOnlyPasswordHashField()    # 비밀번호를 암호화된 가져옴 (수정 불가능)

    class Meta(UserChangeForm.Meta):
        model = User
        fields = ('username', 'name', 'phone', 'email',)

    def clean_phone(self):
        phone_number = self.cleaned_data.get("phone")

        if phone_number:            # 전화번호 형식에 맞게 입력되었는지 검증
            if not re.match(r'^010-\d{4}-\d{4}$', phone_number):
                raise forms.ValidationError('전화번호를 지정된 형식에 맞게 입력해 주세요.') 
        return phone_number

class CustomPasswordChangeForm(PasswordChangeForm):     # 비밀번호 변경
    old_password = forms.CharField(                     # 사용자가 입력한 값 가져오는 과정
        label='현재 비밀번호',
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password'}),
    )
    new_password1 = forms.CharField(
        label='변경할 비밀번호',
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
    )
    new_password2 = forms.CharField(
        label='비밀번호 확인',
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
    )

    def clean_old_password(self):                      # 현재(기존) 비밀번호 맞게 입력했는지 확인
        old_password = self.cleaned_data.get('old_password')
        if not self.user.check_password(old_password):
            raise forms.ValidationError('현재 비밀번호가 올바르지 않습니다.')
        return old_password

    def clean_new_password2(self):                      # 변경할 비밀번호 올바르게 입력되었는지 검증
        new_password1 = self.cleaned_data.get('new_password1')
        new_password2 = self.cleaned_data.get('new_password2')
        if new_password1 and new_password2 and new_password1 != new_password2:
            raise forms.ValidationError('새로운 비밀번호가 일치하지 않습니다.')
        return new_password2



        
