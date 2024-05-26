from django.shortcuts import render, redirect

# def mypage(request):
#     if request.method == 'GET':
#         return render(request, 'user/mypage.html')
    
#     elif request.method == 'POST':
#         return 
    

def changepw(request):
    return render(request, 'user/changepw.html')