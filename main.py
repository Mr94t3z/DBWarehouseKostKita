import dao
import pandas as pd

# table name target
targetTables = [
    'CUSTOMERS',
    'OBJECTS',
    'EMPLOYEES',
    'ORDERS'
]


def frecthRecords(tableName):

    sqlQuery = f"""
                    SELECT *
                    FROM {tableName}
                    WHERE 1 = 1
                """

    cnxn = dao.getSourceConnetion()  # get connection object
    cursor = cnxn.cursor()  # get cursor object
    cursor.execute(sqlQuery)  # execute query

    KostKitaList = []  # create empty list

    # fetch all records
    for row in cursor:
        KostKitaList.append([elem for elem in row])  # elem = x**2
        print([elem for elem in row])

    # create dataframe
    pd.DataFrame(KostKitaList).iloc[:, :].to_csv(
        f'{tableName}.csv', index=False)

    # close cursor
    cursor.close()

    # close connection
    cnxn.close()


# loop through table list
for tableName in targetTables:
    frecthRecords(tableName)
    print(tableName)
