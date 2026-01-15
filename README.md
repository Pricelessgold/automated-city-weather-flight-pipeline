# 🌍 Automated City Weather & Flight Data Pipeline

## Project Overview
This project implements an **automated, cloud-based data pipeline** that collects, processes, and stores **city demographics, weather forecasts, and flight data** from multiple external sources.

The pipeline is designed to support **scalable analytics and predictive modeling**, such as **urban e-scooter demand forecasting**, by continuously updating structured data in a relational database.

---

## Business Use Case
Urban mobility and logistics applications (e.g., e-scooters, ride-sharing) depend on:
- Weather conditions
- City population characteristics
- Flight arrivals and travel activity

This pipeline provides a **reliable and automated data foundation** for downstream analytics and forecasting models.

---

## Data Sources
- **Wikipedia** — city names, population, geographic coordinates (web scraping)
- **OpenWeatherMap API** — 5-day / 3-hour weather forecasts
- **AeroDataBox API** — real-time flight arrival data

---

## System Architecture & Workflow
1. Web scraping collects city metadata
2. APIs fetch weather forecasts and flight data
3. Python scripts process and normalize incoming data
4. Data is stored in a **MySQL relational database**
5. **Google Cloud Functions** execute ingestion logic
6. **Google Cloud Scheduler** triggers automated updates

---

## Database Design
The relational database schema includes:

- **cities**
  - City name, population, latitude, longitude
- **weather_forecast**
  - Forecast data linked to cities
- **airports**
  - Airport details linked to cities
- **flights**
  - Real-time flight arrivals linked to airports and cities

This structure enables efficient joins and time-based analytics.

---

## Key Features
- Automated data ingestion and updates
- Integration of multiple real-world data sources
- Cloud-based deployment for scalability
- Modular Python functions for maintainability
- Relational schema optimized for analytics

---

## Applications
The collected data can be used for:
- Exploratory data analysis
- Dashboarding and visualization
- Time-series forecasting
- Predictive modeling (e.g., e-scooter demand in urban areas)

---

## Tech Stack
- **Python** — data ingestion, processing, automation  
- **MySQL** — relational data storage  
- **Google Cloud Functions** — serverless execution  
- **Google Cloud Scheduler** — automated pipeline scheduling  
- **APIs** — OpenWeatherMap, AeroDataBox  

