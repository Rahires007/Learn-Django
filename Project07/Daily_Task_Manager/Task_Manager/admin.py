from django.contrib import admin
from .models import Task_Manager

# Register your models here.
class Task_ManagerAdmin(admin.ModelAdmin):
    list_display=('Task','Status','Added_Date','Updated_Date')  #Display Fields of Tables
    search_fields=('Task',)  #Implements Search Functionality Inside admin panel
admin.site.register(Task_Manager,Task_ManagerAdmin)