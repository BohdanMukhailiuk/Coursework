import csv

from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.http import HttpResponse

from .models import Task, LeaveFeedBack
from .forms import TaskForm, LeaveFeedBackForm
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
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
    min_exp = 0
    max_exp = 100000000000000
    min_price = 0
    max_price = 10000000000000
    choose_subject_filter = request.GET.get("choose_subject")
    specialization = request.GET.get("specialization")
# 0
    listings = Task.objects.all()

# 1
    if request.GET.get('price_per_hour') and request.GET.get('choose_subject') and request.GET.get('experience') \
            and request.GET.get('specialization'):

        specialization_filter = request.GET.get("specialization")
        print(specialization_filter)

        choose_subject_filter = request.GET.get("choose_subject")
        print(choose_subject_filter)

        experience_filter = request.GET.get('experience')
        print(experience_filter.split("-"))
        min_exp = int(experience_filter.split("-")[0])
        max_exp = int(experience_filter.split("-")[1].split(" ")[0])
        print(min_exp)
        print(max_exp)

        price_per_hour_filter = request.GET.get('price_per_hour')
        print(price_per_hour_filter)

        if "+" in price_per_hour_filter:
            prices = price_per_hour_filter[:-1]
            min_price = int(prices[0])
            max_price = int(prices[0] * 10)
        else:
            prices = price_per_hour_filter.split("-")
            min_price = int(prices[0])
            max_price = int(prices[1])

        listings = Task.objects.filter(choose_subject__contains=choose_subject_filter,
                                       experience__range=(min_exp, max_exp),
                                       price_per_hour__range=(min_price, max_price),
                                       specialization__contains=specialization_filter)

# 2
    elif request.GET.get('price_per_hour') and request.GET.get('choose_subject') and request.GET.get('experience'):

        choose_subject_filter = request.GET.get("choose_subject")
        print(choose_subject_filter)

        experience_filter = request.GET.get('experience')
        print(experience_filter.split("-"))
        min_exp = int(experience_filter.split("-")[0])
        max_exp = int(experience_filter.split("-")[1].split(" ")[0])
        print(min_exp)
        print(max_exp)

        price_per_hour_filter = request.GET.get('price_per_hour')
        print(price_per_hour_filter)

        if "+" in price_per_hour_filter:
            prices = price_per_hour_filter[:-1]
            min_price = int(prices[0])
            max_price = int(prices[0] * 10)
        else:
            prices = price_per_hour_filter.split("-")
            min_price = int(prices[0])
            max_price = int(prices[1])

        listings = Task.objects.filter(choose_subject__contains=choose_subject_filter,
                                       experience__range=(min_exp, max_exp),
                                       price_per_hour__range=(min_price, max_price), )
# 3
    elif request.GET.get('price_per_hour') and request.GET.get('choose_subject') and request.GET.get('specialization'):

        specialization_filter = request.GET.get("specialization")
        print(specialization_filter)

        choose_subject_filter = request.GET.get("choose_subject")
        print(choose_subject_filter)

        price_per_hour_filter = request.GET.get('price_per_hour')
        print(price_per_hour_filter)

        if "+" in price_per_hour_filter:
            prices = price_per_hour_filter[:-1]
            min_price = int(prices[0])
            max_price = int(prices[0] * 10)
        else:
            prices = price_per_hour_filter.split("-")
            min_price = int(prices[0])
            max_price = int(prices[1])

        listings = Task.objects.filter(choose_subject__contains=choose_subject_filter,
                                       price_per_hour__range=(min_price, max_price),
                                       specialization__contains=specialization_filter)
# 4
    elif request.GET.get('choose_subject') and request.GET.get('experience') and request.GET.get('specialization'):

        specialization_filter = request.GET.get("specialization")
        print(specialization_filter)

        choose_subject_filter = request.GET.get("choose_subject")
        print(choose_subject_filter)

        experience_filter = request.GET.get('experience')
        print(experience_filter.split("-"))
        min_exp = int(experience_filter.split("-")[0])
        max_exp = int(experience_filter.split("-")[1].split(" ")[0])
        print(min_exp)
        print(max_exp)

        listings = Task.objects.filter(choose_subject__contains=choose_subject_filter,
                                       experience__range=(min_exp, max_exp),
                                       specialization__contains=specialization_filter)
# 5
    elif request.GET.get('price_per_hour') and request.GET.get('experience') and request.GET.get('specialization'):

        specialization_filter = request.GET.get("specialization")
        print(specialization_filter)

        experience_filter = request.GET.get('experience')
        print(experience_filter.split("-"))
        min_exp = int(experience_filter.split("-")[0])
        max_exp = int(experience_filter.split("-")[1].split(" ")[0])
        print(min_exp)
        print(max_exp)

        price_per_hour_filter = request.GET.get('price_per_hour')
        print(price_per_hour_filter)

        if "+" in price_per_hour_filter:
            prices = price_per_hour_filter[:-1]
            min_price = int(prices[0])
            max_price = int(prices[0] * 10)
        else:
            prices = price_per_hour_filter.split("-")
            min_price = int(prices[0])
            max_price = int(prices[1])

        listings = Task.objects.filter(experience__range=(min_exp, max_exp),
                                       price_per_hour__range=(min_price, max_price),
                                       specialization__contains=specialization_filter)

# 6
    elif request.GET.get('price_per_hour') and request.GET.get('choose_subject'):
        choose_subject_filter = request.GET.get("choose_subject")
        print(choose_subject_filter)

        price_per_hour_filter = request.GET.get('price_per_hour')
        print(price_per_hour_filter)

        if "+" in price_per_hour_filter:
            prices = price_per_hour_filter[:-1]
            min_price = int(prices[0])
            max_price = int(prices[0] * 10)
        else:
            prices = price_per_hour_filter.split("-")
            min_price = int(prices[0])
            max_price = int(prices[1])

        listings = Task.objects.filter(choose_subject__contains=choose_subject_filter,
                                       price_per_hour__range=(min_price, max_price), )
# 7
    elif request.GET.get('price_per_hour') and request.GET.get('experience'):
        price_per_hour_filter = request.GET.get('price_per_hour')
        print(price_per_hour_filter)

        if "+" in price_per_hour_filter:
            prices = price_per_hour_filter[:-1]
            min_price = int(prices[0])
            max_price = int(prices[0] * 10)
        else:
            prices = price_per_hour_filter.split("-")
            min_price = int(prices[0])
            max_price = int(prices[1])

        experience_filter = request.GET.get('experience')
        print(experience_filter.split("-"))
        min_exp = int(experience_filter.split("-")[0])
        max_exp = int(experience_filter.split("-")[1].split(" ")[0])
        print(min_exp)
        print(max_exp)

        listings = Task.objects.filter(price_per_hour__range=(min_price, max_price),
                                       experience__range=(min_exp, max_exp), )
# 8
    elif request.GET.get('price_per_hour') and request.GET.get('specialization'):
        price_per_hour_filter = request.GET.get('price_per_hour')
        print(price_per_hour_filter)

        if "+" in price_per_hour_filter:
            prices = price_per_hour_filter[:-1]
            min_price = int(prices[0])
            max_price = int(prices[0] * 10)
        else:
            prices = price_per_hour_filter.split("-")
            min_price = int(prices[0])
            max_price = int(prices[1])

        specialization_filter = request.GET.get('specialization')

        listings = Task.objects.filter(specialization__contains=specialization_filter,
                                       price_per_hour__range=(min_price, max_price), )



# 9
    elif request.GET.get('choose_subject') and request.GET.get('experience'):
        choose_subject_filter = request.GET.get("choose_subject")
        print(choose_subject_filter)

        experience_filter = request.GET.get('experience')
        print(experience_filter.split("-"))
        min_exp = int(experience_filter.split("-")[0])
        max_exp = int(experience_filter.split("-")[1].split(" ")[0])
        print(min_exp)
        print(max_exp)

        listings = Task.objects.filter(choose_subject__contains=choose_subject_filter,
                                       experience__range=(min_exp, max_exp), )

# 10
    elif request.GET.get('specialization') and request.GET.get('experience'):
        specialization_filter = request.GET.get("specialization")

        experience_filter = request.GET.get('experience')
        print(experience_filter.split("-"))
        min_exp = int(experience_filter.split("-")[0])
        max_exp = int(experience_filter.split("-")[1].split(" ")[0])
        print(min_exp)
        print(max_exp)

        listings = Task.objects.filter(specialization__contains=specialization_filter,
                                       experience__range=(min_exp, max_exp), )

# 11
    elif request.GET.get('choose_subject') and request.GET.get('specialization'):
        choose_subject_filter = request.GET.get("choose_subject")
        specialization_filter = request.GET.get('specialization')

        listings = Task.objects.filter(choose_subject__contains=choose_subject_filter,
                                       specialization__contains=specialization_filter,)

# 12
    elif request.GET.get('specialization'):
        specialization_filter = request.GET.get("specialization")
        listings = Task.objects.filter(specialization__contains=specialization_filter)

# 13
    elif request.GET.get('choose_subject'):
        choose_subject_filter = request.GET.get("choose_subject")
        listings = Task.objects.filter(choose_subject__contains=choose_subject_filter)
# 14
    elif request.GET.get('experience'):
        experience_filter = request.GET.get('experience')
        print(experience_filter.split("-"))
        min_exp = int(experience_filter.split("-")[0])
        max_exp = int(experience_filter.split("-")[1].split(" ")[0])
        print(min_exp)
        print(max_exp)
        listings = Task.objects.filter(experience__range=(min_exp, max_exp))
# 15
    elif request.GET.get('price_per_hour'):
        price_per_hour_filter = request.GET.get('price_per_hour')
        print(price_per_hour_filter)

        if "+" in price_per_hour_filter:
            prices = price_per_hour_filter[:-1]
            min_price = int(prices[0])
            max_price = int(prices[0] * 10)
        else:
            prices = price_per_hour_filter.split("-")
            min_price = int(prices[0])
            max_price = int(prices[1])
        listings = Task.objects.filter(price_per_hour__range=(min_price, max_price))

    context = {
        "title": "Головна сторінка сайту",
        "tasks": tasks,
        'listings': listings,
    }

    return render(request, "main/order.html", context)


def teachers(request):
    error = ''
    if request.method == "POST":
        form = TaskForm(request.POST, request.FILES)
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


def export_products_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="products.csv"'

    writer = csv.writer(response)
    writer.writerow(["first_name", "last_name", "surname", "email", "choose_subject", "price_per_hour",
                  "specialization", "experience", "extra_information"])

    tasks = Task.objects.all().values_list("first_name", "last_name", "surname", "email", "choose_subject", "price_per_hour",
                  "specialization", "experience", "extra_information")
    for task in tasks:
        writer.writerow(task)

    return response

