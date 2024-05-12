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


def get_weather_by_timestamp(begin, end):
    with pool.connection() as conn, conn.cursor() as cs:
        cs.execute("""
            SELECT temp, hum, pres, dp, uvi, cloud, vis, wmain, wdes, Timestamp
            FROM API_weather
            WHERE Timestamp BETWEEN %s AND %s
        """, (begin, end))
        result = [models.Weather(*row) for row in cs.fetchall()]
        return result


