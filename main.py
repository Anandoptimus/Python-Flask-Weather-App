import requests
from flask import Flask, render_template, request, redirect
from key import api_key

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        city = request.form['city']
        parameter = {
            "q": city,
            'appid': api_key
        }
        req = requests.get(url="https://api.openweathermap.org/data/2.5/weather", params=parameter)
        req.raise_for_status()
        name = req.json()['name']
        lat = req.json()['coord']['lat']
        lon = req.json()['coord']['lon']
        weather = req.json()['weather'][0]['description']
        temp = req.json()['main']['temp']
        pressure = req.json()['main']['pressure']
        humidity = req.json()['main']['humidity']
        country = req.json()['sys']['country']
        return render_template("message.html", name=name, lat=lat, lon=lon,
                               weather=weather, temp=temp, pressure=pressure,
                               humidity=humidity, country=country)

    return render_template("index.html")








if __name__ == "__main__":
    app.run(debug=True)

# {'coord': {'lon': 80.2785, 'lat': 13.0878}, 'weather': [{'id': 701, 'main': 'Mist', 'description': 'mist', 'icon': '50d'}],
# 'base': 'stations', 'main': {'temp': 302.04, 'feels_like': 306.57, 'temp_min': 302.04, 'temp_max': 303.14, 'pressure': 1016, 'humidity': 75},
# 'visibility': 5000, 'wind': {'speed': 3.09, 'deg': 150}, 'clouds': {'all': 40}, 'dt': 1708320695, 'sys': {'type': 2, 'id': 2092109, 'country': 'IN',
# 'sunrise': 1708304422, 'sunset': 1708346732}, 'timezone': 19800, 'id': 1264527, 'name': 'Chennai', 'cod': 200}