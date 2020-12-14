import mysql.connector

init = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234",
)
init_db = init.cursor(buffered=True)
init_db.execute("CREATE DATABASE IF NOT EXISTS zizzle;")

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234",
  database="zizzle"
)

zizzle = mydb.cursor(buffered=True)
