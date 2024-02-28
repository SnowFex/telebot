from database.config import host, user, password, port, db_name
import mysql.connector
from getpass import getpass




try:
    connection = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        port=port,
        database=db_name
    )
    print('successfully connected')
except Exception as e:
    print(e)

try:
    mycursor = connection.cursor()
    create_table_query = """CREATE TABLE IF NOT EXISTS weaher (id INT, name VARCHAR(100), city VARCHAR(50), PRIMARY KEY (id))"""
    mycursor.execute(create_table_query)
    connection.commit()

    #def insert_table(self, id, name, city):
       ##insert_table_query = """INSERT INTO weaher (id, name, city) VALUES (%s, %s, %s)"""
       # val = [(register_name)]
       # mycursor.execute(insert_table_query)
       # connection.commit()


except mysql.connector.Error as error:
    print(error)

except Exception as ex:
    print('Connection')
    print(ex)