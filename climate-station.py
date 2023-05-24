import serial
import requests

# Establish serial connection
ser = serial.Serial('COM1', 9600)  # Replace 'COM1' with the appropriate serial port

# Loop to continuously receive data
while True:
    data = ser.readline().decode().strip()  # Read data from the serial port and decode it

    if data == 'ta':  # High traffic on Street A
        print("High traffic on Street A")
    elif data == 'tt':  # High traffic in tunnel
        print("High traffic in tunnel")
    elif data == 'gw':  # Get weather
        print("Getting weather data...")

        # Call OpenWeatherMap API
        url = 'https://api.openweathermap.org/data/2.5/weather'
        params = {
            'lat': '51.509865',
            'lon': '-0.118092',
            'appid': '35033edc5bae430e28bc567c9d680056',
            'units': 'metric'
        }

        try:
            response = requests.get(url, params=params)
            response.raise_for_status()  # Check for any request errors
            weather_data = response.json()  # Process weather data as needed
            print("Weather data:", weather_data)
        except requests.exceptions.RequestException as e:
            print("Failed to retrieve weather data:", e)
    else:
        # Invalid data received
        print("Invalid data received:", data)

# Close the serial connection (unreachable in this infinite loop)
ser.close()
