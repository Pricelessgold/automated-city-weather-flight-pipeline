CREATE DATABASE gans_sample_solution;

USE gans_sample_solution;

CREATE TABLE cities (
    city_id INT AUTO_INCREMENT,
    city_name VARCHAR(255) NOT NULL,
    country VARCHAR(255),
    latitude FLOAT NOT NULL,
    longitude FLOAT NOT NULL,
    PRIMARY KEY (city_id)
);

CREATE TABLE populations (
    cities_data_id INT AUTO_INCREMENT,
    city_id INT,
    population INT NOT NULL,
    time_stamp DATETIME, 
    PRIMARY KEY (cities_data_id),
    FOREIGN KEY (city_id) REFERENCES cities(city_id)
);

create table weather(
city_id int not null,
temperature float, 
wind_speed float, 
rain_in_last_3h float,
forecast varchar(255),
forecast_time datetime not null,
data_retrieved_at datetime not null,
primary key (city_id, forcast_time),
foreign key(city_id)references cities(city_id)
);

select * from weather;

CREATE TABLE airport (
    airport_id INT AUTO_INCREMENT PRIMARY KEY,
    arrival_airport_icao VARCHAR(10) UNIQUE,
    city_id INT,
    airline varchar(255),
    FOREIGN KEY (city_id) REFERENCES cities(city_id)
);    
  select * from airport;
  drop table airport;
  
    CREATE TABLE flight (
    flight_id INT AUTO_INCREMENT PRIMARY KEY,
    flight_number VARCHAR(255),
    airline VARCHAR(255),
    arrival_time DATETIME NOT NULL,
    arrival_terminal INT,
    departure_city VARCHAR(255),
    data_retrieved_on DATETIME NOT NULL,
    arrival_airport_icao varchar(100),
    departure_airport_icao varchar (100),
    airport_id int,
    FOREIGN KEY (airport_id) REFERENCES airport(airport_id)
    #FOREIGN KEY (arrival_airport_id) REFERENCES airport(airport_id)
);
select * from flight;

