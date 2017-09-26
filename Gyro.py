
from sense_hat import SenseHat
from time import sleep

sense = SenseHat()


while 1:
	orientation = sense.get_orientation()
	x = round(orientation['pitch'],2)
	y = round(orientation['roll'],2)
	z = round(orientation['yaw'],2)
	print("x={0}, y={1}, z={2}".format(x,y,z))
	sleep(0.01)
