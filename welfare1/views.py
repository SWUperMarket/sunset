# welfare_app/views.py

from django.shortcuts import render

def index(request):
    return render(request, 'welfare1/condense_main.html')



def page2(request):
    return render(request, 'welfare1/page2.html')
from django.shortcuts import render


def policy_main(request) :
    return render(request, 'welfare1/policy_main.html')


def policy_01(request):
    return render(request, 'welfare1/01.html')

def policy_02(request):
    return render(request, 'welfare1/02.html')

def policy_03(request):
    return render(request, 'welfare1/03.html')

def policy_04(request):
    return render(request, 'welfare1/04.html')

def policy_05(request):
    return render(request, 'welfare1/05.html')

def policy_06(request):
    return render(request, 'welfare1/06.html')

def policy_07(request):
    return render(request, 'welfare1/07.html')

def policy_08(request):
    return render(request, 'welfare1/08.html')

def policy_09(request):
    return render(request, 'welfare1/09.html')

def policy_10(request):
    return render(request, 'welfare1/10.html')

def policy_11(request):
    return render(request, 'welfare1/11.html')

def policy_12(request):
    return render(request, 'welfare1/12.html')

def protect(request):
    return render(request, 'welfare1/13.html')
def home(request):
    return render(request, 'welfare1/14.html')


def welfare_detail(request):
    return render(request, 'welfare1/15.html')

def senior_class(request):
    return render(request, 'welfare1/16.html')
def nursing(request):
    return render(request, 'welfare1/17.html')