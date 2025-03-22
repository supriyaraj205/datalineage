import os
import csv
from riya import database_connection

source_path='C:/Users/supri/Desktop/mydata'




for root,dir,files in os.walk(source_path):
    print(root,files)
    for file in files:
        if file.endswith('.csv'):
            if file == 'customers-10000.csv':
                print(file)
                with open(root+'/'+file,'r') as file_data:
                    rows = csv.reader(file_data)
                    header = next(rows)
                    #print(header)
                    for row in rows:
                        #print(row)
                        insert_query = f"insert into customer_data values {tuple(row)}"
                        #print(insert_query)
                        database_connection(insert_query)

