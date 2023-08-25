from tkinter import *
import requests
import json
from datetime import datetime

#Initialize Window
 
root =Tk()
root.geometry("400x400") #size of the window by default
root.resizable(0,0) #to make the window size fixed
#title of our window
root.title("Weather Widget")

city_value = StringVar()
 
def showWeather():
 
    api_key = "953b11a3b6f8b95ba99dba79daaf66de"  #sample API
 
    # Get city name from user from the input field 
    city_name=city_value.get()
 
    # API url
    weather_url = 'http://api.openweathermap.org/data/2.5/weather?q=' + city_name + '&appid='+api_key
 
    # Get response from fetched url
    response = requests.get(weather_url)
 
    # change response from JSON to python 
    weather_info = response.json()
 
 
    tfield.delete("1.0", "end")   #to clear the text field for each new output
 
#if the cod is 200, it means that weather data was successfully fetched
 
 
    if weather_info['cod'] == 200:
        kelvin = 273 # value of kelvin
 
#-----------Storing the fetched values 
        def time_format_for_location(utc_with_tz):
            local_time = datetime.utcfromtimestamp(utc_with_tz) 
            return local_time.time()
        temp = int(weather_info['main']['temp'] - kelvin)                                     #converting default kelvin value to Celcius
        feels_like_temp = int(weather_info['main']['feels_like'] - kelvin)
        temp_fahrenheit = int(temp * 9/5 + 32)
        feels_like_temp_fahrenheit = int(feels_like_temp * 9/5 + 32)
        pressure = weather_info['main']['pressure']
        humidity = weather_info['main']['humidity']
        wind_speed = weather_info['wind']['speed'] * 3.6
        sunrise = weather_info['sys']['sunrise']
        sunset = weather_info['sys']['sunset']
        timezone = weather_info['timezone']
        cloudy = weather_info['clouds']['all']
        description = weather_info['weather'][0]['description']
        sunrise_time = time_format_for_location(sunrise + timezone)
        sunset_time = time_format_for_location(sunset + timezone)
 
#assigning Values to our weather varaible, to display as output
         
        weather = f"\nWeather of: {city_name}\nTemperature (Celsius): {temp}°\nFeels like in (Celsius): {feels_like_temp}°\nTemperature (Fahrenheit): {temp_fahrenheit}°\nFeels like in (Fahrenheit): {feels_like_temp_fahrenheit}°\nPressure: {pressure} hPa\nHumidity: {humidity}%\nSunrise at {sunrise_time} and Sunset at {sunset_time}\nCloud: {cloudy}%\nInfo: {description}"
    else:
        weather = f"\n\tWeather for '{city_name}' not found!\n\tKindly Enter valid City Name !!"
 
 
 
    tfield.insert(INSERT, weather)   #to insert or send value in our Text Field to display output

city_head= Label(root, text = 'Enter City Name', font = 'OpenSans 12 bold').pack(pady=10) 
 
inp_city = Entry(root, textvariable = city_value,  width = 24, font='OpenSans 14 bold').pack() #entry field

Button(root, command = showWeather, text = "Check Weather", font="OpenSans 10", bg='lightblue', fg='black', activebackground="teal", padx=5, pady=5 ).pack(pady= 20)

weather_now = Label(root, text = "The Weather is: ", font = 'arial 12 bold').pack(pady=10)
 
tfield = Text(root, width=46, height=10)
tfield.pack()

root.mainloop()