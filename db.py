import mysql.connector

init = mysql.connector.connect(
  host="localhost",
  user="", # set username
  password="", # set password
)
init_db = init.cursor(buffered=True)
init_db.execute("CREATE DATABASE IF NOT EXISTS zizzle;")

mydb = mysql.connector.connect(
  host="localhost",
  user="", # set username
  password="", # set password
  database="zizzle"
)

zizzle = mydb.cursor(buffered=True)
