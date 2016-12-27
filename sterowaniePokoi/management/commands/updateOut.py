from django.core.management.base import BaseCommand, CommandError

from sterowaniePokoi.models import Sensor,Period,Pump

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
class Command(BaseCommand):
	help="Update output pin state"
	def handle(self, *args, **options):
		for sensor in Sensor.objects.all():
			state=sensor.getState()
			print str(sensor.getState())+"-"+sensor.name
			try:
				if state  == 0:
					GPIO.setup(sensor.outPin, GPIO.OUT)
					GPIO.output(sensor.outPin,GPIO.LOW)
				elif state == 1:
					GPIO.setup(sensor.outPin, GPIO.OUT)
					GPIO.output(sensor.outPin,GPIO.HIGH)
					print "Turing on pin "+str(sensor.outPin)
			except:
				print "Exception happend"

		for pump in Pump.objects.all():
			print "Checking pump:"+str(pump)
	 		pumpState=0
	 		for sensor in pump.sensor_set.all():
				print "\t Checking Sensor:"+str(sensor)
	 			state=sensor.getState()
	 			if state == 1:
	 				pumpState=1
					print "\t Enabling pump"
	 		if pumpState == 0:
	 				GPIO.setup(pump.outPin, GPIO.OUT)
	 				GPIO.output(pump.outPin,GPIO.LOW)
					print("Pump off, turning off pin:"+str(pump.outPin))
	 		else:
 
	 				GPIO.setup(pump.outPin, GPIO.OUT)
	 				GPIO.output(pump.outPin,GPIO.HIGH)
					print("Pump on, turning on pin:"+str(pump.outPin))

