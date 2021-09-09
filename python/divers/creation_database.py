import psycopg2
from subprocess import PIPE,Popen

user_name = 'postgres'
database_name = 'new_brc2'
path_to_dump = 'Z:\BRC-LIMS\Dump\\brc_db.2021-07-20_premaj'
database_password = 'hercule1821'
host_name = 'localhost'
port_name = '5432'

# first we create a new database
# Establishing the connection
connection = psycopg2.connect(user=user_name,
                                password=database_password,
                                host=host_name,
                                port=port_name)
connection.autocommit = True

# Creating a cursor object using the cursor() method
cursor = connection.cursor()

# Creating a database
cursor.execute('DROP DATABASE IF EXISTS '+database_name)
cursor.execute('CREATE database '+database_name)
print("Database created successfully!")

# Closing the connection
connection.close()

# Connect to an existing database

def dump_table(user_name, database_name, path_to_dump, database_password):    
    command = '"C:\Program Files\PostgreSQL\13\bin\psql" -U {0} {1} < {2}'.format(user_name, database_name, path_to_dump)
    p = Popen(command, shell=True, stdin=PIPE, stdout=PIPE, stderr=PIPE)
    return p.communicate('{}\n'.format(database_password).encode('utf-8'))

dump_table(user_name, database_name, path_to_dump, database_password)
print("Data added successfully!")