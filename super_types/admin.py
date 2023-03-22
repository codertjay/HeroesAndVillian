from django.contrib import admin
from .models import Super, SuperType

# Register your models here.

admin.site.register(SuperType)
admin.site.register(Super)
