import dao

# get connection object
cnxn = dao.getSourceConnetion()

# create cursor object
cursor = cnxn.cursor()

# query to execute
query = "SELECT * FROM ORDERS"

# executing cursor
cursor.execute(query)

# display all records
table = cursor.fetchall()

for row in table:
    print('data = %r' % (row,))
