import os
import csv
from s6 import database_connection

path='C:/Users/supri/Desktop/cust'
my_file=''
for root,dir,files in os.walk(path):
    print(root,files)
    for file in files:
        print(file)
        if file.endswith(".csv"):
            if file == 'customer_data.csv':
             print(file)
             table='customer_data'
             database='custm'
             with open(root+'/'+file,'r')as file_data:
                    rows=csv.reader(file_data)
                    header=next(rows)
                    print(header)
                    for row in rows:
                        print(row)
                        insert_query = f"insert into customer_data values {tuple(row)} "
                        print(insert_query)
                        database_connection(insert_query)