
# API-Pathfinder

 | **Contributors**        | **Student ID** |
|:------------------------|:---------------|
| Chanun Suntrapiwat      | 6510545357     |
| Jirapat Chutimantapong  | 6510545292     |

## Abstract
This project is a part of the year project of  ***Data Acquisition and Integration***, 
***Data Analytics***, and ***Software Testing*** course Kasetsart University.

Our project aims to collect data to study the possible effects of traffic around 
Kasetsart University (Computer Department) that potentially cause air/noise pollution.

Our goal is to study the correlations between the acquired data using the 
knowledge on data acquisition and analytics.

> By the “traffic around Kasetsart University”, we refer to the traffic on 
**Ngamwongwan Road** to the **Kasetsart Intersection** which only includes the section 
that’s around the campus area due to difficulties on data collecting.

## Features
**Trafica web-application would provide the following:**
- Visualize the the acquired Traffic Flow, Air Quality, Noise Pollution data around the Computer Engineering Dept. Kasetsart University
- Display statistical number of the data acquired

**The API would provide:**
Statistical Endpoints of the acquired data included

 **Weather**
- 

**Traffic**
- 


## Libraries and Tools
**Python**
We use Python as a main programming language in our project

**Restful API**
We utilized Restful API to create our API Endpoints

**Swagger**

**GraphQL**

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
>
```

After cloning the project. Navigate to the repository with this command:
```
>
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

*Credit: MacOS guide were originated from this [Medium article][^1]*

[^1]: <https://medium.com/datacat/a-simple-guide-to-creating-a-virtual-environment-in-python-for-windows-and-mac-1079f40be518> "A simple guide to creating a virtual environment in Python for Windows and Mac"

### Configure the `config.py`
1. Duplicate the `config.py.example`. Rename it to `config.py`
2. Fill in the following fields
   - DB_HOST = "[Database Host]"
   - DB_USER = "[KU Nontri Account (b6xxxxxxxxx)]"
   - DB_PASSWD = "[KU Email (@ku.th)]"
   - DB_NAME = "[Database Name]"

### Start an App
> For KU students, make sure that you have turned on the VPN connection to 
> connect to the database

#### To start an API connection
```
> 
```
You'll be able to access the api endpoints via
```

```
