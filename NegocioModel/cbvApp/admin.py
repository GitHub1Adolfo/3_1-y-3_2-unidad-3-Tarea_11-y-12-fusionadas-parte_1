from django.contrib import admin
from cbvApp.models import Student

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'score']

admin.site.register(Student, StudentAdmin)
