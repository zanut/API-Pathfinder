import sys
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
            SELECT temp, hum, pres, dp, uvi, cloud, vis, wmain, wdes, Timestamp
            FROM API_weather
        """)
        result = [models.Weather(*row) for row in cs.fetchall()]
        return result


def get_weather_by_date(date):
    with pool.connection() as conn, conn.cursor() as cs:
        cs.execute("""
            SELECT temp, hum, pres, dp, uvi, cloud, vis, wmain, wdes, Timestamp
            FROM API_weather
            WHERE DATE(Timestamp) = %s
        """, (date,))
        result = [models.Weather(*row) for row in cs.fetchall()]
        return result


def get_weather_by_date_hour(date, hour):
    with pool.connection() as conn, conn.cursor() as cs:
        cs.execute("""
            SELECT temp, hum, pres, dp, uvi, cloud, vis, wmain, wdes, Timestamp
            FROM API_weather
            WHERE DATE(Timestamp) = %s
            AND HOUR(Timestamp) = %s
        """, (date, hour))
        result = [models.Weather(*row) for row in cs.fetchall()]
        return result


def get_weather_between_timestamps(begin, end):
    with pool.connection() as conn, conn.cursor() as cs:
        cs.execute("""
            SELECT temp, hum, pres, dp, uvi, cloud, vis, wmain, wdes, Timestamp
            FROM API_weather
            WHERE Timestamp BETWEEN %s AND %s
        """, (begin, end))
        result = [models.Weather(*row) for row in cs.fetchall()]
        return result


def get_average_weather_by_date(date):
    with pool.connection() as conn, conn.cursor() as cs:
        cs.execute("""
            SELECT 
                ROUND(AVG(temp), 4) AS avg_temp, 
                ROUND(AVG(hum), 4) AS avg_hum, 
                ROUND(AVG(pres), 4) AS avg_pres, 
                ROUND(AVG(dp), 4) AS avg_dp, 
                ROUND(AVG(uvi), 4) AS avg_uvi, 
                ROUND(AVG(cloud), 4) AS avg_cloud, 
                ROUND(AVG(vis), 4) AS avg_vis,
                wmain,
                ROUND(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM API_weather WHERE DATE(Timestamp) = %s), 4) AS occurrence_percentage
            FROM API_weather
            WHERE DATE(Timestamp) = %s
            GROUP BY wmain
        """, (date, date))
        result = [{
            'wmain': row[7],
            'occurrence_percentage': row[8],
            'avg_temp': row[0],
            'avg_hum': row[1],
            'avg_pres': row[2],
            'avg_dp': row[3],
            'avg_uvi': row[4],
            'avg_cloud': row[5],
            'avg_vis': row[6]
        } for row in cs.fetchall()]
        return result


