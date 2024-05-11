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
            SELECT temp, hum, pres, dp, uvi, cloud, vis, main, wdes, timestamp
            FROM weather
        """)
        result = [models.Weather(*row) for row in cs.fetchall()]
        return result

def get_weather_by_timestamp(begin, end):
    with pool.connection() as conn, conn.cursor() as cs:
        cs.execute("""
            SELECT temp, hum, pres, dp, uvi, cloud, vis, main, wdes, timestamp
            FROM weather
            WHERE timestamp BETWEEN %s AND %s
        """, (begin, end))
        result = [models.Weather(*row) for row in cs.fetchall()]
        return result


