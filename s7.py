import os
import csv
from s6 import database_connection

paths_tables = {'order_data':'C:/Users/supri/Desktop/orderinformation',"shipment_data":'C:/Users/supri/Desktop/ship'}
for table , path in paths_tables.items():
    my_file=''
    for root,dir,files in os.walk(path):
        print(root,files)
        for file in files:
            if file.endswith(".csv"):
                if file == 'csv_shipment.csv' or  file=='csv_order_data.csv':
                    print(file)
                    database='custm'
                    with open(root+'/'+file,'r')as file_data:
                          rows=csv.reader(file_data)
                          header=next(rows)
                          print(header)
                          for row in rows:
                              print(row)
                              insert_query = f"insert into {table} values {tuple(row)} "
                              print(insert_query)
                              database_connection(insert_query)