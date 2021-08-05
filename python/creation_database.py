import psycopg2

# first we create a new database
# Establishing the connection
connection = psycopg2.connect(user="postgres",
                                password="hercule1821",
                                host="localhost",
                                port="5432")
connection.autocommit = True

# Creating a cursor object using the cursor() method
cursor = connection.cursor()

# Preparing query to create a database
sql = '''CREATE database new_brc4'''

# Creating a database
name_db = 'new_brc4'
cursor.execute('DROP DATABASE IF EXISTS '+name_db)
cursor.execute('CREATE database '+name_db)
print("Database created successfully!")

# Closing the connection
connection.close()

"""
# Connect to an existing database
connection2 = psycopg2.connect(user="postgres",
                                password="hercule1821",
                                host="localhost",
                                port="5432",
                                database="new_brc4")


# and then we fill it with the dump of BECLims
# Create a cursor to perform database operations
cursor2 = connection2.cursor()

cursor2.execute(open("Z:\BRC-LIMS\Dump\\brc_db.sql", "r", encoding='UTF-8').read())
print("Data added successfully!")

# Closing the connection
connection2.close()
"""
