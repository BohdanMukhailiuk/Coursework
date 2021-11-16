from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from .models import Task, LeaveFeedBack
from .forms import TaskForm, LeaveFeedBackForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect, get_object_or_404
from .forms import SignUpForm
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm
from django.contrib.auth.decorators import login_required


class CustomLoginView(LoginView):
    template_name = 'main/login.html'


def index(request):

    context = {
        "title": "Головна сторінка сайту",

    }
    return render(request, "main/index.html", context)


def about(request, pk):
    tasks = Task.objects.filter(id=pk)
    feedbacks = LeaveFeedBack.objects.filter(task_id=pk)
    context = {
        "title": "Тут ви можете залишити свій коментар про викладача",
        "tasks": tasks,
        "feedbacks": feedbacks,

    }

    return render(request, "main/about.html", context)


@login_required
def comment(request, pk):
    tasks = Task.objects.filter(id=pk)
    task = Task.objects.get(id=pk)
    user = User.objects.get(id=request.user.id)
    error = ''
    if request.method == "POST":
        form = LeaveFeedBackForm(request.POST)
        if form.is_valid():
            saved_form = form.save(commit=False)
            saved_form.user = user
            saved_form.task = task
            saved_form.save()
            return redirect('main:about', pk=pk)
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
    if request.GET.get('price_per_hour'):
        price_per_hour_filter = request.GET.get('price_per_hour')
        print(price_per_hour_filter)

        if "+" in price_per_hour_filter:
            prices = price_per_hour_filter[:-1]
            print(prices)
            min_price = int(prices[0])
            max_price = int(prices[0]*10)
        else:
            prices = price_per_hour_filter.split("-")
            print(prices)
            min_price = int(prices[0])
            max_price = int(prices[1])

        listings = Task.objects.filter(price_per_hour__range=(min_price, max_price), )
        print(listings)

    else:
        listings = Task.objects.all()

    context = {
        "title": "Головна сторінка сайту",
        "tasks": tasks,
        'listings': listings
    }
    return render(request, "main/order.html", context)


def teachers(request):
    error = ''
    if request.method == "POST":
        form = TaskForm(request.POST)
        print(Task.objects.all())
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


def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect("main:home")

