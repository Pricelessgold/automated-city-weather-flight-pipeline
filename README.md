# Automated-City-Weather-Flight-Pipeline
Automated data pipeline to collect, process, and store city, weather, and flight data. Built with Python, MySQL, and Google Cloud, this project enables scalable, cloud-based integration of multiple data sources to support analytics and predictive modeling, such as e-scooter demand forecasting.



 
 ## Features
- Web scraping of city names, population, and geographic coordinates from Wikipedia.  
- Integration with **OpenWeatherMap API** to fetch 5-day, 3-hour weather forecasts.  
- Real-time flight data collection via **AeroDataBox API**.  
- Structured **MySQL relational database** linking cities, weather, and flights.  
- Cloud deployment using **Google Cloud Functions** and **Cloud Scheduler** for automated updates.  
- Modular Python functions for easy maintenance and scalability.

  The relational database includes the following tables:  

1. **cities**: Stores city names, population, and coordinates.  
2. **weather_forecast**: Stores weather data linked to cities.  
3. **airports**: Stores airport information linked to cities.  
4. **flights**: Stores real-time flight arrivals linked to airports and cities.


## Usage

Once deployed, the pipeline automatically fetches and updates:

City demographics

Weather forecasts

Flight arrivals

This data can then be used for analytics, visualizations, or predictive modeling, e.g., predicting e-scooter demand in urban area
