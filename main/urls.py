from django.urls import path
from main import views


app_name = "main"

urlpatterns = [

    path('', views.index, name="home"),
    path('about', views.about, name="about"),
    path('order', views.order, name="order"),
    path('teachers', views.teachers, name="teachers"),
    path('register', views.register, name="register"),
    path('login', views.user_login, name="login"),

]
