
from sense_hat import SenseHat
from time import sleep

sense = SenseHat()


yellow = (255, 255, 0)
blue = (0, 0, 255)
y = yellow
b = blue
speed = 0.1

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
