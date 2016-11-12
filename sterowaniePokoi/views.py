from django.shortcuts import render

# Create your views here.

from .models import Sensor,Period
import pyownet

from datetime import datetime

def index(request):
    sensors_list=Sensor.objects.all()
    temp_list=[]
    owproxy=pyownet.protocol.proxy(host="127.0.0.1", port=4304)
    currentTime=datetime.now()
#    for sensor in sensors_list:
#	sensor.temp=float(owproxy.read('/'+sensor.sensorId+'/temperature'))
#        for period in sensor.period_set.all():
#		if period.startHour<=currentTime.hour and period.endHour>currentTime.hour:
#			sensor.setTemp=period.temp
 

    
   
    return render(request,'sterowaniePokoi/list.html',{ 'sensors_list' : sensors_list, 'time': currentTime })
