from django import forms
from qna.models import Question


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question  # 사용할 모델
        fields = ['subject', 'content']
        labels = {
            'subject': '제목',
            'content': '내용',
        }  