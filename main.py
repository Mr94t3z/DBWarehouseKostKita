import dao
import os
import pandas as pd
import sys
from models import customers as cus
from models import objects as obj
from models import employees as emp
from models import orders as ord

sys.path.insert(0, './models')


# table name target
targetTables = [
    'CUSTOMERS',
    'OBJECTS',
    'EMPLOYEES',
    'ORDERS'
]


def truncateTable(tableName):
    # truncate table
    cnxn = dao.getTargetConnetion()  # get target connection object
    cursor = cnxn.cursor()  # get cursor object

    sqlQuery = f"TRUNCATE TABLE {tableName}"

    cursor.execute(sqlQuery)  # execute query

    cnxn.commit()
    cursor.close()
    cnxn.close()


def fetchRecords(tableName):

    sqlQuery = f"""
                    SELECT *
                    FROM {tableName}
                    WHERE 1 = 1
                """

    cnxn = dao.getSourceConnetion()  # get source connection object
    cursor = cnxn.cursor()  # get cursor object
    cursor.execute(sqlQuery)  # execute query

    KostKitaList = []  # create empty list

    # fetch all records
    for row in cursor:
        KostKitaList.append([elem for elem in row])  # elem = x**2
        # print([elem for elem in row])

    # path to save file
    path = f'./data/'

    # create dataframe
    pd.DataFrame(KostKitaList).iloc[:, :].to_csv(
        os.path.join(path, f'{tableName}.csv'), index=False)

    # close cursor
    cursor.close()

    # close connection
    cnxn.close()


def insertRecords(tableName):
    # insert into target database
    if(tableName == 'CUSTOMERS'):
        cus.insertIntoCustomers(tableName)
    elif(tableName == 'OBJECTS'):
        obj.insertIntoObjects(tableName)
    elif(tableName == 'EMPLOYEES'):
        emp.insertIntoEmployees(tableName)
    elif(tableName == 'ORDERS'):
        ord.insertIntoOrders(tableName)


# loop through table list
for tableName in targetTables:
    print(tableName)
    fetchRecords(tableName)
    truncateTable(tableName)
    insertRecords(tableName)
