from django.core.management.base import BaseCommand, CommandError

from sterowaniePokoi.models import Sensor,Period,Pump

from time import gmtime, strftime

from influxdb import InfluxDBClient


class Command (BaseCommand):
	help="Update historical data in influxDBA"
	def handle (self,*args,**options):
		for sensor in Sensor.objects.all():
		    temp=sensor.getTemp()
		    
		    host = 'localhost'
		    port = 8086
		    user = ''
		    password = ''
		    dbname = 'temps'
		    timestring=strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
		    json_body = [
			{
			    "measurement": "temp",
			    "tags": {
				"room": sensor.name,
                                "pump": sensor.pumpId,
			    },
			    "time": timestring,
			    "fields": {
				"temp": temp,
			    }
			}
		    ]

		    client = InfluxDBClient(host, port, user, password, dbname)

		    client.write_points(json_body)

