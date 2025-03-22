import mysql.connector

import mysql.connector

def database_connection(insert_query,row,db):
  conn = mysql.connector.connect(
      host="127.0.0.1",
      user="root",
      password="root",
      database=db
  )
  cursor = conn.cursor()
  #sql = "show table"
  cursor.execute(insert_query,row)
  conn.commit()
  cursor.close()
  conn.close()