from django.urls import path
from main import views


app_name = "main"

urlpatterns = [

    path('', views.index, name="home"),
    path('about', views.about, name="about"),
    path('about/<int:pk>/', views.about, name="about"),
    path('comment/<int:pk>/', views.comment, name="comment"),
    path('comment', views.comment, name="comment"),
    path('order', views.order, name="order"),
    path('teachers', views.teachers, name="teachers"),
    path('register', views.register, name="register"),
    path('login', views.CustomLoginView.as_view(), name="login"),
    path('logout', views.logout_request, name="logout"),

]
