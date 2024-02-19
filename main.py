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
