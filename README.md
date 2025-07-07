# Rain_Alert_API 🌧️
Open Weather Map API + Mobile phone notification

Rain Alert SMS Notification with Python:
This Python script connects to the "OpenWeatherMap API" to check the weather forecast for the next 3 hours in Zurich, Switzerland. 
The API I used is 5 day forecast that is available at any location on the globe. It includes weather forecast data with 3-hour step.
If rain is predicted, it automatically sends an SMS alert to my phone using the "Twilio API".

-----------------------------------------

How It Works:
1. The script calls the **OpenWeatherMap 5-day Forecast API** with specific latitude and longitude coordinates.
2. It checks the weather condition codes for the next few time slots.
3. If rain is detected (weather_id < 700), it sends an SMS notification with the first expected time of rainfall using "Twilio".

-----------------------------------------

Setup instructions:
1. Install required packages
2. Create .env file with necessary keys
3. Run the code (python Rain_Alert_API.py)

-----------------------------------------

This project demonstrates my ability to:
- Work with APIs (both weather data and SMS)
- Automate notifications using Python
- Write clean, simple code for real-world use cases

## Note:
Sensitive data (API keys, auth_token, phone numbers) are stored in environment variables or a `.env` file (not included for security).
