from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Post
from django.views.decorators.csrf import csrf_exempt

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('write')
    return render(request, 'main/login.html')

@csrf_exempt
@login_required
def write_post(request):
    if request.method == 'POST':
        print("POST 요청 수신")
        title = request.POST.get('title')
        content = request.POST.get('content')
        print(f"글 작성됨: 제목={title}, 내용={content}")
        Post.objects.create(
            author=request.user,
            title=title,
            content=content
        )

        return HttpResponse("게시글 작성 완료")
    return render(request, 'main/write.html')

def csrf_attack(request):
    return render(request, 'main/attack.html')