
from sense_hat import SenseHat
from time import sleep

sense = SenseHat()


yellow = (255, 255, 0)
blue = (0, 0, 255)
y = yellow
b = blue
speed = 0.06

while 1:
	message = "Michigan"
	sense.show_message(message, speed, text_colour=yellow, back_colour=blue)

	t = round(sense.get_temperature(),1)
	p = round(sense.get_pressure(),1)
	h = round(sense.get_humidity(),1)
	msg = "Temperature: {0}, Pressure: {1}, Humidity: {2}".format(t,p,h)
	print(msg)
	
	#o = sense.get_orientation()
	#print("pitch: {pitch}, Yaw: {yaw}, Roll: {roll}".format(**o))
	print(sense.get_gyroscope())

	north = sense.get_compass()
	print("North: %s" % north)

	sleep(0.5)

	message = "Go Big Blue"
	sense.show_message(message, speed, text_colour=yellow, back_colour=blue)

	sleep(0.5)

	TheM = [
	y,y,b,b,b,b,y,y,
	b,y,y,b,b,y,y,b,
	b,y,b,y,y,b,y,b,
	b,y,b,b,b,b,y,b,
	b,y,b,b,b,b,y,b,
	b,y,b,b,b,b,y,b,
	y,y,y,b,b,y,y,y,
	y,y,y,b,b,y,y,y
	]
	sense.set_pixels(TheM)
	sleep(5)
