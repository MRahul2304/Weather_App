
Weather Application
This is a simple weather application built using Python's Tkinter library and OpenWeatherMap API. 
It allows users to input a city name and retrieve weather information including weather climate, 
description, temperature, and pressure.

Features:
- City Selection: Users can select a city from a dropdown list of Indian states and union territories.
- Weather Information: Upon clicking the "DONE" button, the application fetches weather data from the OpenWeatherMap API based on the selected city and displays it on the interface.
- Display: Weather climate, description, temperature, and pressure are displayed in separate labels.

 Prerequisites:
- Python 3.x
- tkinter library
- requests library

 Installation:
1. Clone or download the repository to your local machine.
2. Install the required libraries:

    ```
    pip install requests
    ```
3. Run the application:

    ```
    python weather_app.py
    ```

 Usage:
1. Launch the application.
2. Select a city from the dropdown list.
3. Click the "DONE" button to fetch and display weather information for the selected city.

 API Key:
This application uses the OpenWeatherMap API to fetch weather data. Make sure to replace the API key (`"d02413acddc678cecfb11417c4c2f096"`) in the `dataget()` function with your own API key. You can sign up for a free API key [here](https://openweathermap.org/api).

 Notes:
- The temperature is displayed in Celsius.
- Pressure is displayed in hPa (hectopascals).

