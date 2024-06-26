import sys
import traceback

from flask import abort
import pymysql
from dbutils.pooled_db import PooledDB
from config import OPENAPI_STUB_DIR, DB_HOST, DB_USER, DB_PASSWD, DB_NAME

sys.path.append(OPENAPI_STUB_DIR)
from swagger_server import models

pool = PooledDB(creator=pymysql,
                host=DB_HOST,
                user=DB_USER,
                password=DB_PASSWD,
                database=DB_NAME,
                maxconnections=1,
                blocking=True)


def get_weather():
    with pool.connection() as conn, conn.cursor() as cs:
        cs.execute("""
            SELECT Timestamp, wmain, wdes, temp, hum, pres, dp, uvi, cloud, vis
            FROM API_weather
        """)
        result = [models.Weather(*row) for row in cs.fetchall()]
        return result


def get_weather_unique_date():
    with pool.connection() as conn, conn.cursor() as cs:
        cs.execute("""
            SELECT DISTINCT DATE(Timestamp)
            FROM API_weather
        """)
        result = [models.WeatherUniqueDate(*row) for row in cs.fetchall()]
        return result


def get_weather_by_date(date):
    with pool.connection() as conn, conn.cursor() as cs:
        cs.execute("""
            SELECT Timestamp, wmain, wdes, temp, hum, pres, dp, uvi, cloud, vis
            FROM API_weather
            WHERE DATE(Timestamp) = %s
            ORDER BY Timestamp ASC
        """, (date,))
        result = [models.Weather(*row) for row in cs.fetchall()]
        return result


def get_weather_by_date_hour(date, hour):
    with pool.connection() as conn, conn.cursor() as cs:
        cs.execute("""
            SELECT Timestamp, wmain, wdes, temp, hum, pres, dp, uvi, cloud, vis
            FROM API_weather
            WHERE DATE(Timestamp) = %s
            AND HOUR(Timestamp) = %s
        """, (date, hour))
        result = [models.Weather(*row) for row in cs.fetchall()]
        return result


def get_weather_between_timestamps(begin, end):
    with pool.connection() as conn, conn.cursor() as cs:
        cs.execute("""
            SELECT Timestamp, wmain, wdes, temp, hum, pres, dp, uvi, cloud, vis
            FROM API_weather
            WHERE Timestamp BETWEEN %s AND %s
        """, (begin, end))
        result = [models.Weather(*row) for row in cs.fetchall()]
        return result


def get_average_weather_by_date(date):
    with pool.connection() as conn, conn.cursor() as cs:
        cs.execute("""
            SELECT
                wmain,
                ROUND(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM API_weather WHERE DATE(Timestamp) = %s), 4) AS occurrence_percentage,
                ROUND(AVG(temp), 4) AS avg_temp, 
                ROUND(AVG(hum), 4) AS avg_hum, 
                ROUND(AVG(pres), 4) AS avg_pres, 
                ROUND(AVG(dp), 4) AS avg_dp, 
                ROUND(AVG(uvi), 4) AS avg_uvi, 
                ROUND(AVG(cloud), 4) AS avg_cloud, 
                ROUND(AVG(vis), 4) AS avg_vis
            FROM API_weather
            WHERE DATE(Timestamp) = %s
            GROUP BY wmain
        """, (date, date))
        result = [models.AverageWeather(*row) for row in cs.fetchall()]
        return result


def get_average_weather_by_date_hour(date, hour):
    with pool.connection() as conn, conn.cursor() as cs:
        cs.execute("""
            SELECT
                wmain,
                ROUND(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM API_weather WHERE DATE(Timestamp) = %s AND HOUR(Timestamp) = %s), 4) AS occurrence_percentage,
                ROUND(AVG(temp), 4) AS avg_temp, 
                ROUND(AVG(hum), 4) AS avg_hum, 
                ROUND(AVG(pres), 4) AS avg_pres, 
                ROUND(AVG(dp), 4) AS avg_dp, 
                ROUND(AVG(uvi), 4) AS avg_uvi, 
                ROUND(AVG(cloud), 4) AS avg_cloud, 
                ROUND(AVG(vis), 4) AS avg_vis
            FROM API_weather
            WHERE DATE(Timestamp) = %s AND HOUR(Timestamp) = %s
            GROUP BY wmain
        """, (date, hour, date, hour))
        result = [models.AverageWeather(*row) for row in cs.fetchall()]
        return result


def get_average_weather_between_timestamp(begin, end):
    with pool.connection() as conn, conn.cursor() as cs:
        cs.execute("""
            SELECT
                wmain,
                ROUND(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM API_weather WHERE Timestamp >= %s AND Timestamp <= %s), 4) AS occurrence_percentage,
                ROUND(AVG(temp), 4) AS avg_temp, 
                ROUND(AVG(hum), 4) AS avg_hum, 
                ROUND(AVG(pres), 4) AS avg_pres, 
                ROUND(AVG(dp), 4) AS avg_dp, 
                ROUND(AVG(uvi), 4) AS avg_uvi, 
                ROUND(AVG(cloud), 4) AS avg_cloud, 
                ROUND(AVG(vis), 4) AS avg_vis
            FROM API_weather
            WHERE Timestamp >= %s AND Timestamp <= %s
            GROUP BY wmain
        """, (begin, end, begin, end))
        result = [models.AverageWeather(*row) for row in cs.fetchall()]
        return result


def get_average_weather_with_rain_percent():
    with pool.connection() as conn, conn.cursor() as cs:
        cs.execute("""
            SELECT
                DATE(Timestamp) AS date,
                ROUND(AVG(temp), 4) AS avg_temp, 
                ROUND(AVG(hum), 4) AS avg_hum, 
                ROUND(AVG(pres), 4) AS avg_pres, 
                ROUND(AVG(dp), 4) AS avg_dp, 
                ROUND(AVG(uvi), 4) AS avg_uvi, 
                ROUND(AVG(cloud), 4) AS avg_cloud, 
                ROUND(AVG(vis), 4) AS avg_vis,
                ROUND(SUM(CASE WHEN wmain = 'Rain' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) AS rain_percentage
            FROM API_weather
            GROUP BY DATE(Timestamp)
        """)
        result = [models.AverageWeatherRainPercent(*row) for row in cs.fetchall()]
        return result


def get_traffic_all():
    with pool.connection() as conn, conn.cursor() as cs:
        cs.execute("""
            SELECT Timestamp, Latitude, Longitude, DeviceID, Acceleration
            FROM Updated_GPS_tracker
        """)
        result = [models.Traffic(*row) for row in cs.fetchall()]
        return result


def get_devices():
    with pool.connection() as conn, conn.cursor() as cs:
        cs.execute("""
            SELECT DISTINCT DeviceID
            FROM Updated_GPS_tracker
        """)
        result = [models.Device(*row) for row in cs.fetchall()]
        return result


def get_traffic_by_device(device_id):
    with pool.connection() as conn, conn.cursor() as cs:
        cs.execute("""
            SELECT Timestamp, Latitude, Longitude, DeviceID, Acceleration
            FROM Updated_GPS_tracker
            WHERE DeviceID = %s
        """, (device_id,))
        result = [models.Traffic(*row) for row in cs.fetchall()]
        return result


def get_traffic_by_device_timestamp(device_id, begin, end):
    with pool.connection() as conn, conn.cursor() as cs:
        cs.execute("""
            SELECT Timestamp, Latitude, Longitude, DeviceID, Acceleration
            FROM Updated_GPS_tracker
            WHERE DeviceID = %s
            AND Timestamp BETWEEN %s AND %s
        """, (device_id, begin, end))
        result = [models.Traffic(*row) for row in cs.fetchall()]
        return result


def get_traffic_by_device_date(device_id, date):
    with pool.connection() as conn, conn.cursor() as cs:
        cs.execute("""
            SELECT Timestamp, Latitude, Longitude, DeviceID, Acceleration
            FROM Updated_GPS_tracker
            WHERE DeviceID = %s
            AND DATE(Timestamp) = %s
        """, (device_id, date))
        result = [models.Traffic(*row) for row in cs.fetchall()]
        return result


def get_traffic_by_device_weather(device_id, wmain):
    with pool.connection() as conn, conn.cursor() as cs:
        cs.execute("""
            SELECT t.Timestamp, t.Latitude, t.Longitude, t.DeviceID, t.Acceleration
            FROM API_weather w
            INNER JOIN Updated_GPS_tracker t
            ON ABS(TIMESTAMPDIFF(SECOND, t.`Timestamp`, w.`Timestamp`)) <= 300
            WHERE t.DeviceID = %s
            AND w.wmain = %s
        """, (device_id, wmain))
        result = [models.Traffic(*row) for row in cs.fetchall()]
        return result


def get_traffic_unique_dates():
    with pool.connection() as conn, conn.cursor() as cs:
        cs.execute("""
            SELECT DISTINCT DATE(Timestamp) as date
            FROM Updated_GPS_tracker
        """)
        result = [models.UniqueDate(*row) for row in cs.fetchall()]
        return result


def get_traffic_by_date(date):
    with pool.connection() as conn, conn.cursor() as cs:
        cs.execute("""
            SELECT Timestamp, Latitude, Longitude, DeviceID, Acceleration
            FROM Updated_GPS_tracker
            WHERE DATE(Timestamp) = %s
        """, (date,))
        result = [models.Traffic(*row) for row in cs.fetchall()]
        return result


def get_traffic_unique_travel_id():
    with pool.connection() as conn, conn.cursor() as cs:
        cs.execute("""
            SELECT DISTINCT TravelID
            FROM Updated_GPS_tracker
            ORDER BY TravelID ASC
        """)
        result = [models.UniqueTravelID(*row) for row in cs.fetchall()]
        return result


def get_traffic_by_travel_id(travel_id):
    with pool.connection() as conn, conn.cursor() as cs:
        cs.execute("""
            SELECT Timestamp, Latitude, Longitude, DeviceID, Acceleration
            FROM Updated_GPS_tracker
            WHERE TravelID = %s
        """, (travel_id,))
        result = [models.Traffic(*row) for row in cs.fetchall()]
        return result


def get_traffic_details():
    with pool.connection() as conn, conn.cursor() as cs:
        cs.execute("""
            SELECT 
                TravelID AS travelID,
                MIN(Timestamp) AS startTime,
                MAX(Timestamp) AS endTime,
                ROUND(AVG(Acceleration), 4) AS avg_acceleration,
                TIMESTAMPDIFF(MINUTE, MIN(Timestamp), MAX(Timestamp)) AS time_spent
            FROM Updated_GPS_tracker
            GROUP BY TravelID
        """)
        result = [models.DetailsTraffic(*row) for row in cs.fetchall()]
        return result


def get_traffic_details_by_travel_id(travel_id):
    with pool.connection() as conn, conn.cursor() as cs:
        cs.execute("""
            SELECT 
                %s AS travelID,
                MIN(Timestamp) AS startTime,
                MAX(Timestamp) AS endTime,
                ROUND(AVG(Acceleration), 4) AS avg_acceleration, 
                TIMESTAMPDIFF(MINUTE, MIN(Timestamp), MAX(Timestamp)) AS time_spent
            FROM Updated_GPS_tracker
            WHERE TravelID = %s
        """, (travel_id, travel_id,))
        result = [models.DetailsTraffic(*row) for row in cs.fetchall()]
        return result


def get_traffic_details_by_weather(wmain):
    with pool.connection() as conn, conn.cursor() as cs:
        cs.execute("""
            SELECT 
                TravelID AS travelID,
                MIN(t.Timestamp) AS startTime,
                MAX(t.Timestamp) AS endTime,
                ROUND(AVG(Acceleration), 4) AS avg_acceleration, 
                TIMESTAMPDIFF(MINUTE, MIN(t.Timestamp), MAX(t.Timestamp)) AS time_spent,
                %s AS wmain
            FROM API_weather w
            INNER JOIN Updated_GPS_tracker t
            ON ABS(TIMESTAMPDIFF(SECOND, t.`Timestamp`, w.`Timestamp`)) <= 300
            WHERE w.wmain = %s
            GROUP BY TravelID
        """, (wmain, wmain))
        result = [models.DetailsTrafficWeather(*row) for row in cs.fetchall()]
        return result


def get_weather_condition_by_time(time):
    with pool.connection() as conn, conn.cursor() as cs:
        cs.execute("""
            SELECT Timestamp, wmain, wdes, temp, hum, pres, dp, uvi, cloud, vis
            FROM API_weather
            ORDER BY ABS(TIMESTAMPDIFF(SECOND, %s, Timestamp))
            LIMIT 1
        """, (time,))
        result = [models.Weather(*row) for row in cs.fetchall()]
        return result
