from os import error
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import auth
from django.views.decorators.csrf import csrf_exempt



# Create your views here.
@csrf_exempt
def signup(request):
    try:
        if request.method == 'POST':
            if request.POST['password1'] == request.POST['password2']:
                user = User.objects.create_user(request.POST['username'],request.POST['password1'])
                auth.login(request, user)
                return redirect('recommend')
            else:
                return render(request, 'signup.html', {'error': '비밀번호가 일치하지 않습니다.'})
        return render(request, 'signup.html')
    except(User.DoesNotExist):
        return render(request, 'signup.html',{'id':'아이디를 입력 하세요'})
    except(TypeError, ValueError, OverflowError):
        return render(request, 'signup.html',{'error':'칸을 입력 하세요'})
    
@csrf_exempt
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('recommend')
        else:
            return render(request, 'login.html', {'error': 'username or password is incorrect.'})
    else:
        return render(request, 'login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('recommend')
    return render(request, 'login.html')