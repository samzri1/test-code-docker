import psycopg2
import mysql.connector
from pymongo import MongoClient

def test_postgresql():
    print("Testing PostgreSQL connection...")
    conn = psycopg2.connect(
        host="localhost",
        database="mydatabase",
        user="myuser",
        password="mypassword"
    )
    cur = conn.cursor()
    cur.execute("SELECT version();")
    ver = cur.fetchone()
    assert ver is not None
    conn.close()
    print("PostgreSQL test completed successfully.")

def test_mysql():
    print("Testing MySQL connection...")
    conn = mysql.connector.connect(
        host="localhost",
        database="mydatabase",
        user="myuser",
        password="mypassword"
    )
    cur = conn.cursor()
    cur.execute("SELECT version();")
    ver = cur.fetchone()
    assert ver is not None
    conn.close()
    print("MySQL test completed successfully.")

def test_mongodb():
    print("Testing MongoDB connection...")
    client = MongoClient('mongodb://myuser:mypassword@localhost:27017/')
    db = client['mydatabase']
    collection = db['mycollection']
    post = {"title": "Test post", "body": "This is a test post."}
    post_id = collection.insert_one(post).inserted_id
    assert post_id is not None
    client.close()
    print("MongoDB test completed successfully.")

if __name__ == '__main__':
    test_postgresql()
    test_mysql()
    test_mongodb()
