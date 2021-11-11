from django.contrib.auth.views import LoginView
from .models import Task, LeaveFeedBack
from .forms import TaskForm, LeaveFeedBackForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from django.contrib.auth.decorators import login_required



class CustomLoginView(LoginView):
    template_name = 'main/login.html'


def index(request):
    return render(request, "main/index.html")


def about(request):
    tasks = Task.objects.order_by("id")[0:1]
    feedbacks = LeaveFeedBack.objects.order_by("id")
    name = request.user

    context = {
        "title": "Тут ви можете залишити свій коментар про викладача",
        "tasks": tasks,
        "feedbacks": feedbacks,
        "name": name,

    }

    return render(request, "main/about.html", context)


@login_required
def comment(request):
    tasks = Task.objects.order_by("id")[0:1]
    error = ''
    if request.method == "POST":
        form = LeaveFeedBackForm(request.POST)
        if form.is_valid():
            # form.instance.user = request.user
            form.save()
            return redirect('main:home')
        else:
            error = "Форма вказана не вірно"

    form = LeaveFeedBackForm()
    context = {
        "form": form,
        "error": error,
        "title": "Тут ви можете залишити свій коментар про викладача",
        "tasks": tasks,
    }

    return render(request, "main/comment.html", context)


def order(request):
    tasks = Task.objects.order_by("id")
    context = {
        "title": "Головна сторінка сайту",
        "tasks": tasks
    }
    return render(request, "main/order.html", context)


def teachers(request):
    error = ''
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main:home')
        else:
            error = "Форма вказана не вірно"

    form = TaskForm()
    context = {
        "form": form,
        "error": error
    }

    return render(request, "main/teachers.html", context)


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('main:home')
    else:
        form = UserCreationForm()
    return render(request, 'main/register.html', {'form': form})

