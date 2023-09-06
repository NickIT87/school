import mysql.connector

# Replace the placeholders with your MySQL database credentials
db_config = {
    'host': 'localhost',
    'user': 'nick',
    'password': 'klim1987',
    'database': 'test'
}

# Connect to MySQL server
connection = mysql.connector.connect(**db_config)
cursor = connection.cursor()

#cursor.execute("CREATE DATABASE IF NOT EXISTS test")
cursor.execute("CREATE TABLE IF NOT EXISTS Person (name VARCHAR(255), age smallint UNSIGNED, personID int PRIMARY KEY)")
cursor.execute("INSERT INTO Person (name, age, personID) VALUES (%s, %s, %s)", ("Tim", 45, 1))
connection.commit()
cursor.execute("DESCRIBE Person")
for x in cursor:
    print(x)
cursor.execute("SELECT * FROM Person")
for x in cursor:
    print(x)

cursor.close()
connection.close()
