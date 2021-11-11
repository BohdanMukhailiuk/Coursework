from .models import Task, LeaveFeedBack
from django.forms import ModelForm, TextInput, Textarea, CheckboxInput
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ["first_name", "last_name", "surname", "subject", "price_per_hour", "specialization", "experience", "extra_information", "check", "image"]
        widgets = {

            "last_name": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Введіть ваше прізвище"
            }),

            "first_name": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Введіть ваше ім'я"
            }),

            "surname": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Введіть ваше ім'я по батькові"
            }),

            "subject": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Введіть предмет, який викладатимете"
            }),

            "price_per_hour": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Введіть ціну вашого заняття за годину"
            }),

            "specialization": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Введіть напрямок викладання"
            }),

            "experience": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Введіть стаж роботи"
            }),

            "extra_information": Textarea(attrs={
                "class": "form-control",
                "placeholder": "Введіть додаткову інформацію про себе"
            }),

            "check": CheckboxInput(attrs={
                "class": "form-control",
            }),



        }


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class LeaveFeedBackForm(ModelForm):
    class Meta:
        model = LeaveFeedBack
        fields = ("feedback", )
        widgets = {

            "feedback": Textarea(attrs={
                "class": "form-control",
                "placeholder": "Залишіть свій коментар тут"
            }),

        }


