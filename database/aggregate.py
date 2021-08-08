from database.models import DB
import csv

class Aggregate:
    def __init__(self):
        self.obj = DB()
        self.db = self.obj.session
        self.conn = self.obj.conn

    def getAggregateCSV(self):
        print ("-- Grabbing aggregated data into CSV")
        data = self.conn.execute("select name, count(name) as 'no. of products' from demo.Products group by name")
        header = ['name', 'no. of products']

        with open('dataset/aggregate.csv', 'w', encoding='UTF8', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(header)
            writer.writerows(data)
    
    def getAggregateDB(self):
        print ("-- Grabbing aggregated data into table")
        data = self.conn.execute("select name, count(name) as 'no. of products' from demo.Products group by name")
        result ={}
        for row in data:
            i = row.name
            if not i in result:
                result[i]={
                    'name': row['name'],
                    'noofproducts': row['no. of products']
                }
        return result