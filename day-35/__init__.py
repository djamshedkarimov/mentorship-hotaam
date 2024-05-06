import requests
from twilio.rest import Client
'''importing modules'''

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "0d7c0cde4345ce3d69d519a78cc1c95c"
account_sid = "AC462a8a290c93f8a96f553ca0259cf9b3"
auth_token = "7909e5bf1534350407d8a065104a637b"
'''my twilio information'''

weather_params = {
    "lat": 46.947975,
    "lon": 7.447447,
    "appid": api_key,
    "cnt": 4,
}
'''the weather parameters for response'''

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
# print(weather_data["list"][0]["weather"][0]["id"])

will_rain = False
for hour_data in weather_data["list"]:
    '''for every hour in weather data list'''
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
        '''if condition code less than 700 minutes, it will rain'''
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an ☔️",
        from_="+18777804236",
        to="9499961930"
        '''if will_rain (true), send message!!!'''
    )
    print(message.status)