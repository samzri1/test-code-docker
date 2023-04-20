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


def test_mongodb():
    client = MongoClient('mongodb://myuser:mypassword@localhost:27017/')
    db = client['mydatabase']
    collection = db['mycollection']
    post = {"title": "Test post", "body": "This is a test post."}
    post_id = collection.insert_one(post).inserted_id
    print("Inserted post with ID: ", post_id)

    posts = collection.find()
    print("Data in MongoDB: ")
    for post in posts:
        print(post)

    client.close()


def test_postgresql_insert():
    conn = psycopg2.connect(
        host="localhost",
        database="mydatabase",
        user="myuser",
        password="mypassword"
    )
    cur = conn.cursor()
    cur.execute("INSERT INTO mytable (id, name) VALUES (3, 'John');")
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
    cur.execute("INSERT INTO mytable (id, name) VALUES (3, 'John');")
    conn.commit()
    print("Inserted data into MySQL")
    conn.close()


def test_mongodb_insert():
    client = MongoClient('mongodb://myuser:mypassword@localhost:27017/')
    db = client['mydatabase']
    collection = db['mycollection']
    post = {"title": "Another test post", "body": "This is another test post."}
    post_id = collection.insert_one(post).inserted_id
    print("Inserted post with ID: ", post_id)
    client.close()


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




def create_table_mysql():
    conn = mysql.connector.connect(
        host="localhost",
        database="mydatabase",
        user="myuser",
        password="mypassword"
    )
    cur = conn.cursor()
    cur.execute("CREATE TABLE mytable (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255));")
    conn.commit()
    conn.close()




if __name__ == "__main__":

    #create_table_mysql()
    #create_table_postgresql()
  #  test_postgresql_insert()
  #  test_mysql_insert()
  #  test_mongodb_insert()
    
    test_postgresql()
    test_mysql()
    test_mongodb()

    


#pytest test2.py