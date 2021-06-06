
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password, make_password
from .models import Fcuser
from .forms import LoginForm

# Create your views here.

def home(request):
    # user_id = request.session.get('user')

    # if user_id:
    #     fcuser = Fcuser.objects.get(pk=user_id)
    #     return HttpResponse(fcuser.username)

    # return HttpResponse('Home')
    return render(request, 'home.html')

def logout(request):
    if request.session.get('user'):
        del(request.session['user'])
    return redirect('/')

def login(request):
    # if request.method == 'GET':
    #     return render(request, 'login.html')
    # elif request.method == 'POST':
    #     username = request.POST.get('username', None)
    #     password = request.POST.get('password', None)

    #     res_data={}
    #     if not (username and password):
    #         res_data['error'] = '모든 값을 입력해야합니다.'
    #     else:
    #         fcuser = Fcuser.objects.get(username=username)
    #         print(fcuser.password, password)
    #         if check_password(password, fcuser.password):
    #             request.session['user'] = fcuser.id
    #             return redirect('/')
    #             #비밀번호가 일치, 로그인 처리를!
    #         else:
    #             res_data['error'] = '비밀번호를 틀렸습니다'
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            request.session['user'] = form.user_id
            return redirect('/')
    else:
        form = LoginForm()
    
    
    return render(request, 'login.html', {'form': form})

def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    elif request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        re_password = request.POST.get('re-password', None)
        email = request.POST.get('email', None)

        res_data = {}

        if not (username and password and re_password):
            res_data['error'] = '모든 값을 입력해야 합니다'
        elif password != re_password:
            res_data['error'] = '비밀번호가 다릅니다.'
        else:
            fcuser = Fcuser(
                username = username,
                password = make_password(password),
                useremail = email
            )
            fcuser.save()
        return render(request, 'register.html', res_data)