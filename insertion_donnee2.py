import psycopg2
import mysql.connector
from pymongo import MongoClient


def test_postgresql_insert():
    conn = psycopg2.connect(
        host="localhost",
        database="mydatabase",
        user="myuser",
        password="mypassword"
    )
    cur = conn.cursor()
    cur.execute("INSERT INTO mytable (id, name) VALUES (4, 'John');")
    conn.commit()
    print("Inserted data into PostgreSQL")
    conn.close()


def test_mysql_insert():
    conn = mysql.connector.connect(
        host="localhost",
        database="mydatabase",
        user="myuser",
        password="mypassword"
    )
    cur = conn.cursor()
    cur.execute("INSERT INTO mytable (id, name) VALUES (4, 'John');")
    conn.commit()
    print("Inserted data into MySQL")
    conn.close()



def create_table_mysql():
    conn = mysql.connector.connect(
        host="localhost",
        database="mydatabase",
        user="myuser",
        password="mypassword"
    )
    cur = conn.cursor()
    cur.execute("CREATE TABLE mytable (id INT PRIMARY KEY, name VARCHAR(255));")
    conn.commit()
    conn.close()

import psycopg2

def create_table_postgresql():
    conn = psycopg2.connect(
        host="localhost",
        database="mydatabase",
        user="myuser",
        password="mypassword"
    )
    cur = conn.cursor()
    cur.execute("CREATE TABLE mytable (id SERIAL PRIMARY KEY, name VARCHAR(255));")
    conn.commit()
    conn.close()




if __name__ == "__main__":
    create_table_mysql()
    create_table_postgresql()


    

    test_postgresql_insert()
    test_mysql_insert()
    

