from django.contrib import admin
from . import models
# Register your models here.


admin.AdminSite.register(models.Shelter)
admin.AdminSite.register(models.Dog)

