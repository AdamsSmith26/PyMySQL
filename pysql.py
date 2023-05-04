import mysql.connector

mydb = mysql.connector.connect(
  host='localhost',
  user="root",
  password="root",
  database = "sakila"
)

mycursor = mydb.cursor()

# mycursor.execute("SHOW TABLES")
# mycursor.execute("SELECT * FROM sakila.actor;")
mycursor.execute("SELECT * FROM sakila.actor WHERE first_name = 'SCARLETT';")

for i in mycursor:
  print(i)