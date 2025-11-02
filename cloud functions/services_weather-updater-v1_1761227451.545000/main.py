import functions_framework
import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.exc import IntegrityError
from lat_lon_parser import parse
from dotenv import load_dotenv
import os
import requests
from pytz import timezone
from datetime import datetime
import keys

@functions_framework.http
def retrieve_and_send_data(request):
  connection_string = create_connection_string()
  cities_df = fetch_cities_data(connection_string)
  weather_df = fetch_weather_data(cities_df)
  store_weather_data(weather_df, connection_string)
  return "Data has been updated"

def create_connection_string():
  schema = "gans_sample_solution"
  host = "35.205.164.253"
  user = "root"
  password = keys.password
  port = 3306
  return f'mysql+pymysql://{user}:{password}@{host}:{port}/{schema}'

def fetch_cities_data(connection_string):
  return pd.read_sql("cities", con=connection_string)
  cities_df = fetch_cities_data(connection_string)
    
def fetch_weather_data(cities_df):
  berlin_timezone = timezone('Europe/Berlin')
  API_key = 'Api_key'
  weather_items = []

  for _, city in cities_df.iterrows():
      latitude = city["latitude"]
      longitude = city["longitude"]
      city_id = city["city_id"]

      url = (f"https://api.openweathermap.org/data/2.5/forecast?lat={latitude}&lon={longitude}&appid={API_key}&units=metric")
      response = requests.get(url)
      weather_data = response.json()

      print(weather_data)

      retrieval_time = datetime.now(berlin_timezone).strftime("%Y-%m-%d %H:%M:%S")

      for item in weather_data["list"]:
          weather_item = {
              "city_id": city_id,
              "forecast_time": item.get("dt_txt"),
              "temperature": item["main"].get("temp"),
              "forecast": item["weather"][0].get("main"),
              "rain_in_last_3h": item.get("rain", {}).get("3h", 0),
              "wind_speed": item["wind"].get("speed"),
              "data_retrieved_at": retrieval_time
          }
          weather_items.append(weather_item)

  weather_df = pd.DataFrame(weather_items)
  weather_df["forecast_time"] = pd.to_datetime(weather_df["forecast_time"])
  weather_df["data_retrieved_at"] = pd.to_datetime(weather_df["data_retrieved_at"])

   
  return weather_df

def store_weather_data(weather_df, connection_string):
  weather_df.to_sql('weather',
                    if_exists='append',
                    con=connection_string,
                    index=False)