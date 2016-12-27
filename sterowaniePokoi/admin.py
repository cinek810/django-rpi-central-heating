from django.contrib import admin

# Register your models here.
from .models import Sensor,Period,Pump
admin.site.register(Sensor)
admin.site.register(Period)
admin.site.register(Pump)
