# import required modules
import mysql.connector
import ConfigParser as cfg


# define class to connect to database
def getSourceConnetion():

    # database configuration
    config = cfg.ConfigParser()
    config.readfp(open(r'config.ini'))
    DB_HOST = config.get('DBWarehouse', 'DB_HOST')
    DB_USER = config.get('DBWarehouse', 'DB_USER')
    DB_PASS = config.get('DBWarehouse', 'DB_PASS')
    DB_NAME = config.get('DBWarehouse', 'DB_NAME')

    # create connection object
    cnxn = mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASS,
        database=DB_NAME
    )

    return cnxn
