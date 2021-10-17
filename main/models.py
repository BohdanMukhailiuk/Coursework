from django.db import models


class Task(models.Model):
    last_name = models.CharField(verbose_name="Прізвище", max_length=50)
    first_name = models.CharField(verbose_name="Ім'я", max_length=50)
    surname = models.CharField(verbose_name="По батькові", max_length=50)
    subject = models.CharField(verbose_name="Назва предмету викладання", max_length=50)
    price_per_hour = models.CharField(verbose_name="Ціна заняття за годину", max_length=50)
    specialization = models.CharField(verbose_name="Напрямок викладання", max_length=50)
    experience = models.CharField(verbose_name="Стаж роботи", max_length=50)
    extra_information = models.TextField(verbose_name="Додаткова інформація")
    check = models.BooleanField(default=False)

    def __str__(self):
        return "{} {} {} {} {}".format(self.last_name, self.first_name, self.surname, self.subject, self.price_per_hour)

    class Meta:
        verbose_name = 'Репетитор'
        verbose_name_plural = 'Репетитори'


