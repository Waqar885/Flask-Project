# Weather App

A Flask-based web application to retrieve and display current weather information for any city worldwide. The app uses the OpenWeatherMap API to fetch real-time weather data and presents it in a user-friendly interface.

## Features

- Search for weather information by city name.
- Displays temperature, humidity, wind speed, and weather conditions.
- Shows a weather icon representing the current condition.
- Responsive design using Bootstrap.

## Technologies Used

- **Python** (Flask Framework)
- **HTML** (with Jinja2 templating)
- **CSS** (Bootstrap and custom styles)
- **JavaScript** (Bootstrap Bundle)
- **OpenWeatherMap API** for weather data

## File Structure

```
weather-app/
|-- app.py               # Main Flask application
|-- templates/
|   |-- base.html        # Base template
|   |-- weather.html     # Weather display page
|-- static/
|   |-- Design.css       # Custom CSS file
|-- secret_key.py        # API key file (excluded from the repository)
```

## How to Run Locally

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/weather-app.git
   cd weather-app
   ```

2. Install dependencies:

   ```bash
   pip install flask requests
   ```

3. Obtain an API key from [OpenWeatherMap](https://openweathermap.org/) and add it to a file named `secret_key.py` in the project directory:

   ```python
   # secret_key.py
   key = "your_api_key_here"
   ```

4. Run the application:

   ```bash
   python app.py
   ```

5. Open a web browser and go to `http://127.0.0.1:5000` to access the app.

## Usage

- Enter a city name in the search bar to fetch the weather information.
- The app displays the weather data, including:
  - City name
  - Temperature (in Celsius)
  - Feels like temperature (in Fahrenheit)
  - Humidity (in percentage)
  - Wind speed (in km/h)
  - Weather condition description and icon

## Screenshots

*Include screenshots of your app running locally.*

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Feel free to fork this repository and submit pull requests for improvements or new features.

---

Built with ❤️ by Waqar Raza using Flask.

