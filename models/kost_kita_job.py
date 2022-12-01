import dao


def insertIntoKostKitaJob():

    cnxn = dao.getTargetConnetion()  # get target connection object
    cursor = cnxn.cursor()  # get cursor object

    try:
        sqlQuery = ""
        cursor.execute(sqlQuery)

    except Exception as e:
        print(e)

    cnxn.commit()
    cursor.close()
    cnxn.close()
