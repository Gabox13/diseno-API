import pymysql
from  pymysql import Error


def get_connection():
    try:
        return pymysql.connect(
            host='baseweb.c7cqs2suad72.us-east-2.rds.amazonaws.com',
            port= 3306,
            user='admin',
            password='dgrf1234',
            db= 'tecDB'
        )
    except Error as ex:
        raise ex

