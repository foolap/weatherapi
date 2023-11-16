from flask import Flask, render_template, request


import json


import urllib.request


app = Flask(__name__)

@app.route('/', methods =['POST', 'GET'])
def weather():
	if request.method == 'POST':
		city = request.form['city']
	else:
		# for default name mathura
		city = 'brno'

	# your API key will come here
	api = '31fe190e3de33f86b2c0eab15a243ae5'



	# source contain json data from api
	source = urllib.request.urlopen(f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api}").read()

	# converting JSON data to a dictionary
	list_of_data = json.loads(source)
	print(list_of_data)

	# data for variable list_of_data
	data = {
		"country_code": str(list_of_data['sys']['country']),
		"cityname": str(list_of_data['name']),

		"coordinate": str(list_of_data['coord']['lon']) + ' '
					+ str(list_of_data['coord']['lat']),
		"temp": str(list_of_data['main']['temp']) + 'k',
		"temp_cel": str(round(list_of_data['main']['temp']-273.15,2)) + '°C',
		"pressure": str(list_of_data['main']['pressure'])+ 'Pa',
		"humidity": str(list_of_data['main']['humidity'])+'%',
	}
	print(data)
	return render_template('index.html', data = data)



if __name__ == '__main__':
	app.run(debug = True)

