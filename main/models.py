from django.contrib.auth.models import User
from django.db import models


class Task(models.Model):
    image = models.ImageField(upload_to='images', blank=True)
    last_name = models.CharField(verbose_name="Прізвище", max_length=50)
    first_name = models.CharField(verbose_name="Ім'я", max_length=50)
    surname = models.CharField(verbose_name="По батькові", max_length=50)
    choose_subject = models.CharField(verbose_name="Предмет", max_length=16, null=True)
    price_per_hour = models.CharField(verbose_name="Ціна заняття за годину у грн", max_length=50)
    specialization = models.CharField(verbose_name="Напрямок викладання", max_length=50)
    experience = models.IntegerField(verbose_name="Стаж роботи(у місяцях)")
    extra_information = models.TextField(verbose_name="Додаткова інформація")
    check = models.BooleanField(default=False)
    email = models.EmailField(verbose_name="Електронна пошта", max_length=254, null=True)

    def __str__(self):
        return "{} {} {} {} {}".format(self.last_name, self.first_name, self.surname, self.price_per_hour, self.image)

    class Meta:
        verbose_name = 'Репетитор'
        verbose_name_plural = 'Репетитори'


class LeaveFeedBack(models.Model):
    feedback = models.TextField(verbose_name="Ви можете зилишити свій коментар тут", null=True)
    check = models.BooleanField(default=False, null=True)
    task = models.ForeignKey(Task, null=True, on_delete=models.CASCADE)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)


