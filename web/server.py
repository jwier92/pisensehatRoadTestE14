from flask import Flask, flash, redirect, render_template, request, session, abort, jsonify
from sense_hat import SenseHat

app = Flask(__name__, static_url_path='')

sense = SenseHat()	

@app.route("/")
def index():
	tempC = round(sense.get_temperature(),1)
	humidity = round(sense.get_humidity(),1)
	pressure = round(sense.get_pressure(),1)
	return render_template('index.html',temperature=tempC,humidity=humidity,
		pressure=pressure) 

@app.route("/api/temperature")
def apiTemperature():
	tempC = round(sense.get_temperature(),1)
	return str(tempC)

 
@app.route("/api/humidity")
def apiHumidity():
	humidity = round(sense.get_humidity(),1)
	return str(humidity)

@app.route("/api/pressure")
def apiPressure():
	pressure = round(sense.get_pressure(),1)
	return str(pressure)

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=5000)

