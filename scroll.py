
from sense_hat import SenseHat

sense = SenseHat()

yellow = (255, 255, 0)
blue = (0, 0, 255)

message = "Jason Wier is my name!"

speed = 0.05
sense.show_message(message, speed, text_colour=yellow, back_colour=blue)
