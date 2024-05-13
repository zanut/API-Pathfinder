
# API-Pathfinder

 | **Contributors**        | **Student ID** |
|:------------------------|:---------------|
| Chanun Suntrapiwat      | 6510545357     |
| Jirapat Chutimantapong  | 6510545292     |

## Project Overview
We try to investigate the relation between traffic and weather by collecting 
the data on traffic like linearX, linearY, LinearZ, Latitude, Longitude ,and Timestamp 
in realtime and change into acceleration and time spent for each time we travel to University.

> We used 2 devices(from each member) to collect the traffic data.

> We collected data from traffic on **Ngamwongwan Road** to the **Kasetsart Intersection** which only includes the section 
that’s around the campus area due to difficulties on data collecting.

## Features
- Visualization Web Application.
- Display statistical number of the data acquired.

**The API would provide:**
Statistical Endpoints of the acquired data included

 **Weather**
- All weather data
- Weather Data for the specified date
- Weather Data for the specified date and hour
- Weather Data between two date-time
- Average weather data for the specified date
- Average weather data for the specified date and hour
- Average weather data between two date-time
- Average weather data with rain-percentage

**Traffic**
- All traffic data
- Traffic data for the specified date
- Traffic data from each device
- Traffic data from each device between two date-time
- Traffic data from each device for the specified date
- Traffic data from each device for the specified weather condition
- Traffic data for the specified TravelID(each time we travel)
- All Calculated Traffic data(acceleration and time spent)
- Calculated Traffic data(acceleration and time spent) for each TravelID

## Libraries and Tools
**Python**
We use Python as a main programming language in our project

**Restful API**
We utilized Restful API to create our API Endpoints


The remaining libraries and tools are available in `requirements.txt` file. 


## Primary Data Source
- [Cedalo MQQT Connect app](https://apps.apple.com/th/app/cedalo-mqtt-connect/id1462295012)

## API and Secondary Data Sources
- [OpenWeatherMap API](https://openweathermap.org/api/one-call-3)


## Setup and Configurations Guide
Here is some guideline on how to setup the project:

### Clone the repository
Open the terminal at the desire directory, and run the following command:
```
> git clone https://github.com/zanut/API-Pathfinder.git
```

After cloning the project. Navigate to the repository with this command:
```
> cd API-Pathfinder
```

### Initialize the Virtual Environment
Generate the virtual environment using the following command:

**Windows**
```
> python -m venv venv
```
**MacOS**
```
> python3 -m venv venv
```

Then after the virtual environment is generated, activate the virtual environment
**Windows**
```
> venv/Scripts/activate
```

**MacOS**
```
> source venv/bin/activate
```
Lastly, install the required packages using the following command:
```
> pip install -r requirements.txt

```


### Configure the `config.py`
1. Duplicate the `config.py.example`. Rename it to `config.py`
2. Fill in the following fields
   - DB_HOST = "[Database Host]"
   - DB_USER = "[KU Nontri Account (b6xxxxxxxxx)]"
   - DB_PASSWD = "[KU Email (@ku.th)]"
   - DB_NAME = "[Database Name]"

### Make sure you are connected to KU or are using KU vpn
you can follow the instruction here:
- [KU VPN](https://vpn.ku.ac.th)

### Stub
- Make the python-flask folder from the [Swagger Editor](https://editor.swagger.io).
- Unzip the file and move the file to the project's directory.

### Start an API connection
In project's directory run:
```
> python3 main.py
```
You'll be able to access the api endpoints via:
```
http://127.0.0.1:8080/pathfinder-api/v1/ui
```

### Connect GraphQL
Open another Terminal, run:
```
> openapi-to-graphql --cors openapi/pathfinder-api.yaml
```
You'll be able to test query in GraphiQL at:
```
http://localhost:3000/graphql
```

### Open Web Application
- Open the index.html file in your preferred browser
