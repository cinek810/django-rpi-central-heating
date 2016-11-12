from django.contrib import admin

# Register your models here.
from .models import Sensor,Period
admin.site.register(Sensor)
admin.site.register(Period)
