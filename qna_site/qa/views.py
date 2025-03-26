from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("안녕하세요 qa에 오신것을 환영합니다 by 이지상_20213060")