# Flask Weather App

## Description
This is a simple Flask web application that retrieves weather information for a given city using the OpenWeatherMap API. Users can input a city name, and the application displays details such as temperature, weather description, and location coordinates.

## Features
- Retrieves weather information using OpenWeatherMap API
- Displays temperature, weather description, location coordinates, and other details for a given city
- Simple web interface for user interaction

## Installation
1. **Clone the repository:**
   ```bash
   git clone https://github.com/Anandoptimus/Day96.git
   ```
   
2. **Navigate to the project directory:**
   ```bash
   cd Day96
   ```
   
3. **Install dependencies:**
   ```bash
   pip install Flask requests
   ```
   
4. **Run the application:**
   ```bash
   python main.py
   ```

## Usage
1. Access the web application by visiting [http://localhost:5000](http://localhost:5000) in your web browser.
2. Enter the name of the city in the provided form.
3. Click the "Get Weather" button to retrieve and display weather information.

## Configuration
- Obtain an API key from [OpenWeatherMap](https://openweathermap.org/api) and replace the placeholder in the `key.py` file with your actual API key.

## Files
- `app.py`: Flask application script
- `key.py`: File containing the OpenWeatherMap API key (add this to your `.gitignore` to keep it private)
- `templates/index.html`: HTML template for the main page
- `templates/message.html`: HTML template for displaying weather information

## Dependencies
- Flask
- Requests

## Contribution
Feel free to contribute to the project by opening issues or submitting pull requests.

## License
This project is licensed under the [MIT License](LICENSE).

   
