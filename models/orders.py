import dao
import os
import pandas as pd


def insertIntoOrders(tableName):

    cnxn = dao.getTargetConnetion()  # get target connection object
    cursor = cnxn.cursor()  # get cursor object

    # path to import file
    path = f'./data/'

    # read csv file
    df = pd.read_csv(os.path.join(path, f'{tableName}.csv'))
    df.fillna('', inplace=True)

    # loop through each row
    for i, row in df.iterrows():

        try:
            sqlQuery = "INSERT INTO `ORDERS`(`orderID`, `employeeID`, `customerID`, `objectID`, `startAt`, `endAt`) VALUES (" + \
                "%s,"*(len(row)-1) + "%s)"
            cursor.execute(sqlQuery, tuple(row))

        except Exception as e:
            print(e)

    cnxn.commit()
    cursor.close()
    cnxn.close()
