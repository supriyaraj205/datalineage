import mysql.connector

def database_connection(insert_query):
  conn = mysql.connector.connect(
      host="127.0.0.1",
      user="root",
      password="root",
      database="organization_info"
  )
  cursor = conn.cursor()
  sql = "show table"
  cursor.execute(insert_query)
  conn.commit()
  cursor.close()
  conn.close()

