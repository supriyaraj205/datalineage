import os
import csv
import datetime

from s1 import database_connection

source_path='C:/Users/supri/Desktop/mydata'
table=''
db=''
for root,dir,files in os.walk(source_path):
    print(root,files)
    for file in files:
        if file.endswith(".csv"):
            if file =='organizations-10000.csv':
                table = "organ_data"
                db= "organization_info"
            elif file=="customers-10000.csv":
                table= "customer_data"
                db="customer_info"
            print(root+'/'+file)
            my_file=root+'/'+file
            with open(my_file,'r')as file_data:
                rows=csv.reader(file_data)
                header=next(rows)
                for row in rows:

                    if file=="customers-10000.csv":
                        insert_query=f"""insert into {table} 
                        (IndexId,customerId,FirstName,LastName,Company,City,
                        Country,Phone1,Phone2,Email,SubscriptionDate,Website) 
                        values 
                        (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""

                        #print(insert_query)
                        #print(row)
                        #print(row[10])
                        #print(type(row[10]))
                        changed_date = datetime.datetime.strptime(row[10], '%d-%m-%Y')
                        #print(type(date))
                        row[10]= changed_date.strftime('%Y-%m-%d')
                        print(row[10])
                    elif file =='organizations-10000.csv':
                        insert_query = f"""insert into {table} 
                                                (id,organization,name,website,country,description,founded,industry,
                                                numberofemployees) 
                                                values 
                                                (%s, %s, %s, %s, %s, %s, %s, %s, %s)"""

                    database_connection(insert_query,row,db)


