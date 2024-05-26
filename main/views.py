import json
from django.shortcuts import render

def index(request):
    # JSON 파일 열기
    with open('secret.json', encoding='utf-8') as json_file:
        data = json.load(json_file)
    
    # API 키 추출
    apikey = data['API_KEY']
    apidict = []
    for openai in apikey:
        content = {
            "apikey": str(openai['API_KEY']),    
        }
        apidict.append(content)
    
    # JSON 문자열로 변환
    openaiJson = json.dumps(apidict)
    
    # 템플릿에 데이터 전달
    return render(request, 'main/index.html', {'openaiJson': openaiJson})
