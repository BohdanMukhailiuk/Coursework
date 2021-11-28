from django.contrib import admin
from .models import Task
from .models import LeaveFeedBack

class ApproveCheckTask(admin.ModelAdmin):
    list_display = ("last_name", "first_name", "surname", "choose_subject", "price_per_hour", "specialization",
                    "experience", "extra_information", "check", 'image')


class ApproveCheckLeaveFeedBack(admin.ModelAdmin):
    list_display = ('user', 'feedback', "check")


admin.site.register(Task, ApproveCheckTask)
admin.site.register(LeaveFeedBack, ApproveCheckLeaveFeedBack)

