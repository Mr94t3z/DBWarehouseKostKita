# import required modules
import mysql.connector
import ConfigParser as cfg


# dbwareshouse source
def getSourceConnetion():

    # database configuration
    config = cfg.ConfigParser()
    config.readfp(open(r'./config/_db.ini'))
    DB_HOST = config.get('DBWarehouse_Source', 'DB_HOST')
    DB_USER = config.get('DBWarehouse_Source', 'DB_USER')
    DB_PASS = config.get('DBWarehouse_Source', 'DB_PASS')
    DB_NAME = config.get('DBWarehouse_Source', 'DB_NAME')

    # create connection object
    cnxn = mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASS,
        database=DB_NAME
    )

    return cnxn


# dbwarehouse target
def getTargetConnetion():

    # database configuration
    config = cfg.ConfigParser()
    config.readfp(open(r'./config/_db.ini'))
    DB_HOST = config.get('DBWarehouse_Target', 'DB_HOST')
    DB_USER = config.get('DBWarehouse_Target', 'DB_USER')
    DB_PASS = config.get('DBWarehouse_Target', 'DB_PASS')
    DB_NAME = config.get('DBWarehouse_Target', 'DB_NAME')

    # create connection object
    cnxn = mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASS,
        database=DB_NAME
    )

    return cnxn
