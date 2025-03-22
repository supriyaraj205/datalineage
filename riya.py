import mysql.connector

def database_connection(insert_query):
    conn=mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="root",
        database="customer_info"
    )
    cursor=conn.cursor()

    #sql="show tables"
    cursor.execute(insert_query)
    #tables = cursor.fetchall()
    #print(tables)
    conn.commit()
    cursor.close()
    conn.close()

#database_connection()
