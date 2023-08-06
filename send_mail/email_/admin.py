from django.contrib import admin
from .models import Employee, Template, Mail_Logs

# Register your models here.
class Employeeadmin(admin.ModelAdmin):
    list_display = ('employee_name', 'employee_ID', 'email_id', 'birth_date',"join_date")

admin.site.register(Employee, Employeeadmin)

class Templateadmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'subject', 'message')


admin.site.register(Template, Templateadmin)
admin.site.register(Mail_Logs)