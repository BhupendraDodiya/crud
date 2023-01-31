from django.contrib import admin
from . models import *

# Register your models here.
@admin.register((User))
class UserModelAdmin(admin.ModelAdmin):
    list_display = ['id','name','contact','email','password','DOB']