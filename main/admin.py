from django.contrib import admin
from .models import Task

class ApproveCheckTask(admin.ModelAdmin):
    list_display = ("last_name", "first_name", "surname", "subject", "price_per_hour", "specialization", "experience", "extra_information", "check", 'image')


admin.site.register(Task, ApproveCheckTask)


