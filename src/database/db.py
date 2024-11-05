import pymysql
from  pymysql import Error


def get_connection():
    try:
        return pymysql.connect(
            host='database-diseno.cf42aq24umw7.us-west-1.rds.amazonaws.com',
            port= 3306,
            user='admin',
            password='diseno1234',
            db= 'tecDB'
        )
    except Error as ex:
        raise ex

