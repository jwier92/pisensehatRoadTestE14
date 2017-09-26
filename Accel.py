
from sense_hat import SenseHat
from time import sleep

sense = SenseHat()


while 1:
	accel = sense.get_accelerometer_raw()
	x = round(accel['x'],0)
	y = round(accel['y'],0)
	z = round(accel['z'],0)
	print("x={0}, y={1}, z={2}".format(x,y,z))
	sleep(0.01)
