from django.contrib import admin
from appResume.models import Student

# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'message']


admin.site.register(Student, StudentAdmin)    