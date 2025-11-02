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
from datetime import datetime, timedelta
import keys


#def get_send_flight_data(icao_list):
@functions_framework.http
def get_send_flight_data(request):
  connection_string = create_connection_string()
  flights_arrivals = fetch_flight_data(['EDDH','EDDM'])
  store_flight_data(flights_arrivals, connection_string)
  get_send_airport_data(connection_string)
  return "Flight data fetched and stored successfully."



def create_connection_string():
  schema = "gans_sample_solution"
  host = "35.205.164.253"
  user = "root"
  password = keys.password
  port = 3306
  return f'mysql+pymysql://{user}:{password}@{host}:{port}/{schema}'

def fetch_flight_data(icao_list):
   

    api_key = keys.API_key

    berlin_timezone = timezone('Europe/Berlin')
    today = datetime.now(berlin_timezone).date()
    tomorrow = (today + timedelta(days=1))

    list_for_arrivals_df = []

    for icao in icao_list:
        print(icao)   


        times = [["00:00","11:59"],["12:00","23:59"]]

        for time in times:
            url = f"https://aerodatabox.p.rapidapi.com/flights/airports/icao/{icao}/{tomorrow}T{time[0]}/{tomorrow}T{time[1]}"
            print(url)

            querystring = {"direction":"Arrival","withCancelled":"false"}

            headers = {
                "X-RapidAPI-Key": 'Api_key',
                "X-RapidAPI-Host": "aerodatabox.p.rapidapi.com"
                }

            response = requests.request("GET", url, headers=headers, params=querystring)
            flights_resp = response.json()

            arrivals_df = pd.json_normalize(flights_resp["arrivals"])[["number", "airline.name", "movement.scheduledTime.local", "movement.terminal", "movement.airport.name", "movement.airport.icao"]]
            arrivals_df = arrivals_df.rename(columns={"number": "flight_number", "airline.name": "airline", "movement.scheduledTime.local": "arrival_time", "movement.terminal": "arrival_terminal", "movement.airport.name": "departure_city", "movement.airport.icao": "departure_airport_icao"})
            arrivals_df["arrival_airport_icao"] = icao
            arrivals_df["data_retrieved_on"] = datetime.now(berlin_timezone).strftime("%Y-%m-%d %H:%M:%S")
            arrivals_df = arrivals_df[["arrival_airport_icao", "flight_number", "airline", "arrival_time", "arrival_terminal", "departure_city", "departure_airport_icao", "data_retrieved_on"]]

            # fixing arrival_time
            arrivals_df["arrival_time"] = arrivals_df["arrival_time"].str.split("+").str[0]

            list_for_arrivals_df.append(arrivals_df)
            
    flights_arrivals = pd.concat(list_for_arrivals_df, ignore_index=True)
    flights_arrivals.drop_duplicates(inplace=True)
    return flights_arrivals

    # Send data to database
def store_flight_data(flights_arrivals, connection_string):
  flights_arrivals.to_sql('flight',
                     if_exists='append',
                     con=connection_string,
                     index=False)

def get_send_airport_data(connection_string):
    airport_df = pd.read_sql("select flight_data_id, airline, arrival_airport_icao from flight", con=connection_string)
    airport_df.to_sql('airport', if_exists='append',
                     con=connection_string,
                     index=False)
