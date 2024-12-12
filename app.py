from flask import Flask, render_template, request
import requests
from secret_key import key

app = Flask(__name__)

@app.route('/')
def main():
    return render_template("index.html")

@app.route('/weather', methods=["POST", 'GET'])
def weather():
    if request.method == "POST":
        User_city = request.form['city']

        weather_data = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={User_city}&appid={key}')

        if weather_data.status_code != 200:
            return render_template('weather.html', error="Location not found.")
        else:
            response = weather_data.json()
            weathers = {
            "city": response["name"],
            "temperature": str(int(response["main"]["temp"]) - 273),
            "feels_like": str(1.8 * (int(response["main"]["feels_like"])-273) +32),
            "humidity": response["main"]["humidity"],
            "wind_speed": response["wind"]["speed"],
            "condition": response["weather"][0]["description"].capitalize(),
            "icon_url": f"http://openweathermap.org/img/wn/{response['weather'][0]['icon']}@2x.png"
            }
            return render_template('weather.html', weather=weathers)
    
    return("index.html")

if __name__=="__main__":
    app.run(debug=True)