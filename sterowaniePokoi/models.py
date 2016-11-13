from __future__ import unicode_literals

from django.db import models

import pyownet

from datetime import datetime

# Create your models here.
class Sensor(models.Model):
	sensorId=models.CharField(max_length=30)
	name=models.CharField(max_length=40,default="Nieznany opis")
	setTemp=models.FloatField(default=19)
	tolerance=models.FloatField(default=0.5)
	outPin=models.IntegerField(default=-1)
	
	def __str__(self):
		return self.name+" ID:"+self.sensorId
	def getTemp(self):
		owproxy=pyownet.protocol.proxy(host="127.0.0.1", port=4304)
		return round(float(owproxy.read('/'+self.sensorId+'/temperature')),1)
	def getSetTemp(self):
		currentTime=datetime.now()
		setTemp=self.setTemp
		for period in self.period_set.all():
			if period.startHour<=currentTime.hour and period.endHour>currentTime.hour:
				setTemp=period.temp
		return setTemp

	def getState(self):
		setTemp=self.getSetTemp()
		currTemp=self.getTemp()
		if setTemp-self.tolerance > currTemp:
			return 1
		elif setTemp+self.tolerance <  currTemp:
			return 0
		else:
			return 2
	def periodsByStart(self):
		return self.period_set.order_by('startHour')

		
		
		

class Period(models.Model):
	sensor=models.ForeignKey(Sensor, on_delete=models.CASCADE)
	startHour=models.IntegerField()
	endHour=models.IntegerField()
	temp=models.IntegerField()
	def __str__(self):
		return self.sensor.name+" Start:"+str(self.startHour)+" End:"+str(self.endHour)+" Temp:"+str(self.temp)
	def clean(self):
		if self.endHour <= self.startHour:
			raise ValueError("End >= Start")
		for period in self.sensor.period_set.all():
			if (self.startHour>=period.startHour and self.startHour<period.endHour ) or ( self.endHour <= period.endHour and self.endHour>period.startHour):
				raise ValueError("Overlaps with different period")
