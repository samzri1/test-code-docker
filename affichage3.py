import psycopg2
import mysql.connector
from pymongo import MongoClient


def test_postgresql():
    conn = psycopg2.connect(
        host="localhost",
        database="mydatabase",
        user="myuser",
        password="mypassword"
    )
    cur = conn.cursor()
    cur.execute("SELECT version();")
    ver = cur.fetchone()
    print("PostgreSQL version: ", ver)
    
    cur.execute("SELECT * FROM mytable;")
    rows = cur.fetchall()
    print("Data in PostgreSQL: ")
    for row in rows:
        print(row)
        
    conn.close()


def test_mysql():
    conn = mysql.connector.connect(
        host="localhost",
        database="mydatabase",
        user="myuser",
        password="mypassword"
    )
    cur = conn.cursor()
    cur.execute("SELECT version();")
    ver = cur.fetchone()
    print("MySQL version: ", ver)

    cur.execute("SELECT * FROM mytable;")
    rows = cur.fetchall()
    print("Data in MySQL: ")
    for row in rows:
        print(row)

    conn.close()



if __name__ == "__main__":
    test_postgresql()
    test_mysql()