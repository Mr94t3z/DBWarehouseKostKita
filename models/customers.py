import dao
import os
import pandas as pd


def insertIntoCustomers(tableName):

    cnxn = dao.getTargetConnetion()  # get target connection object
    cursor = cnxn.cursor()  # get cursor object

    # path to import file
    path = f'./data/'

    # read csv file
    df = pd.read_csv(os.path.join(path, f'{tableName}.csv'))
    df.fillna('', inplace=True)

    # loop through each row
    for i, row in df.iterrows():
        sqlQuery = "INSERT INTO `CUSTOMERS`(`customerID`, `customerName`, `phone`, `city`) VALUES (" + \
            "%s,"*(len(row)-1) + "%s)"
        cursor.execute(sqlQuery, tuple(row))

    cnxn.commit()
    cursor.close()
    cnxn.close()
