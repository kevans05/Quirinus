import datetime
import sqlite3
import os

from GCWeatherScrap import download_gc_weather

WeatherStationDatabase = sqlite3.connect('WeatherStationDatabase.db').cursor()
WeatherStationDatabase.execute('''CREATE TABLE stocks (Date DATETIME, Temp_C real, DewPointTemp_C real, StnPress_kPa real, Hmdx real)''')

class_weather = download_gc_weather.canadian_weather()
x = class_weather.read_multiple_month_from_gc(station=10999, dt_start=datetime.datetime(year=1990,month=1,day=2))

for j in x:
    print(j["Date"], j["Temp_C"], j["DewPointTemp_C"], j["StnPress_kPa"], j["Hmdx"])
    WeatherStationDatabase.execute("INSERT INTO stocks VALUES (?,?,?,?,?)", [j["Date"], j["Temp_C"], j["DewPointTemp_C"], j["StnPress_kPa"], j["Hmdx"]])
WeatherStationDatabase.close()