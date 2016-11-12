from django.core.management.base import BaseCommand, CommandError

from sterowaniePokoi.models import Sensor,Period

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
