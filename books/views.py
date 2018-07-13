from django.shortcuts import render, redirect
from django.views import View
from books.models import Person
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

# Create your views here.

class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('home')
            else:
                return redirect('login')
        else:
            redirect('login')
        return redirect('home')


class RegisterUserView(View):
    def get(self, request):
        return render(request, 'register.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username and password:
            user_exists = User.objects.filter(username=username)
            if user_exists:
                print('User exists so i am not doing anything...')
            else:
                new_user = User.objects.create_user(username=username, password=password)
                new_profile = Person.objects.create(user=new_user)
        return redirect('login')


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login')


class HomeView(LoginRequiredMixin, View):
    login_url = 'login'

    def get(self, request):
        user = request.user
        ctx = {
            user: 'user',
        }
        return render(request, 'home.html', ctx)

    def post(self, request):
        pass
