from django.contrib import admin
from .models import Task


class ApproveCheckTask(admin.ModelAdmin):
    list_display = ("last_name", "first_name", "surname", "subject", "price_per_hour", "specialization", "experience", "extra_information", "check")
    # list_display = [str(field) for field in Task._meta.get_fields()]

admin.site.register(Task, ApproveCheckTask)


